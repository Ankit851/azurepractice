from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Linux World! Ankit Coder <b>hello !!</b>"
