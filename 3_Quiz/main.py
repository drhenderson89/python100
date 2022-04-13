"""Run simple quiz of true/false questions"""

from operator import truediv
from re import T


if __name__=="__main__":
    print("Running Quiz...")

    from question_model import Question
    from data import question_data
    from quiz_brain import QuizBrain

    question_bank=[]
    for q in question_data:
        question_bank.append(Question(q["text"], q["answer"]))

    quiz = QuizBrain(question_bank)
    while(quiz.still_has_questions()):
        quiz.next_question()

    print("Quiz completed!")
    print(f"Your final score was: {quiz.score}/{len(question_bank)}")