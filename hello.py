from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    return "I piloti di F1"