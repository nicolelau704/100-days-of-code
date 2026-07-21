from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#Create a bank of questions objects using the information in question_data
question_bank = []

for item in question_data:
    question_bank.append(Question(item["question"], item["correct_answer"]))

#Create a quiz object
quiz = QuizBrain(question_bank)

#Keep asking questions until there are no more left then display the results of the quiz
while quiz.still_has_questions():
    quiz.next_question()
