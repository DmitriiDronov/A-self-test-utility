from os import system, name


def clear_scr():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def press_enter_to_continue():
    input("Press enter to continue...")