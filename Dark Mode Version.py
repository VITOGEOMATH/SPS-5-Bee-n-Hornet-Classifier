import sys
import os
import json
import pyaudio
import threading
import numpy as np
from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.fftpack import fft
from scipy.io.wavfile import write
import requests

def classify_signal(frequency_data, tawon_range, lebah_range):
    tawon_power = np.sum((frequency_data >= tawon_range[0]) & (frequency_data <= tawon_range[1]))
    lebah_power = np.sum((frequency_data >= lebah_range[0]) & (frequency_data <= lebah_range[1]))
    if tawon_power > lebah_power:
        return "Tawon"
    elif lebah_power > tawon_power:
        return "Lebah"
    else:
        return "Tidak Diketahui"

class LivePlotWidget(FigureCanvas):
    def __init__(self, title="", xlabel="", ylabel="", parent=None):
        self.figure = Figure(facecolor='black')
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)

        # Set dark theme
        self.ax.set_facecolor('#1e1e1e')
        self.ax.tick_params(colors='white')
        self.ax.spines['bottom'].set_color('white')
        self.ax.spines['left'].set_color('white')
        self.ax.xaxis.label.set_color('white')
        self.ax.yaxis.label.set_color('white')
        self.ax.title.set_color('white')

        # Add titles and labels
        self.ax.set_title(title, fontsize=10)
        self.ax.set_xlabel(xlabel, fontsize=8)
        self.ax.set_ylabel(ylabel, fontsize=8)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bee and Hornet Classifier")
        self.setGeometry(100, 100, 1200, 800)

        # Variables for audio recording
        self.recording = False
        self.audio_thread = None
        self.frames = []
        self.sampling_rate = 44100
        self.channels = 1
        self.chunk = 1024
        self.audio = pyaudio.PyAudio()
        self.file_counter = 1
        self.last_saved_file = None

        # Edge Impulse Settings
        self.api_url = "https://ingestion.edgeimpulse.com/api/testing/files"
        self.api_key = "ei_dc83dc55bae805f866cd618e013fff18d8037f56af7f2257cecb501eff3f721f"

        # Main Layout
        main_layout = QtWidgets.QVBoxLayout()

        # Top Layout: Parameters
        params_layout = QtWidgets.QGridLayout()
        self.audio_device_combo = QtWidgets.QComboBox()
        self.audio_device_combo.addItem("Microsoft Sound Mapper - Input")
        self.amplitude_spin = QtWidgets.QSpinBox()
        self.amplitude_spin.setValue(100)
        self.sampling_rate_spin = QtWidgets.QSpinBox()
        self.sampling_rate_spin.setRange(1000, 192000)
        self.sampling_rate_spin.setValue(self.sampling_rate)
        self.update_interval_spin = QtWidgets.QSpinBox()
        self.update_interval_spin.setRange(1, 100)
        self.update_interval_spin.setValue(30)

        params_layout.addWidget(QtWidgets.QLabel("Audio Device"), 0, 0)
        params_layout.addWidget(self.audio_device_combo, 0, 1)
        params_layout.addWidget(QtWidgets.QLabel("Amplitude"), 0, 2)
        params_layout.addWidget(self.amplitude_spin, 0, 3)
        params_layout.addWidget(QtWidgets.QLabel("Sampling Rate (>1000 Hz)"), 0, 4)
        params_layout.addWidget(self.sampling_rate_spin, 0, 5)
        params_layout.addWidget(QtWidgets.QLabel("Update Interval (1 to 100 ms)"), 0, 6)
        params_layout.addWidget(self.update_interval_spin, 0, 7)

        # Plot Buttons
        self.start_button = QtWidgets.QPushButton("Start Record")
        self.stop_button = QtWidgets.QPushButton("Stop Record")
        self.reset_button = QtWidgets.QPushButton("Reset")
        self.save_button = QtWidgets.QPushButton("Save")
        self.play_button = QtWidgets.QPushButton("Play")  # New Play button
        self.analyze_button = QtWidgets.QPushButton("Analyze")
        self.upload_button = QtWidgets.QPushButton("Upload to Edge Impulse")

        params_layout.addWidget(self.start_button, 0, 8)
        params_layout.addWidget(self.stop_button, 0, 9)
        params_layout.addWidget(self.reset_button, 0, 10)
        params_layout.addWidget(self.save_button, 0, 11)
        params_layout.addWidget(self.play_button, 1, 8)  # Add Play button to layout
        params_layout.addWidget(self.analyze_button, 1, 9)
        params_layout.addWidget(self.upload_button, 1, 10)

        main_layout.addLayout(params_layout)

        # Plot Area
        self.plot1 = LivePlotWidget("Original Signal", xlabel="Time", ylabel="Amplitude")
        self.plot2 = LivePlotWidget("DFT of Signal", xlabel="Frequency (Hz)", ylabel="Amplitude")
        self.plot3 = LivePlotWidget("FFT of Signal", xlabel="Frequency (Hz)", ylabel="Magnitude")

        plot_layout = QtWidgets.QVBoxLayout()
        plot_layout.addWidget(self.plot1)
        plot_layout.addWidget(self.plot2)
        plot_layout.addWidget(self.plot3)  # Adding new plot for FFT
        main_layout.addLayout(plot_layout)

        # Recording Duration Display
        duration_layout = QtWidgets.QHBoxLayout()
        self.recording_label = QtWidgets.QLabel("Recording Duration: 0.00 seconds")
        self.analysis_result_label = QtWidgets.QLabel("Analysis Result: Not Analyzed")
        duration_layout.addWidget(self.recording_label)
        duration_layout.addWidget(self.analysis_result_label)
        main_layout.addLayout(duration_layout)

        # Central Widget
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Button Styles
        button_style = """
            QPushButton {
                background-color: #444444; /* Warna tombol */
                color: white; /* Warna teks */
                border: 1px solid #555555; /* Warna border */
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #555555; /* Warna tombol saat hover */
            }
            QPushButton:pressed {
                background-color: #333333; /* Warna tombol saat ditekan */
            }
        """

        self.start_button.setStyleSheet(button_style)
        self.stop_button.setStyleSheet(button_style)
        self.reset_button.setStyleSheet(button_style)
        self.save_button.setStyleSheet(button_style)
        self.play_button.setStyleSheet(button_style)
        self.analyze_button.setStyleSheet(button_style)
        self.upload_button.setStyleSheet(button_style)

        # Connect Buttons
        self.start_button.clicked.connect(self.start_recording)
        self.stop_button.clicked.connect(self.stop_recording)
        self.reset_button.clicked.connect(self.reset_recording)
        self.save_button.clicked.connect(self.save_data)
        self.play_button.clicked.connect(self.play_audio)  # Connect Play button
        self.analyze_button.clicked.connect(self.analyze_signal)
        self.upload_button.clicked.connect(self.upload_last_saved_file)

        # Timer for updating plots and duration
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_plots)

    def start_recording(self):
        if not self.recording:
            self.recording = True
            self.frames = []
            self.audio_thread = threading.Thread(target=self.record_audio)
            self.audio_thread.start()
            self.timer.start(self.update_interval_spin.value())

    def stop_recording(self):
        self.recording = False
        if self.audio_thread:
            self.audio_thread.join()
        self.timer.stop()

    def reset_recording(self):
        self.frames = []
        self.recording_label.setText("Recording Duration: 0.00 seconds")
        self.analysis_result_label.setText("Analysis Result: Not Analyzed")
        self.plot1.ax.clear()
        self.plot2.ax.clear()
        self.plot3.ax.clear()  # Clear the new plot as well
        self.plot1.draw()
        self.plot2.draw()
        self.plot3.draw()

    def save_data(self):
        if self.frames:
            audio_filename = f"audio_data{self.file_counter}.wav"
            write(audio_filename, self.sampling_rate, np.array(self.frames, dtype=np.int16))
            self.file_counter += 1
            self.last_saved_file = audio_filename  # Store the last saved file
            QtWidgets.QMessageBox.information(self, "Save Data", f"Audio data saved successfully as {audio_filename}!")
        else:
            QtWidgets.QMessageBox.warning(self, "Save Data", "No data to save!")

    def upload_last_saved_file(self):
        if self.last_saved_file:
            self.upload_audio_to_edge_impulse(self.last_saved_file)
        else:
            QtWidgets.QMessageBox.warning(self, "Upload Error", "No saved file available for upload!")

    def upload_audio_to_edge_impulse(self, audio_filename):
        try:
            with open(audio_filename, "rb") as f:
                response = requests.post(
                    self.api_url,
                    headers={"x-api-key": self.api_key},
                    files={"data": (os.path.basename(audio_filename), f, "audio/wav")},
                )
            if response.status_code == 200:
                QtWidgets.QMessageBox.information(self, "Upload Success", f"Uploaded {audio_filename} successfully to Edge Impulse!")
            else:
                QtWidgets.QMessageBox.warning(self, "Upload Failed", f"Failed to upload {audio_filename}. Status code: {response.status_code}")
                print("Response text:", response.text)
        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Upload Error", f"Error occurred during file upload: {e}")

    def record_audio(self):
        try:
            stream = self.audio.open(format=pyaudio.paInt16,
                                     channels=self.channels,
                                     rate=self.sampling_rate,
                                     input=True,
                                     frames_per_buffer=self.chunk)
            while self.recording:
                data = stream.read(self.chunk)
                self.frames.extend(np.frombuffer(data, dtype=np.int16))
            stream.stop_stream()
            stream.close()
        except Exception as e:
            print(f"Error during recording: {e}")

    def update_plots(self):
        if self.frames:
            N = len(self.frames)
            x_data = np.linspace(0, N / self.sampling_rate, N)  # Time axis data

            # Update Original Signal Plot
            self.plot1.ax.clear()
            self.plot1.ax.plot(x_data, self.frames[:N], color='red')  # Red for the time-domain signal
            self.plot1.ax.set_xlim(0, max(x_data))  # Set x-axis limits
            self.plot1.ax.set_ylim(-1.0, 1.0)  # Normalize amplitude (if needed)
            self.plot1.ax.set_title("Real-Time Signal", fontsize=10)
            self.plot1.draw()

            # Update DFT Plot
            freq = np.fft.fftfreq(N, d=1 / self.sampling_rate)
            magnitude = np.abs(fft(self.frames[:N]))
            self.plot2.ax.clear()
            self.plot2.ax.plot(freq[:N // 2], magnitude[:N // 2], color='blue')  # Blue for the DFT plot
            self.plot2.ax.set_xlim(0, self.sampling_rate // 2)  # Limit to Nyquist frequency
            self.plot2.ax.set_ylim(0, max(magnitude[:N // 2]))  # Adjust amplitude range
            self.plot2.ax.set_title("DFT of Signal", fontsize=10)
            self.plot2.draw()

            # Update FFT Plot (new plot)
            self.plot3.ax.clear()
            self.plot3.ax.plot(freq[:N // 2], magnitude[:N // 2], color='green')  # Green for FFT plot
            self.plot3.ax.set_xlim(0, self.sampling_rate // 2)
            self.plot3.ax.set_ylim(0, max(magnitude[:N // 2]))
            self.plot3.ax.set_title("FFT of Signal", fontsize=10)
            self.plot3.draw()

            # Update Recording Duration
            duration = len(self.frames) / self.sampling_rate
            self.recording_label.setText(f"Recording Duration: {duration:.2f} seconds")

    def play_audio(self):
        if self.frames:
            try:
                stream = self.audio.open(format=pyaudio.paInt16,
                                         channels=self.channels,
                                         rate=self.sampling_rate,
                                         output=True)
                stream.write(np.array(self.frames, dtype=np.int16).tobytes())
                stream.stop_stream()
                stream.close()
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "Playback Error", f"Error occurred during playback: {e}")
        else:
            QtWidgets.QMessageBox.warning(self, "Playback Error", "No audio data to play!")

    def analyze_signal(self):
        if self.frames:
            freq = np.fft.fftfreq(len(self.frames), d=1/self.sampling_rate)
            magnitude = np.abs(fft(self.frames))
            tawon_range = (200, 450)
            lebah_range = (350, 700)
            result = classify_signal(freq, tawon_range, lebah_range)
            self.analysis_result_label.setText(f"Analysis Result: {result}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Apply dark theme
    dark_theme = """
    QWidget {
        background-color: #121212; /* Warna latar belakang jendela */
        color: white; /* Warna teks */
    }
    QLabel {
        color: white; /* Warna teks label */
    }
    QComboBox, QSpinBox {
        background-color: #1e1e1e; /* Warna latar belakang widget input */
        color: white; /* Warna teks */
        border: 1px solid #333333;
        border-radius: 5px;
        padding: 2px;
    }
    QComboBox QAbstractItemView {
        background-color: #1e1e1e;
        color: white;
    }
    """
    app.setStyleSheet(dark_theme)

    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
