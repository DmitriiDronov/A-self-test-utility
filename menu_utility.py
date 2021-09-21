from os import listdir
from os.path import isfile, join
from pathlib import Path
from test import Test

class Menu():
    

    def __init__(self):
        self.__path = self.__get_tests_path()
        self.__test_files_with_path = self.__get_test_files()
        self.__menuMap = self.__map_tests_to_number()


    def display(self):
        map = self.__menuMap
        for key in map:
            print(str(key) + '. ' + map[key])


    def ask_for_choice(self):
        choice = input("Enter a nubmer of test you want to study: ")
        self.handle_choice(choice)


    def handle_choice(self, choice):
        choice = int(choice)
        keys = self.__menuMap.keys()

        if choice not in keys:
            print("Invalid choice, try again")
            self.ask_for_choice()
        return self.get_test_by_choice(choice)


    def get_test_by_choice(self, choice):
        test_name = self.__menuMap.get(choice)
        test_path = self.__test_files_with_path.get(test_name)
        return Test(test_path)
    

    def __get_tests_path(self):
        return Path().absolute().joinpath('tests')


    def __get_test_files(self):
        path = self.__path
        files = [file for file in listdir(path) if isfile(join(path, file))]
        
        files_with_path = dict()
        for file in files:
            files_with_path[file] = self.__path.joinpath(file)

        return files_with_path


    def __map_tests_to_number(self):
        map = dict()
        for index, item in enumerate(self.__test_files_with_path):
            key = index + 1
            map[key] = item
        return map