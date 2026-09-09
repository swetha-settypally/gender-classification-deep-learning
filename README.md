# Gender Classification using Deep Learning

A deep learning project that classifies facial images into male and female categories using a Convolutional Neural Network (CNN).

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pillow

## Dataset

The project uses the UTKFace dataset. Images are organized into male and female folders based on the labels provided in the dataset.

## Model

A CNN model is used with:

- Convolutional layers
- Max Pooling layers
- Flatten layer
- Dense layers
- Dropout layer
- Sigmoid output layer

## Results

The model achieved approximately **90.81% validation accuracy** after 10 epochs.

## Project Files

- `prepare_dataset.py` - Prepares and organizes the dataset
- `train_model.py` - Builds and trains the CNN model
- `evaluate_model.py` - Evaluates model performance
- `predict.py` - Predicts the class of a single image
- `.gitignore` - Prevents dataset and model files from being uploaded

## How to Run

Install the required libraries:

```bash
python -m pip install tensorflow pillow numpy matplotlib scikit-learn
