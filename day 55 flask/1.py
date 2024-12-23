from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello"

@app.route("/<name>")
def greet(name):
    return f"Hello {name+12}"

if __name__ == "__main__":
    app.run(debug=True)
