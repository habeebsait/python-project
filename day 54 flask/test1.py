from flask import Flask, render_template
import random

app = Flask(__name__)

num = random.randint(0,10)
print(num)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/{num}")
def number():
    return "Perfectttt"



app.run()
