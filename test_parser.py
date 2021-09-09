import json

class TestParser():


    def __init__(self, test_path):
        self.__test_path = test_path
        self.test_questions_with_answers = self.__parse()


    def __parse(self):
        file = open(self.__test_path, encoding='utf-8')
        content = json.load(file)
        print(content)