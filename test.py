from test_parser import TestParser
from test_question import TestQuestion
from utility import clear_scr
import time


class Test():


    def __init__(self, test_path):
        self.__test_parser = TestParser(test_path) 
        self.question_queue = self.__test_parser.get_question_queue()
        self.question_queue.reverse()

        self.answered_correctly = 0
        self.answered_incorrectly = 0
        self.question_number = 0
        
        self.start()


    def start(self):
        self.start_time = time.time()
        while (self.question_queue):
            # clear_scr()
            self.question_number = self.question_number + 1
            self.__print_statistics()

            question = self.question_queue.pop()
            all_answers = question.get_all_answers()
            correct_answers = question.get_correct_answers()

            print(question)

            number_of_correct_answers = len(correct_answers)
            print('Enter {} answer(s)'.format(number_of_correct_answers))

            user_answers = []
            for i in range(number_of_correct_answers):
                answer_index = int(input('Enter {} answer: '.format(i)))
                user_answers.append(all_answers[answer_index])
                print(user_answers)

            if (self.__check_answers(user_answers)):
                print('Correct!')
            else:
                print('Correct answers: ')
                for answer in correct_answers:
                    print(answer)
            

        self.__print_summary()    
    
    
    def __check_answers(self, user_answers):
        for user_answer in user_answers:
            for key in user_answer.keys():
                if user_answer[key] == 0:
                    return False
        return True


    def __print_statistics(self):
        print(str(self.question_number).center(50))
        answered_incorrectly = 'Answered incorectly {}'.format(self.answered_incorrectly).ljust(50)
        answered_correctly = 'Answered correctly {}'.format(self.answered_correctly).rjust(50)
        print(answered_incorrectly + ' ' + answered_correctly)


    def __print_summary(self):
        pass