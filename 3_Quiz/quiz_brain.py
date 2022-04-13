
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        q_answer = self.question_list[self.question_number].answer
        q_text = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q_text} (True/False)?: ")
        self.check_answer(q_answer, user_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, q_answer, user_answer):
        if q_answer.lower() == user_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect!")
        print(f"The correct answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")