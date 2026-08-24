class QuizBrain:

    def __init__(self,q_list):
        self.question_no = 0
        self.score = 0
        self.question_list = q_list

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        answer = input(f"Q.{self.question_no}: {current_question.text} (True/False): ")
        self.check_answer(answer, current_question.answer)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("You got it right!")
            print(f"The correct answer was: {correct_answer}")
            self.score += 1
            print(f"Your current score is: {self.score}/{self.question_no}")
            print("\n")
        else:
            print("You got it wrong!")
            print(f"The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_no}")
            print("\n")
