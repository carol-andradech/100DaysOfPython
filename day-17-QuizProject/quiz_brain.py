#TODO: ask question
#TODO: check if answer is correct
#TODO: check if is the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} True or False? ")
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Yoy got it right!")
        else:
            print("That's wrong.")
        print(f"You current score is: {self.score}/{self.question_number}")