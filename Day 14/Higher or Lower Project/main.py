import random
from random import randint

import art
import game_data

def first_play():
    randomvalue = randint(0,len(game_data.data)-1)
    print(f"Compare A: {game_data.data[randomvalue]['name']} a {game_data.data[randomvalue]['description']}, from {game_data.data[randomvalue]['country']}")
    print(art.vs)
    while True:
        randomvalueb = randint(0,len(game_data.data)-1)
        if randomvalueb != randomvalue:
            print(f"Compare B: {game_data.data[randomvalueb]['name']} a {game_data.data[randomvalueb]['description']}, from {game_data.data[randomvalueb]['country']}")
            break
        else:
            continue
    return randomvalue, randomvalueb


def score_compare(indexA, indexB, choice):
    follower_count1 = int(game_data.data[indexA]['follower_count'])
    follower_count2 = int(game_data.data[indexB]['follower_count'])
    if choice == 'a':
        if follower_count1 > follower_count2:
            return True
    if choice == 'b':
        if follower_count1 < follower_count2:
            return True
    return False


if __name__== "__main__":
    Score=0
    while True:
        print(art.logo)
        if Score != 0:
            print(f"You're right, Current Score: {Score}")
        index1, index2 = first_play()
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        flag= score_compare(index1,index2,choice)
        if flag == False:
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, That's Wrong. Final Score: {Score}")
            break
        elif flag == True:
            Score += 1
            print("\n" * 20)






