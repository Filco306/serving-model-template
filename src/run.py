from flask import Flask, jsonify
from src.model import Model
from dotenv import load_dotenv
import os

if load_dotenv() is False:
    raise Exception("Environment file not loaded. ")

app = Flask(__name__)

model = Model()


@app.route("/health", methods=["GET"])
def health():
    """ Health function for checking the health of the container or server """
    return jsonify({"status": "200 OK"})


@app.route("/serve", methods=["POST"])
def serve():
    """" Serving function, returning predictions.  """
    prediction = model.predict(x=None)
    return jsonify({"status": "200", "prediction": float(prediction)})


if __name__ == "__main__":
    app.run(debug=os.environ.get("IS_PROD", "FALSE") == "TRUE")
