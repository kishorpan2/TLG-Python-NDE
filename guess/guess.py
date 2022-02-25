#!/usr/bin/env python3
"""Number guessing game!"""

import random
count =0
def main():
    num= random.randint(1,100)

    while True && count <= 5:
        guess= int(input("Guess a number between 1 and 100"))
        count = count+1
        if guess > num:
            print("Too high!")

        elif guess < num:
            print("Too low!")

        else:
            print("Correct!")
            break

main()
