import tensorflow as tf
import cv2
import numpy as np


def prediction_model(image):
    model = tf.keras.models.load_model('C:/website/model_classificator/model.h5')
    image = cv2.resize(image, (150, 150))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    prediction = model.predict(image)
    if round(prediction[0][0]) == 1:
        return "Пневмония"
    return "Пневмонии нет"
