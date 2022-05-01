import os
# hide TF warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

from PIL import Image
from urllib.request import urlretrieve

import logging

class SentenceTranslator:

    def __init__(self, model_path):
        logging.info("SentenceTranslator class initialized")
        self.model = load_model(model_path)
        logging.info("Model is loaded!")
        

    def predict(self, sentence):
        # come up with a translation
        print("now I am here")
        #em lmees this is not working corrently 
        return self.model.predict(sentence)


def main():
	model = SentenceTranslator('model/h5')
	translated_senetnce = model.predict("I love the way you lie")
	logging.info("This is the  translation {}".format(translated_senetnce)) 

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()