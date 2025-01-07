from flask import Flask
from ML.logger import logging


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    logging.info("Testing")

    return "Done"

if __name__ == "__main__":
    app.run(debug=True)
