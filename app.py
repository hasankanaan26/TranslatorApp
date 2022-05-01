import os
import logging

from flask import Flask, request, jsonify

from model.model import  SentenceTranslator

app = Flask(__name__)  

# define model path
model_path = './model/model.h5'

# create instance
model = SentenceTranslator(model_path)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    """Provide simple health check route."""
    return "Hello world, welcome to our translation app!"


@app.route("/v1/translate", methods=["GET", "POST"])
def predict():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    logging.info("Translation request received!")
    sentence = request.args.get("sentence")
    translation = model.predict(sentence)
    
    logging.info("translation from model= {}".format(translation))
    return jsonify({"translation": str(translation)})

def main():
    """Run the Flask app."""
    app.run(host="0.0.0.0", port=8000, debug=False) 


if __name__ == "__main__":
    main()