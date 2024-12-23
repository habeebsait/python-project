from flask import Flask, render_template
import random
from datetime import datetime

year = datetime.now().year

app = Flask(__name__)

@app.route("/")
def home():
    num= random.randint(1,10)
    return render_template("index.html", rnum = num, year = year)


if __name__ == "__main__":
    app.run()
