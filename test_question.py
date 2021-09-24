class TestQuestion():


    def __init__(self, question_text, answers):
        self.question_text = question_text
        self.answers = answers


    def __str__(self):
        question = str(self.question_text + '\n')
        for index, answer in enumerate(self.answers):
            question = question + str(index) + '. ' + answer['answer_text'] + '\n'
        return question
    
    def print_with_answer(self) -> None:
        question = str(self.question_text + '\n').center(50)
        for index, answer in enumerate(self.answers):
            question = question + str(index) + '. ' + answer['answer_text'] + ' - ' + str(answer['value']) + '\n'
        print(question)


    def get_all_answers(self) -> list:
        return self.answers


    def get_correct_answers(self) -> list:
        correct_answers = []
        for answer in self.answers:
            if self.__is_answer_correct(answer):
                correct_answers.append(answer)
        return correct_answers


    def __is_answer_correct(self, answer) -> bool:
        if (not answer):
            return False
            
        if (answer['value'] == 1):
            return True
        return False