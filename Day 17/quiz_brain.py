class QuizBrain:

    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0


    def is_question_available(self):
        if len(self.question_list) != self.question_number:
            return True
        return False

    def check_answer(self,u_ans, a_ans):
        if u_ans.lower() == a_ans.lower():
            print("You got it right !")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {a_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        self.check_answer(user_answer,current_question.answer)