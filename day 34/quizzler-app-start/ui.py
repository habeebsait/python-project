THEME_COLOR = "#375362"


from tkinter import *
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import time

user_answer = "w"

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)



quiz = QuizBrain(question_bank)

i=0

def main():
    canvas.config(bg = "white")
    canvas.itemconfig(question_text, text = quiz.q_text)

def choose_true():
    global user_answer
    user_answer = "true"
    ui_check_answer()

def choose_false():
    global user_answer
    user_answer = "false"
    ui_check_answer()

def get_next_question():
    if user_answer == "w":
        canvas.config(bg = "white")
    elif quiz.correct_answer.lower() == user_answer.lower():
        canvas.config(bg= "#2dd10d")

    else:
        canvas.config(bg = "#cf0606")

    print(user_answer)
    quiz.next_question()
    window.after(500, main)
    
    


def ui_check_answer():
    global i
    i+=1
    if i == 10:
        quiz.check_answer(user_answer)
        canvas.destroy()
        true_button.destroy()
        false_button.destroy()
        score_label.config(text = f"Final Score: {quiz.score} \n You've completed the quiz!!", font = ("Arial", 40, "normal"))
        score_label.place(x=0, y=200)
        
        
    else:
        quiz.check_answer(user_answer)
        score_label.config(text = f"Score: {quiz.score}")
        get_next_question()
    




window = Tk()
window.minsize(550,600)
window.config(bg = THEME_COLOR, padx=20, pady =20)
window.after(1000, get_next_question)

score_label = Label(text = "Score: 0", bg = THEME_COLOR, pady=30)
score_label.place(x=300, y=0)

canvas = Canvas(background= "white" , width =300, height = 250)
canvas.place(x=100, y=100)
question_text = canvas.create_text(150,125, text = "", width = 250, fill = "black")


true_image = PhotoImage(file = "day 34/quizzler-app-start/images/true.png")
true_button = Button(image= true_image, command= choose_true)
true_button.place(x=100,y=400)

false_image = PhotoImage(file = "day 34/quizzler-app-start/images/false.png")
false_button = Button(image= false_image, command = choose_false)
false_button.place(x=300,y=400)

















window.mainloop()