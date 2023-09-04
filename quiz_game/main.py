from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for ques in question_data:
    new_ques=Question(ques["question"],ques["correct_answer"])
    question_bank.append(new_ques)

quiz=QuizBrain(question_bank)

while(quiz.still_has_questions()):
    quiz.next_question()
    print()

print(f'''
Thank you for taking the quiz.
We appreciate that.
Your final score is {quiz.score}/{quiz.ques_num}
''')