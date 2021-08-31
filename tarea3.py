from numpy import random
from tabulate import tabulate

def clone_list(lst):
    new_list = []
    for i in range(len(lst)):
        new_list.append(lst[i])
    return(new_list)

def chunks(deck, n): #THIS FUNCTION DIVIDES THE DECK INTO CHUNKS, https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
    for i in range(0, len(deck), n):
        yield(deck[i:i + n])

def turn_cycle(player1_score, player2_score, player_turn, deck): 
    hidden_deck = deck
    print("PLAYER 1 SCORE:", player1_score)
    print("PLAYER 2 SCORE:", player2_score)
    print("--------------==PLAYER", player_turn, "TURN==--------------")
    print()
    return()

def create_deck(card_number):
    new_deck = []
    if card_number == 1:
        columns = 1
    elif card_number == 2:
        columns = 2
    elif card_number == 3:
        columns = 3
    else:
        columns = 4

    for card in range(card_number):
        new_deck.append(card + 1)
        new_deck.append(card + 1)
    random.shuffle(new_deck)
    return(list(chunks(new_deck, columns)))

########################################################################################

card_number = int(input("Welcome to MEMORIZE! Type the number of cards for each player: "))
player1_score, player2_score = 0, 0
player_turn = 1
print("")
print("----------------==NEW GAME==-----------------")
new_deck = create_deck(card_number)

for i in range(len(new_deck)):
    new_deck[i].insert(0,i)

new_deck_hidden = clone_list(new_deck)

for i in range(len(new_deck_hidden)):
    for j in range(len(new_deck_hidden[i])):
        new_deck_hidden[i][j] = " ҉"

print(new_deck)
print(new_deck_hidden)

print(tabulate(new_deck,[0,1,2,3]))

