class QuizBrain:
    
   def __init__(self,ques_list):
      self.ques_num=0
      self.score=0
      self.question_list=ques_list
   
   def still_has_questions(self):
      return self.ques_num<len(self.question_list)
   
   def next_question(self):
      question=self.question_list[self.ques_num].text
      correct_answer=self.question_list[self.ques_num].answer
      self.ques_num+=1
      user_answer=input(f"Q.{self.ques_num}: {question} [Ture/False]").title()
      self.check_answer(user_answer,correct_answer)

   def check_answer(self,u_ans,c_ans):
      if(u_ans==c_ans):
         print("Yay!!You got the correct answer.")
         self.score+=1
      else:
         print("OOps!Sorry,that is wrong.")
      print(f"The Correct answer is {c_ans}")
      print(f"Your Current score is: {self.score}/{self.ques_num}")
   
   

      
