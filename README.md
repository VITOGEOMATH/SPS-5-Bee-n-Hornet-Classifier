![alt text](https://github.com/VITOGEOMATH/SPS-5/blob/main/GUI%20Bee%20n%20Hornet%20Classifier.png?raw=true)
![alt text](https://github.com/VITOGEOMATH/SPS-5/blob/main/Lebah%20dan%20Tawon.png?raw=true)
# Bee and wasp sound detection system to detect pests in beekeeping

This application aims to develop a system that can distinguish bee and wasp sounds using frequency analysis, digital signal processing, and machine learning technologies. The system will provide a user interface with sound visualization features, model training, and model deployment to ESP32-based IoT devices.

## Authors
1. Ahmad Radhy (Supervisor)
2. Muhammad Rif'al Faiz Arivito (2042231067)
3. Emir Hakim Zauhari (2042231069)
4. Kania Nayaka U (2042231033)

Instrumentation Engineering - Institut Teknologi Sepuluh Nopember ( ITS ) Surabaya, Indonesia

## Features

1. **Voice Recording**: The application allows users to record audio through an intuitive and user-friendly interface.
2. **Edge Impulse Integration**: Audio data is uploaded to Edge Impulse for training deep learning models.
3. **ESP32 Integration**: The trained model is deployed to an ESP32 device for real-time audio classification.
4. **Sound Recording**: The application will enable users to directly record the sounds of bees or wasps using the microphone.
5. **Frequency Analysis**: Digital signal processing techniques are used to extract features from the sound, such as dominant frequency, intensity, and temporal patterns.
6. **Sound Visualization**: The application displays frequency spectrum, waveform, and spectrogram to assist in understanding the characteristics of the sound.

## Requirements

### Software
- Programming Language: Python (for GUI, signal processing, and machine learning).
- GUI framework: PyQt6.
- Machine Learning Framework: TensorFlow, Edge Impulse.
- Database: MySQL.
- Visualization: Matplotlib, PyQtGraph.

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

1. Data Collection
Record the sounds of bees and wasps in various conditions.
Save the sound data in WAV or MP3 format, and label them according to their type (bee/wasp).
2. Data Processing
Use libraries such as Librosa or SciPy for signal analysis.
Extract key features such as Mel-Frequency Cepstral Coefficients (MFCC), energy spectrum, and frequency spectrum.
3. Model Training
Use a platform such as Edge Impulse or a framework such as TensorFlow/PyTorch.
Use the processed speech data to train the speech classification model.
4. Visualization
Use PyQt6 to build the user interface.
Involve visualization modules such as Matplotlib or PyQtGraph to display voice graphs.
5. Implementation on ESP32
Convert the trained model to an Arduino library using Edge Impulse.
Use a microphone module like INMP441 to detect sound in real-time on the ESP32.
6. Upload to MySQL
Save the voice recording data and classification results to MySQL database for further analysis.


## Project Structure
```
pyqt6-voice-ai/
├── Bee n Hornet Beta.py                       # PyQt6 GUI Application
├── QT DESIGN BEE n HORNET Classifier          # Voice recording logic
└── README.md                                  # Project documentation
```

## Future Improvements

- Adding support for multiple languages to the application, so that voice analysis reports can be displayed in the user's preferred language.
Integration of translation APIs such as Google Translate or DeepL for language flexibility in classification result reports.
User Interface (GUI) Improvements

- GUI redesign with a more modern and user-friendly look.
Added dark mode for visual comfort.
Provided drag-and-drop feature to upload sound files directly.
Provides real-time process indicators, such as loading bars for voice recording or model training.
Model Performance Optimization on ESP32

- Optimize machine learning models for low-latency performance and power efficiency on ESP32 devices.
Use techniques such as model quantization or model pruning to reduce model size without sacrificing accuracy.
Addition of New Voice Types

- Expanding the dataset to support classification of other insect sound types, such as mosquitoes or dragonflies.
Provides an “Add New Category” feature for users to train the model with new sound data.
Cloud Integration for Advanced Analysis

- Provides the option to upload data to the cloud (such as AWS or Google Cloud) for large-scale analysis and data storage.
Added features to view historical reports and trend analysis of bee or wasp sounds.

Automatic Notification and Alarm

- Developed an automatic notification system that provides alerts if wasp sounds are detected in the environment.
Added support for push notifications via mobile app or email.
Advanced Data Visualization

- Use 3D graphics to show the sound spectrum more interactively.
Provides comparative analysis of bee and wasp sounds to visualize the differences in more depth.
Use of AI in Edge Devices

- Integration with more advanced microcontrollers such as Raspberry Pi Pico or STM32 to support more complex model inference.
Adding the ability to detect live voice from multiple devices at once in an IoT network.
Educational Feature Development

- Provide an in-app educational module to understand the sound characteristics of bees and wasps.
Added simple gamification, such as voice recognition quizzes, for child users.
Additional Hardware Support

- Supports more sensitive external microphones for higher sound picking accuracy.
Added option to connect the device with environmental sensors such as temperature and humidity for more contextual analysis.

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
