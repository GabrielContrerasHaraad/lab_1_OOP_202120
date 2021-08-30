from numpy import random
import math

def turn_cycle(player1_score, player2_score, player_turn, deck): 
    hidden_deck = deck
    print("PLAYER 1 SCORE:", player1_score)
    print("PLAYER 2 SCORE:", player2_score)
    print("--------------==PLAYER", player_turn, "TURN==--------------")
    print()
    return()

def create_deck(card_number):
    new_deck = []
    table = []

    if card_number == 1:
        columns = 2
    elif card_number == 2:
        columns = 4
    elif card_number == 3:
        columns = 6
    elif card_number == 4:
        columns = 8
    else:
        columns = 8

    if (card_number*2) % columns == 0:
        carry = 0
    else:
        carry = 1

    for card in range(card_number):
        new_deck.append(card + 1)
        new_deck.append(card + 1)
    random.shuffle(new_deck)

    for i in range(columns + 1):
        table.append([])

    table[0] = " ҉"
    for i in range(columns + carry):
        for j in range(round(card_number / columns)):
            table[i].append(new_deck[i])

    print(table)
    return(new_deck)

card_number = int(input("Welcome to MEMORIZE! Type the number of cards for each player: "))
player1_score, player2_score = 0, 0
player_turn = 1
print("")
print("----------------==NEW GAME==-----------------")
new_deck = create_deck(card_number)
print(new_deck)