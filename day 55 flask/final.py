import random
from flask import Flask

random = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Guess the correct number!!\
    <img src = 'https://media.giphy.com/media/fsu57DW244IyGgikk6/giphy.gif?cid=ecf05e47dqv2hy1qlmw5xyqgu8kwth6psxles02n1ogy3hlb&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"

@app.route("/<int:guess>")
def guess_num(guess):
    if guess > random:
        return "<h1>Guess lower!!</h1>\
            <img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeXNyNTJwbGx6d3JlNGFpeDUyYW04Z3lncDVkZnNmd2Q1bzA1b2ZhaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3OhXBaoR1tVPW/giphy.gif'>"
    
    elif guess < random:
        return "<h1>Guess higher!!</h1>\
            <img src = 'https://media.giphy.com/media/CPRV4t6Zyxa9wCnzCS/giphy.gif?cid=790b7611ysr52pllzwre4aix52am8gygp5dfsfwd5o05ofaj&ep=v1_gifs_search&rid=giphy.gif&ct=g'>"
    
    else:
        return "<h1>Yess uve guessed it right!!!</h1>\
            <img src = 'https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeGl5YmxtMXFkdHN2eHVyZTBzOGVycnZ0YjE2amQwdDBtbWxibzF0aiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BMR4cgypuglVu/giphy.gif'>"
    
app.run()