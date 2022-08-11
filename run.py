import random
import time
import os
from getkey import getkey, keys

level=1
ls=[]
input_number=[]
def instructions():
    print("Can you remember all the numbers?")
    print("The goal of the game is to try to remember as much numbers as you can.")
    print("The order of the numbers doesn't mather.")
    print('enter the numbers seperated with a comma')
    print(' for example: 32, 5, 99, 43')
    print("try to repeat the numbers you see and level up.")
    print("How far can you get?")
    print()
    print('Enter a nickname:')
    nickname = input()
    print()
    print("Press Enter to get started")
    key = getkey()
    if key == keys.ENTER:
        print("upressed enter")



def generate_random_number(): 
    """
    Print a random number and make it disappear after 20 seconds
    """
    global level
    global ls
    for i in range(level): 
        var = random.randint(1, 99)
        ls.append(var)
    print(ls)
    print(f'level: {level}')
    key = getkey()
    if  key == keys.ENTER:
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
            print('enter the numbers seperated with a comma')
            print(' ex. 32, 5, 99, 43')
            x = input('Enter the numbers:')
            guessed_numbers= (x.strip()).split(",")
            guessed_numbers_int = [eval(i) for i in guessed_numbers]  # convert list numbers to list of strings https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
            input_number=guessed_numbers_int
            return input_number
        except NameError:
            print("not a number")
        except SyntaxError:
            print("did you use the right format?")
            print(' ex. 32, 5, 99, 43')
        
    return guessed_numbers_int, ls

def check_correct():
    global level
    global input_number
    global ls
    ls.sort()
    input_number.sort()
    if input_number == ls: 
        ls=[]
        level +=1
        main()
    else: 
        end_game()
        

def end_game():
    print("stop")

def main():
    generate_random_number()
    user_input()
    check_correct()
   
def startgame(): 
     instructions()
     main()

startgame()