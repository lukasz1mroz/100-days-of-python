class QuizBrain:

    def __init__(self, question_list):
        self.question = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        curr_question = self.question_list[self.question]
        self.question += 1
        response = input(f'Q.{self.question}: {curr_question.text} (True/False): ')
        self.check_answer(response, curr_question.answer)

    def still_has_questions(self):
        return self.question < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"Correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question}.")






