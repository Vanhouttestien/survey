import random
import time
import os
import sys
from getkey import getkey, keys
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from colorama import Fore, Style
from pyfiglet import Figlet
from threading import Timer

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('nummemory').worksheet('score')

# global variables
LEVEL = 1
NUMBERS = []
INPUT_NUMBERS = []
NICKNAME = ""


def start_menu():
    """
    start menu: Figlet with Nummmory
    and option to choose to start the game or read the instructions
    code for figlet from:
    www.devdungeon.com/content/create-ascii-art-text-banners-python
    """
    custom_fig = Figlet(font='computer')
    print(custom_fig.renderText('Nummory'))
    print('')
    print('Press i to see the instructions')
    print('Press s to start the game')
    key = getkey()
    while True:
        if key == keys.I:
            instructions()
            break
        elif key == keys.S:
            os.system('clear')
            break
        else:
            os.system('clear')
            startgame()


def typingPrint(text):
    """
    typing effect
    code from www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)


def instructions():
    """
    prints the instruction with typing effect
    """
    os.system('clear')
    typingPrint("""
    Can you remember all the numbers?
    The goal of the game is to try to remember as many numbers as you can.
    Game:
    1. You get to see a list of numbers
    2. you have 20 seconds to try and memorize the numbers
    3. try to type all numbers
       -Enter the numbers seperated with whitespace
       -the order is not important
       -For example: 32 5 99 43 is the same as 5 99 32 43
    4. If you have all the numbers correct you
    go up one level and get a extra number.

    How far can you get?
    Can you break the highscore?
    """)
    print()


def nickname_validation():
    """
    functions asks user to input a nickname
    and verifies that the input is not empty.
    """
    global NICKNAME
    print('Enter a nickname and press ENTER to get started')
    print(Fore.BLUE+'nickname:', end="")
    while True:
        NICKNAME = input("\n")
        if len(NICKNAME) == 0:
            print(Fore.RED + 'Please enter a nickname.')
            continue
        print(Fore.MAGENTA + f'Welcome {NICKNAME}')
        time.sleep(2)
        os.system('clear')
        return NICKNAME


def times_up():
    """
    When 20 seconds are over this clears the random numbers.
    """
    os.system('clear')
    print("Your time is up!")
    print("Press a key to continue.")


def generate_random_number():
    """
    Print a random number and make it disappear after 20 seconds
    or after a keypress.
    """
    global LEVEL
    global NUMBERS
    os.system('clear')
    for i in range(LEVEL):
        var = random.randint(1, 99)
        NUMBERS.append(var)
    print(Style.RESET_ALL)
    print("Wait for 20 seconds or press any key")
    print(f'level: {LEVEL}')
    print()
    print(Style.BRIGHT+'Numbers:')
    print()
    print(*NUMBERS, sep='          ')
    my_timer = Timer(20, times_up)
    my_timer.start()
    key = getkey()
    my_timer.cancel()
    os.system('clear')
    return LEVEL, NUMBERS


def user_input():
    """
    User can fill the numbers in.
    The input get's validated.
    It should be a number seperated by whitespaces.
    """
    os.system('clear')
    global INPUT_NUMBERS
    while True:
        try:
            print(Style.RESET_ALL)
            print('Have you remembered them all?')
            print()
            print()
            print(Fore.BLUE+'Enter the numbers:', end="")
            x = input("\n")
            guessed_numbers = (x.strip()).split(" ")
            """convert list numbers to list of strings
            www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
            """
            guessed_numbers_int = [eval(i) for i in guessed_numbers]
            INPUT_NUMBERS = guessed_numbers_int
            return INPUT_NUMBERS
        except NameError:
            print(Fore.RED + "You can only use numbers")
        except SyntaxError:
            print(Fore.RED + "did you use the right format?")
            print("you can only use numbers)
            print("and they should be separated by a whitespace")
            print('ex. 32 5 99 43')
    return guessed_numbers_int, NUMBERS


def check_correct():
    """
    Checks if the input number is the same as the printed number.
    When it is the same you go a level up and the screen gets cleared.
    otherwise you go to endgame function.
    """
    global LEVEL
    global INPUT_NUMBERS
    global NUMBERS
    NUMBERS.sort()
    INPUT_NUMBERS.sort()
    if INPUT_NUMBERS == NUMBERS:
        NUMBERS = []
        LEVEL += 1
        os.system('clear')
        main()
    else:
        return LEVEL, NUMBERS


def end_game():
    """
    After a wrong answer tells the user
    what they got wrong and to with level they got.
    """
    global LEVEL
    print(Fore.RED + "You gave the wrong answer")
    print(f'the right answer was {NUMBERS}')
    print(f'You got till level {LEVEL}')
    score_update()
    print()
    print(f'level is {LEVEL}')


def score_update():
    """
    Prints level and nickname to google sheets and prints the current top 10
    """
    global NICKNAME
    global LEVEL
    SHEET.insert_row([NICKNAME, LEVEL], index=2)
    SHEET.sort((2, 'des'))
    # code for making a table: www.statology.org/create-table-in-python/
    highscore_list = SHEET.get_values('A2:B11')
    print(Fore.LIGHTMAGENTA_EX + "Highscore:")
    col_names = ["NAME", "LEVEL"]
    print(Fore.LIGHTMAGENTA_EX + tabulate(highscore_list, headers=col_names))


def resetlevel():
    global LEVEL
    global NUMBERS
    LEVEL = 1
    NUMBERS = []


def restart():
    """
    Give the user the oppurtunity to restart.
    if restart reset game.
    """
    print('Would you like to try again?')
    resetlevel()
    answer = None
    """
    code from
    https://tutorial.eyehunts.com/
    """
    while answer not in ("yes", "no"):
        answer = input("Enter yes or no: ")
        if answer.lower() == "yes":
            main()
        elif answer.lower() == "no":
            sys.exit(0)
        else:
            print("Please enter yes or no.")


def startgame():
    start_menu()
    nickname_validation()
    main()


def main():
    generate_random_number()
    user_input()
    check_correct()
    end_game()
    restart()


startgame()
