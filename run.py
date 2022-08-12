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


def instructions():
    custom_fig = Figlet(font='computer')    # code from https://www.devdungeon.com/content/create-ascii-art-text-banners-python
    print(custom_fig.renderText('Nummory'))
    print("Can you remember all the numbers?")
    print("The goal of the game is to try to remember as much numbers as you can.")
    print("The order of the numbers doesn't mather.")
    print('Enter the numbers seperated with whitespace')
    print(Fore.GREEN + 'For example: 32 5 99 43')
    print(Fore.WHITE + "Try to repeat all the numbers you see and level up.")
    print("How far can you get?")
    print()
    print('Enter a nickname and press ENTER')
    print(Fore.BLUE+'nickname:',end="")
    global nickname
    while True: 
        try:    
            nickname = input()
            1/len(nickname)
            print(Fore.GREEN + f'Welcome {nickname}')
            time.sleep(2)

            os.system('clear')
            return nickname
        except ZeroDivisionError:
            print(Fore.RED + 'Please enter a nickname.')
    
def generate_random_number(): 
    """
    Print a random number and make it disappear after 20 seconds
    """
    global level
    global ls
    for i in range(level): 
        var = random.randint(1, 99)
        ls.append(var)
    print(Style.RESET_ALL)
    print("Wait for 20 seconds or press any key")
    print(f'level: {level}')
    print()
    print(Fore.BLUE + 'Numbers:')
    print(*ls, sep = ',')
    key = getkey()
    if  key == key:
        os.system('clear')
    else:
        time.sleep(20) 
        os.system('clear')
    return level, ls

def user_input():
    """
    User can fill the numbers in.
    """
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
    print(Fore.RED + "You gave the wrong answer")
    print(f'the right answer was {ls}')
    print(f'You got till level {level}')
    score_update()

def score_update():
    """
    Prints level and nickname to google sheets and prints the current top 10
    """
    global nickname
    global level
    score= SHEET.insert_row([nickname,level], index=2)
    SHEET.sort((2,'des'))
    highscore_list=SHEET.get_values('A2:B11')       #code for making a table: https://www.statology.org/create-table-in-python/
    col_names = ["NAME", "LEVEL"]  
    print(Fore.LIGHTMAGENTA_EX + tabulate(highscore_list, headers=col_names))

def main():
    generate_random_number()
    user_input()
    check_correct()
   
def startgame(): 
     instructions()
     main()

startgame()