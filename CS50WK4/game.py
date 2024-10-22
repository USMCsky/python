# In a file called game.py, implement a program that:
#
# Prompts the user for a level,
# . If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and
# , inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer,
# the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.
# Hints
# Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.
import random
import sys

def get_pos_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
        except ValueError:
            pass
        print("Level: ")

def main():
    level = get_pos_int("Level: ")
    answer = random.randint(1, level)

    while True:
        guess = get_pos_int("Guess: ")
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit()

main()
