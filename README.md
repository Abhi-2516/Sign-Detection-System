# Hand Sign Prediction using Machine Learning

A machine learning project that predicts hand signs across **10-2 classes** with an accuracy of **85%**.

## Features
- **Hand Sign Recognition**: Classifies hand gestures into predefined categories.
- **Deep Learning Model**: Trained on a dataset of hand gestures.
- **85% Accuracy**: Achieved using optimized model training.
- **Real-time Prediction**: Supports live camera input for real-time hand sign detection.
- **User-friendly Interface**: Simple UI for uploading images and getting predictions.

## Technologies Used
- **Python**
- **TensorFlow / Keras**
- **OpenCV**
- **NumPy, Pandas**
- **Matplotlib / Seaborn**
- **Flask (for Web Deployment)**

## Installation

### Clone the Repository
```sh
git clone https://github.com/Abhi-2516/hand-sign-prediction.git
cd hand-sign-prediction
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Run the Application
```sh
python app.py
```
The app will be accessible at `http://localhost:5000/`.

## Dataset
The model was trained on a labeled dataset of hand gestures, preprocessed using OpenCV and augmented for better performance.

## Model Training
1. Data Preprocessing (resizing, normalization, augmentation)
2. CNN Model Training (Convolutional layers, Pooling, Dense layers)
3. Evaluation & Hyperparameter Tuning
4. Achieved **85% accuracy**

## Usage
1. Upload an image of a hand sign.
2. The model predicts the sign and displays the result.
3. For real-time detection, the webcam captures hand signs and predicts them live.

## Contributing
Contributions are welcome! If you want to improve this project, feel free to fork the repo and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For inquiries, contact me at: [2516abhi43@gmail.com](mailto:2516abhi43@gmail.com)

