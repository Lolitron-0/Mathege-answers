from color import *
import keyboard
import os
import ctypes

def getUrlChoice():
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
    selected = 0
    options = [(1, 7), (2, 9), (3, 5), (4, 183), (5, 6), (6, 10), (7, 8), (8, 11), (9, 12), (10, 184), (11, 13)]
    
    while True:
        os.system('cls')
        print(Style.BOLD + Style.UNDERLINE + Fore.CYAN + 'MATHEGE ANSWERS')
        print()
        print(Style.RESETALL + Fore.WHITE + 'Выберите номер задания: ')
        for i in range(len(options)):
            option = options[i]
            print((Fore.CYAN if selected == i else Fore.WHITE) + str(option[0]))

        print(Style.RESETALL)

        key = keyboard.read_hotkey(False)

        if key == 'up' and selected > 0:
            selected -= 1
        elif key == 'down' and selected < len(options) - 1:
            selected += 1
        elif key == 'enter':
            os.system('cls')
            return 'https://prof.mathege.ru/prototypes/?position='+str(options[selected][1])+'&filter=&limit=1000'
