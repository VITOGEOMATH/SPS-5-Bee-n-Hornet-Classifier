![alt text](https://github.com/VITOGEOMATH/SPS-5/blob/main/GUI%20Bee%20n%20Hornet%20Classifier.png?raw=true)
![alt text](https://github.com/VITOGEOMATH/SPS-5/blob/main/Lebah%20dan%20Tawon.png?raw=true)
# Sistem pendeteksian suara lebah dan tawon guna mendeteksi hama pada peternakan lebah

Aplikasi ini bertujuan untuk mengembangkan sistem yang dapat membedakan suara lebah dan tawon menggunakan analisis frekuensi, pemrosesan sinyal digital, dan teknologi machine learning. Sistem ini akan menyediakan antarmuka pengguna dengan fitur visualisasi suara, pelatihan model, dan penerapan model ke perangkat IoT berbasis ESP32.

## Authors
1. Muhammad Rif'al Faiz Arivito (2042231067)
2. Emir Hakim Zauhari (2042231069)
3. Kania Nayaka U (2042231033)

Teknik Instrumentasi - Institut Teknologi Sepuluh Nopember Surabaya

## Features

1. **Voice Recording**: Record audio input using a simple and intuitive GUI.
2. **Edge Impulse Integration**: Upload audio data to Edge Impulse for training deep learning models.
3. **ESP32 Integration**: Deploy the trained model to ESP32 for real-time audio classification.
4. **Perekaman Suara** : Aplikasi akan memungkinkan pengguna merekam suara lebah atau tawon secara langsung melalui mikrofon.
5. **Analisis Frekuensi** : Menggunakan pemrosesan sinyal digital untuk mengekstraksi fitur dari suara, seperti frekuensi dominan, intensitas, dan pola waktu.
6. **Visualisasi Plot Suara** : Menampilkan spektrum frekuensi, waveform, dan spektrogram untuk membantu memahami perbedaan karakteristik suara.

## Requirements

### Software
- Bahasa Pemrograman: Python (untuk GUI, pemrosesan sinyal, dan machine learning).
- Framework GUI: PyQt6.
- Framework Machine Learning: TensorFlow, Edge Impulse.
- Database: MySQL.
- Visualisasi: Matplotlib, PyQtGraph.

### Hardware
- ESP32
- Microphone module INMP441 (for ESP32, optional for GUI testing)

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/VITOGEOMATH/SPS-5/tree/main
cd pyqt6-voice-ai
```

### 2. Install Python Dependencies
```bash
pip install PyQt6 pyaudio mysql-connector-python edge-impulse-cli 
```


### 3. Configure Edge Impulse
Install the Edge Impulse CLI and log in:
```bash
npm install -g edge-impulse-cli
edge-impulse-login
```

### 4. Prepare ESP32
Install the ESP32 core in Arduino IDE and ensure necessary libraries are installed.

## Usage

### 1. Run the PyQt6 Application
Start the GUI application:
```bash
python main.py
```

### 2. Record and Analyze
- Use the GUI to record audio.


### 3. Upload to Edge Impulse
- Use the GUI or command line to upload recordings to Edge Impulse for training:
```bash
edge-impulse-uploader recordings/yourfile.wav
```

### 4. Train the Model
- Train a model on Edge Impulse using the uploaded data.

### 5. Export and Deploy to ESP32
- Download the trained model as an Arduino library.
- Include the library in your ESP32 Arduino project.
- Use the model to classify real-time audio inputs.

## Langkah Implementasi

1. Pengumpulan Data
Rekam suara lebah dan tawon di berbagai kondisi.
Simpan data suara dalam format WAV atau MP3, dan labelkan sesuai jenisnya (lebah/tawon).
2. Pemrosesan Data
Gunakan pustaka seperti Librosa atau SciPy untuk analisis sinyal.
Ekstraksi fitur utama seperti Mel-Frequency Cepstral Coefficients (MFCC), spektrum energi, dan spektrum frekuensi.
3. Pelatihan Model
Gunakan platform seperti Edge Impulse atau framework seperti TensorFlow/PyTorch.
Gunakan data suara yang diproses untuk melatih model klasifikasi suara.
4. Visualisasi
Gunakan PyQt6 untuk membangun antarmuka pengguna.
Libatkan modul visualisasi seperti Matplotlib atau PyQtGraph untuk menampilkan grafik suara.
5. Implementasi di ESP32
Konversi model terlatih ke library Arduino menggunakan Edge Impulse.
Gunakan modul mikrofon seperti INMP441 untuk mendeteksi suara secara real-time di ESP32.
6. Pengunggahan ke MySQL
Simpan data rekaman suara dan hasil klasifikasi ke database MySQL untuk analisis lebih lanjut.


## Project Structure
```
pyqt6-voice-ai/
├── Bee n Hornet Beta.py                       # PyQt6 GUI Application
├── QT DESIGN BEE n HORNET Classifier          # Voice recording logic
└── README.md                                  # Project documentation
```

## Future Improvements

- Menambahkan dukungan untuk beberapa bahasa pada aplikasi, sehingga laporan hasil analisis suara dapat ditampilkan dalam bahasa pilihan pengguna.
Integrasi API terjemahan seperti Google Translate atau DeepL untuk fleksibilitas bahasa dalam laporan hasil klasifikasi.
Peningkatan Antarmuka Pengguna (GUI)

- Redesign GUI dengan tampilan yang lebih modern dan ramah pengguna.
Menambahkan mode gelap (dark mode) untuk kenyamanan visual.
Menyediakan fitur drag-and-drop untuk mengunggah file suara secara langsung.
Memberikan indikator proses real-time, seperti loading bar untuk perekaman suara atau pelatihan model.
Optimasi Performa Model pada ESP32

- Mengoptimalkan model machine learning untuk performa rendah latensi dan efisiensi daya di perangkat ESP32.
Menggunakan teknik seperti kuantisasi model (model quantization) atau prunasi model (model pruning) untuk mengurangi ukuran model tanpa mengorbankan akurasi.
Penambahan Jenis Suara Baru

- Memperluas dataset untuk mendukung klasifikasi jenis suara serangga lainnya, seperti nyamuk atau capung.
Menyediakan fitur "Add New Category" agar pengguna dapat melatih model dengan data suara baru.
Integrasi Cloud untuk Analisis Lanjutan

- Menyediakan opsi untuk mengunggah data ke cloud (seperti AWS atau Google Cloud) untuk analisis skala besar dan penyimpanan data.
Menambahkan fitur untuk melihat laporan historis dan analisis tren suara lebah atau tawon.
Notifikasi dan Alarm Otomatis

- Mengembangkan sistem notifikasi otomatis yang memberikan peringatan jika suara tawon terdeteksi dalam lingkungan.
Menambahkan dukungan untuk notifikasi push melalui aplikasi mobile atau email.
Visualisasi Data Lanjutan

- Menggunakan grafik 3D untuk menunjukkan spektrum suara secara lebih interaktif.
Menyediakan analisis perbandingan suara lebah dan tawon untuk memvisualisasikan perbedaan lebih mendalam.
Penggunaan AI di Edge Devices

- Integrasi dengan microcontroller yang lebih canggih seperti Raspberry Pi Pico atau STM32 untuk mendukung inferensi model lebih kompleks.
Menambahkan kemampuan untuk mendeteksi suara secara langsung dari beberapa perangkat sekaligus dalam jaringan IoT.
Pengembangan Fitur Edukasi

- Menyediakan modul edukasi dalam aplikasi untuk memahami karakteristik suara lebah dan tawon.
Menambahkan gamifikasi sederhana, seperti kuis pengenalan suara, untuk pengguna anak-anak.
Dukungan Hardware Tambahan

- Mendukung mikrofon eksternal yang lebih sensitif untuk akurasi pengambilan suara yang lebih tinggi.
Menambahkan opsi untuk menghubungkan perangkat dengan sensor lingkungan seperti suhu dan kelembapan untuk analisis lebih kontekstual.

## Contributions
Feel free to fork this repository and submit pull requests. Suggestions and improvements are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Reference
https://www.gov.mb.ca/housing/pubs/pests/bees.pdf
https://www.bbc.com/news/science-environment-66697968
