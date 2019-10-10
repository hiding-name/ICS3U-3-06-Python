#!/usr/bin/env python3

# Created by: Matsuru Hoshi
# Created on: Oct 2019
# This is program makes user ghess numbers

import random


def main():
    # funciton makes user guess nimber

    # variable
    number = random.randint(1, 3)

    # Welcome statement
    print("Welcome, this is the NUMBER GUESSER.")
    input("Press Enter to continue.")

    # process
    try:
        # input
        guess = int(input("Guess the number: "))
        if guess == number:
            # output
            print("Good job, you got it.")
        else:
            print("You got it wrong.")
    except Exception:
        print("Invalid input.")


if __name__ == "__main__":
    main()
