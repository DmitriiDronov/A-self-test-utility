from test_parser import TestParser
from test_question import TestQuestion
from utility import Utility
from datetime import datetime
import time


class Test():


    def __init__(self, test_path):
        self.__test_parser = TestParser(test_path) 
        self.question_queue = self.__test_parser.get_question_queue()
        self.question_queue.reverse()
        self.total_questions = len(self.question_queue)

        self.questions_answered_incorectly = list()

        self.answered_correctly = 0
        self.answered_incorrectly = 0
        self.question_number = 0
        
        self.start()


    def start(self):
        self.start_time = time.time()
        while (self.question_queue):
            Utility.clear_scr()
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

            if (self.__check_answers(user_answers)):
                self.answered_correctly = self.answered_correctly + 1
                print('Correct!')
            else:
                self.answered_incorrectly = self.answered_incorrectly + 1
                self.questions_answered_incorectly.append(question)
                print('Correct answers: ')
                for answer in correct_answers:
                    for key in answer.keys():
                        if key == 'answer_text':
                            print(answer[key])
            
            Utility.press_enter_to_continue()
            

        self.__print_summary()    
    
    
    def __check_answers(self, user_answers):
        for user_answer in user_answers:
            for key in user_answer.keys():
                if user_answer[key] == 0:
                    return False
        return True


    def __print_statistics(self):
        print("Question {} of {}".format(self.question_number, self.total_questions))

        answered_correctly = 'Answered correctly {}'.format(self.answered_correctly)
        print(answered_correctly)
        answered_incorrectly = 'Answered incorectly {}'.format(self.answered_incorrectly)
        print(answered_incorrectly)

        success_persentage = self.__get_success_percentage()
        print("Success: {}%".format(success_persentage))

        time_now = time.time()
        time_passed = datetime.fromtimestamp(time_now - self.start_time)
        print("Time passed {}".format(time_passed.strftime("%M:%S")))
        print('*' * 50)


    def __get_success_percentage(self):
        success_percentage = (100 * self.answered_correctly) / self.total_questions
        return success_percentage


    def __print_summary(self):
        Utility.clear_scr()
        print("Total correct answers: {}\nTotal incorrect answers: {}".format(self.answered_correctly, self.answered_incorrectly))
        print("Your success: {}".format(self.__get_success_percentage()))
    
        choice = ''
        while(choice != 'Y' or choice != 'N'):
            choice = input("Review incorrect answers? (Y/n): ")
            choice = choice.upper()
            if choice == 'Y':
                self.__print_incorrect_questions()
                break
            elif choice == 'N':
                break;
            else:
                print('Undefined choice')
    
    def __print_incorrect_questions(self):
        for incorrect_question in self.questions_answered_incorectly:
            incorrect_question.print_with_answer()