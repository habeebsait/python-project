class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.answer = input(f"Q{self.question_number}: {current_question.text} (True/False): ")
        
    def check_score(self):
        correct_answer = self.question_list[self.question_number-1]
        if self.answer == correct_answer.answer:
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong!")

        print(f"The correct answer was: {self.question_list[self.question_number-1].answer}")

        print(f"Your current score is: {self.score}/{self.question_number}")
        