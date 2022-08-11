import random
import time
import os

def generate_random_number(): 
    """
    Print a random number and make it disappear after 20 seconds
    """
    var= random.randint(1, 99)
    print(var)
    time.sleep(20)
    os.system('clear')

def user_input():
    """
    User can fill the numbers in.
    """
    while True:
        try: 
            print('enter the numbers seperated with a comma')
            print('32, 5, 99, 43')
            x = input('Enter the numbers:')
            guessed_numbers= (x.strip()).split(",")
            guessed_numbers_int = [eval(i) for i in guessed_numbers]  # convert list numbers to list of strings https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
        except NameError:
            print("not a number")
        
    return guessed_numbers_int

        # if validate(guessed_numbers_int):
        #     print("this is valid")
        #     break
        
"""
def validate(values):
    try:
        [int(value) for value in values]
    except ValueError:
        print('Not a number')
"""        
    

def main():
    #generate_random_number()
    user_input()

main()