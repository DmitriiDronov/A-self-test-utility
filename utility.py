from os import system, name

class Utility:

    
    @staticmethod
    def clear_scr():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')


    @staticmethod
    def press_enter_to_continue():
        input("Press enter to continue...")