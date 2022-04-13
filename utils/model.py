import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json


class FacialExpressionRecognizer(object):

    EMOTIONS_LIST = ["Angry", "Happy", "Neutral", "Sad", "Surprise"]

    def __init__(self, model_json_file, model_weights_file):
        with open(model_json_file, "r") as json_file:
            loaded_model_json = json_file.read()
            self.loaded_model = model_from_json(loaded_model_json)

        self.loaded_model.load_weights(model_weights_file)


    def predict_emotion(self, img):
        self.preds = self.loaded_model.predict(img)

        return FacialExpressionRecognizer.EMOTIONS_LIST[np.argmax(self.preds)]
