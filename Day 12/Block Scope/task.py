from random import choice, randint

import art
import random

print(art.logo)
Hard = 5
Easy = 10
Number = randint(1,100)
print(Number)

def input_num():
    return int(input("Make a Guess: "))

def game_play():
    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")

def extended_game_play():
    game_play()
    choices: str = input("Choose a difficulty. Type 'easy' or 'hard':")
    if choices == "easy":
        print(f"You have {Easy} attempts remaining to guess the number.")
        return Easy
    elif choices == "hard":
        print(f"You have {Hard} attempts remaining to guess the number.")
        return Hard
    return 0

def loop_logic():
    limit=extended_game_play()
    if limit == 0:
        print("You have entered a wrong entry")
        exit()
    while limit > 0:
        number_entered= input_num()
        if number_entered == Number:
            print(f"You got it! The answer was {number_entered}.")
            break
        elif number_entered > Number:
            print("Too high. \nGuess again.")
        else:
            print("Too low. \nGuess again.")
        limit -= 1
        print(f"You have {limit} attempts remaining to guess the number.")

if __name__== "__main__":
    loop_logic()






