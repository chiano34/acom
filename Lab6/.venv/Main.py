import cv2
import numpy as np
from keras.src.saving import load_model

def perceptron():
    model = load_model('perceptron.keras')
    img = cv2.imread('5.png', cv2.IMREAD_GRAYSCALE)
    img = img / 255.0
    img = img.reshape(1, 784)
    predictions = model.predict(img)
    predicted_digit = np.argmax(predictions)
    print(f"Предполагаемый результат: {predicted_digit}")
def cnn():
    model = load_model('cnn_adam_2sl_15ep.keras')
    img = cv2.imread('5.png', cv2.IMREAD_GRAYSCALE)
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)
    predictions = model.predict(img)
    predicted_digit = np.argmax(predictions)
    print(f"Предполагаемый результат: {predicted_digit}")
cnn()