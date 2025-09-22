class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def show_question(self):
        print(self.text, self.answer)