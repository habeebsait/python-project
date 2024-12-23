from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

n = len(question_data)
i =0




question_bank = []

while i < n:
    pass
    question = Question(question_data[i]["text"], question_data[i]["answer"])
    question_bank.append(question)

    i += 1
    

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    quiz.check_score()