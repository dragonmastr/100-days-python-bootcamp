import random

import art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 0 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(art.logo + "\n")
    user = []
    computer = []
    user_score = -1
    computer_score = -1
    for i in range(2):
        user.append(deal_card())
        computer.append(deal_card())
    is_game_over = False
    while not is_game_over:
        user_score = calculate_score(user)
        computer_score = calculate_score(computer)
        print(f"Your cards: {user}, current score: {user_score}")
        print(f"Computer's first card: {computer[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user.append(deal_card())
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    print(compare(user_score, computer_score))

flag = 'y'
while flag=='y':
    flag = input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower()
    if flag == "n":
        exit()
    else:
        play_game()


