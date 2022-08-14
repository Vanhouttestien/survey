import random
import time
import os
from getkey import getkey, keys
import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate
from colorama import init
from colorama import Fore, Back, Style
from pyfiglet import Figlet
import sys
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

#global variables
level=1
ls=[]
input_number=[]
nickname= ""

def start_menu():
    custom_fig = Figlet(font='computer')    # code from https://www.devdungeon.com/content/create-ascii-art-text-banners-python
    print(custom_fig.renderText('                            Nummory'))
    print('')
    print('Press i to see the instructions')
    print('Press s to start the game')
    key = getkey()
    if key == keys.I:
        instructions()
    elif key == keys.S:
        os.system('clear')

def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

def instructions():
    os.system('clear')
    typingPrint("""
    Can you remember all the numbers?
    The goal of the game is to try to remember as much numbers as you can.
    Game: 
    1. You get to see a list of numbers 
    2. you have 20 seconds to try and memorize the numbers
    3. try to type all numbers
       -Enter the numbers seperated with whitespace
       -the order is not important 
       -For example: 32 5 99 43 is the same as 5 99 32 43
    4. If you have all the numbers correct you go a level up and get a number more. 
    
    How far can you get?
    Can you break the highscore? 
    """)

    print()
    
def nickname_val():
    """
    functions asks user to input a nickname and checks if the string is not empty
    """
    global nickname
    print('Enter a nickname and press ENTER to get started')
    print(Fore.BLUE+'nickname:',end="")
    while True: 
        try:    
            nickname = input()
            1/len(nickname)
            print(Fore.MAGENTA + f'Welcome {nickname}')
            time.sleep(2)
            os.system('clear')
            return nickname    
        except ZeroDivisionError:
            print(Fore.RED + 'Please enter a nickname.')

def times_up():
    os.system('clear')
    print("Your time is up!")
    print("Press a key to continue.")

def generate_random_number(): 
    """
    Print a random number and make it disappear after 20 seconds
    """
    global level
    global ls
    timer = 5
    os.system('clear')
    for i in range(level): 
        var = random.randint(1, 99)
        ls.append(var)
    print(Style.RESET_ALL)
    print("Wait for 20 seconds or press any key")
    print(f'level: {level}')
    print()
    print(Style.BRIGHT+'Numbers:')
    print()
    print(*ls, sep = '    ')
    MyTimer = Timer(20, times_up)
    MyTimer.start()
    key = getkey()
    if key == key:
        MyTimer.cancel()
    os.system('clear')
    return level, ls

def user_input():
    """
    User can fill the numbers in.
    """
    os.system('clear')
    global input_number
    while True:
        try: 
            print(Style.RESET_ALL)
            print('Have you remembered them all?')
            print()
            print()
            print(Fore.BLUE+'Enter the numbers:',end="")
            x = input()
            guessed_numbers = (x.strip()).split(" ")
            guessed_numbers_int = [eval(i) for i in guessed_numbers]  # convert list numbers to list of strings https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
            input_number = guessed_numbers_int
            return input_number
        except NameError:
            print(Fore.RED + "You didn't type a number")
            print(Fore.RED +'seperate the numbers by a whitespace: ex. 32 5 99 43')
        except SyntaxError:
            print(Fore.RED + "did you use the right format?")
            print(Fore.RED + "you can only use numbers and they should be seperated by a whitespace")
            print(Fore.RED +' ex. 32 5 99 43')
        
    return guessed_numbers_int, ls

def check_correct():
    """
    Checks if the input number is the same as the printed number. 
    When it is the same you go a level up and the screen gets cleared. 
    otherwise you go to endgame function.
    """
    global level
    global input_number
    global ls
    ls.sort()
    input_number.sort()
    if input_number == ls: 
        ls=[]
        level += 1
        os.system('clear')
        main()
    else: 
        end_game()
        

def end_game():
    global level
    os.system('clear')
    print(Fore.RED + "You gave the wrong answer")
    print(f'the right answer was {ls}')
    print(f'You got till level {level}')
    score_update()
    print()
    print(f'level is {level}')
    restart()


def restart():
    print('Would you like to try again?')
    print('Yes: press y')
    print('No: press n')
    key = getkey()
    def resetlevel():
        global level
        global ls
        level=1
        ls=[]
        return level, ls
    resetlevel()
    if key == keys.Y:
        main()
    elif key == keys.N:
        sys.exit(0)
    


def score_update():
    """
    Prints level and nickname to google sheets and prints the current top 10
    """
    global nickname
    global level
    score= SHEET.insert_row([nickname,level], index=2)
    SHEET.sort((2,'des'))
    highscore_list=SHEET.get_values('A2:B11')       #code for making a table: https://www.statology.org/create-table-in-python/
    print("highscore:")
    col_names = ["NAME", "LEVEL"]  
    print(Fore.LIGHTMAGENTA_EX + tabulate(highscore_list, headers=col_names))
    # to ADD: print possition and if in top 10 add congrats message
    # restart possibility 



def main():
    generate_random_number()
    user_input()
    check_correct()
    
   
def startgame(): 
     start_menu()
     nickname_val()
     main()

startgame()