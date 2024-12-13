 def record_audio(self):
        while self.running:
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            self.audio_data.extend(np.frombuffer(data, dtype=np.int16))

    def update_plots(self):
        if not self.audio_data:
            return

        signal = np.array(self.audio_data)
        normalized_signal = signal / np.max(np.abs(signal) + 1e-6)
        time = np.linspace(0, len(normalized_signal) / self.rate, len(normalized_signal))

        self.plot1.ax.clear()
        self.plot1.ax.plot(time, normalized_signal, color='blue', alpha=0.7, linewidth=2)
        self.plot1.ax.grid(True, linestyle='--', alpha=0.5)
        self.plot1.ax.set_title("Live Signal (Filtered)", fontsize=12, fontweight='bold')
        self.plot1.ax.set_xlabel("Time [s]", fontsize=10)
        self.plot1.ax.set_ylabel("Amplitude", fontsize=10)
        self.plot1.draw()

        impulse_signal = np.diff(normalized_signal)
        self.plot2.ax.clear()
        self.plot2.ax.plot(impulse_signal, color='green', alpha=0.7, linewidth=2)
        self.plot2.ax.grid(True, linestyle='--', alpha=0.5)
        self.plot2.ax.set_title("Impulse Signal", fontsize=12, fontweight='bold')
        self.plot2.ax.set_xlabel("Sample", fontsize=10)
        self.plot2.ax.set_ylabel("Amplitude", fontsize=10)
        self.plot2.draw()

        hz = np.fft.rfftfreq(len(normalized_signal), 1 / self.rate)
        amplitude = np.abs(np.fft.rfft(normalized_signal))
        self.plot4.ax.clear()
        self.plot4.ax.plot(hz, amplitude, color='orange', alpha=0.7, linewidth=2)
        self.plot4.ax.grid(True, linestyle='--', alpha=0.5)
        self.plot4.ax.set_title("DFT (Frequency Domain)", fontsize=12, fontweight='bold')
        self.plot4.ax.set_xlabel("Frequency [Hz]", fontsize=10)
        self.plot4.ax.set_ylabel("Amplitude", fontsize=10)
        self.plot4.draw()

    def update_elapsed_time(self):
        self.elapsed_time += 1
        minutes, seconds = divmod(self.elapsed_time, 60)
        self.time_label.setText(f"Recording Time: {minutes:02}:{seconds:02}")

    def closeEvent(self, event):
        self.running = False
        self.p.terminate()
        event.accept()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
