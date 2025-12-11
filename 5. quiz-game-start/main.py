from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    n_text= question["text"]
    n_answer= question["answer"]
    obj_question = Question(question_text=n_text,answer_text=n_answer)
    question_bank.append(obj_question)

quiz = QuizBrain(question_bank)
while True:
    if quiz.still_has_question():
        quiz.next_question()
    else:
        print("you completed the quize!")
        print(f"your final score is {quiz.score}/{quiz.question_number}")
        break
























#
# question_list = []
# for question in question_data:
#     new_question = question["text"]
#     new_answer = question["answer"]
#     new_q = Question(question_text=new_question, answer_text=new_answer)
#     question_list.append(new_q)
# print(question_list[3].answer)
#
