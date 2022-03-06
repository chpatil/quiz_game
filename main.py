from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_bank.append(Question(i["question"], i["correct_answer"]))
# print(question_bank)
quiz_brain_object = QuizBrain(question_bank)
# print(quiz_brain_object.next_question())
while quiz_brain_object.has_next_question():
    quiz_brain_object.next_question()
print("You have completed the quiz")
print(f"Your final score is {quiz_brain_object.score}/{quiz_brain_object.question_number} ")
