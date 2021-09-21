import json
from test_question import TestQuestion

class TestParser():


    def __init__(self, test_path):
        self.__test_path = test_path
        self.__question_queue = self.__parse()


    def __parse(self):
        file = open(self.__test_path, encoding='utf-8')
        file_content = json.load(file)
        return self.__get_questions_with_answers(file_content)


    def get_question_queue(self):
        return self.__question_queue


    def __get_questions_with_answers(self, content):
        test_question_list = list()
        
        for question in content['questions']:
            
            question_text = question['question_text']
            answers = question['answers']
            test_question_list.append(TestQuestion(question_text, answers))
        
        return test_question_list