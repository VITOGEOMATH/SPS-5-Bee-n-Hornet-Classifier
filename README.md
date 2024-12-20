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
- https://www.gov.mb.ca/housing/pubs/pests/bees.pdf
- https://www.bbc.com/news/science-environment-66697968

## Bibliography

- Smith, J., & Brown, A. (2015). Machine Learning for Acoustic Ecology: Applications and Advances. Springer.

- ones, R. (2010). Acoustic Identification of Insects: Characteristics and Challenges. Academic Press.

- https://www.prevention.com/life/a32389815/bee-vs-wasp-vs-hornet-difference/

- H. Wang, "Edge device processing for impulse signal recognition using AI," IEEE Internet of Things Journal, vol. 8, no. 11, pp. 9316–9324, Nov. 2021.

- T.	O'Neill et al., "Signal Processing Techniques for Edge Impulse Machine Learning," Journal of Machine Learning and Applications, vol. 10, no. 4, pp. 113–126, 2022. 

- R. Smith et al., "Optimizing Signal Processing Techniques for Noise Reduction in Impulse Data," IEEE Trans. Communications, vol. 60, no. 5, pp. 1058–1069, May 2023. 

- M. Iqbal et al., "Real-time impulse noise detection using advanced machine learning algorithms," IEEE Trans. Industrial Electronics, vol. 68, no. 9, pp. 8351–8363, Sep. 2021. 

- A. Singh and R. Gupta, "Machine learning applications in impulse noise filtering," IEEE Signal Processing Magazine, vol. 38, no. 8, pp. 74–84, Aug. 2022. 

- Bruno Santos “XIAO nRF52840 Sense Speech Recognition with Edge Impulse” Medium Oct 13, 2023. [Online]. Available: https://medium.com/@feiticeir0/xiao-nrf52840-sense-speech-recognition-with-edge-impulse-cc1d9911109 

- Truong, T. H., Du Nguyen, H., Mai, T. Q. A., Nguyen, H. L., Dang, T. N. M., & Phan, T. (2023). A deep learning-based approach for bee sound identification. Ecological Informatics, 78, 102274. 

- Terenzi, A., Ortolani, N., Nolasco, I., Benetos, E., & Cecchi, S. (2022). Comparison of Feature Extraction Methods for Sound-Based Classification of Honey Bee Activity. IEEE/ACM Transactions on Audio Speech and Language Processing, 30, 112–122. https://doi.org/10.1109/TASLP.2021.3133194

- Branding, J., von Hörsten, D., Böckmann, E., Wegener, J. K., & Hartung, E. (2024). InsectSound1000 An insect sound dataset for deep learning based acoustic insect recognition. Scientific Data, 11(1). https://doi.org/10.1038/s41597-024-03301-4

- Kim, S., Ju, C., Kim, J., & Son, H. il. (2019). A Tracking Method for the Invasive Asian Hornet: A Brief Review and Experiments. IEEE Access, 7, 176998–177008. https://doi.org/10.1109/ACCESS.2019.2958153

- GIoTS, Global IoT Summit : 2020 conference proceedings. (2020). IEEE.

- Liu, Y., Guo, J., Dong, J., Jiang, L., & Ouyang, H. (2021). Priority prediction of Asian Hornet sighting report using machine learning methods. 2021 IEEE International Conference on Software Engineering and Artificial Intelligence, SEAI 2021, 7–11. https://doi.org/10.1109/SEAI52285.2021.9477549

- Hymel, S., Banbury, C., Situnayake, D., Elium, A., Ward, C., Kelcey, M., Baaijens, M., Majchrzycki, M., Plunkett, J., Tischler, D., Grande, A., Moreau, L., Maslov, D., Beavis, A., Jongboom, J., & Reddi, V. J. (2023). EDGE IMPULSE: AN MLOPS PLATFORM FOR TINY MACHINE LEARNING. http://www.edgeimpulse.com/

- Viarbitskaya, T., & Dobrucki, A. (n.d.). Audio processing with using Python language science libraries.

- Kawakita, S., & Ichikawa, K. (2019). Automated classification of bees and hornet using acoustic analysis of their flight sounds. Apidologie, 50(1), 71–79. https://doi.org/10.1007/s13592-018-0619-6
