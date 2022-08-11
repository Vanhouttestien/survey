import random
import time
import os

level=1

def generate_random_number(): 
    """
    Print a random number and make it disappear after 20 seconds
    """
    global level
    ls=[]
    for i in range(level): 
        var = random.randint(1, 99)
        ls.append(var)
    print(ls)
    level +=1
    print(level)
    return level
    time.sleep(2)
    os.system('clear')

# def user_input():
#     """
#     User can fill the numbers in.
#     """
#     while True:
#         try: 
#             print('enter the numbers seperated with a comma')
#             print('32, 5, 99, 43')
#             x = input('Enter the numbers:')
#             guessed_numbers= (x.strip()).split(",")
#             guessed_numbers_int = [eval(i) for i in guessed_numbers]  # convert list numbers to list of strings https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
#         except NameError:
#             print("not a number")
        
#     return guessed_numbers_int

def check_correct():
    global level
    if level<10:
         main()
    else: 
        print("stop")

def correct_add_number():
    generate_random_number()

def main():
    generate_random_number()
    #user_input()
    check_correct()

main()