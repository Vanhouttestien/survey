import random
import time
import os

def generate_random_number(): 
    var= random.randint(1, 99)
    print(var)
    time.sleep(20)
    os.system("CLS")


def main():
    generate_random_number()

main()