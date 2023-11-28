from question_model import Question
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for item in question_data:
    question_to_append = Question(item['text'], item['answer'])
    question_bank.append(question_to_append)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():
    
    quiz.next_question()

print (f"Congrats. You completed the quiz. Your final score is {quiz.score}/{quiz.question_number}")