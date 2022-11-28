import os
import random





def deal():
    hand = []
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def points(hand):
    points=0
    cards = len(hand)
    print(hand)
    for(i=0; i < cards; i++):
        print(hand[i])
    #     if cards[i] < 1 and cards[i] > 11:
    #         print(cards[i]) 
    #     else:
    #         if cards[i] == "J":points =+ 10
    #         if cards[i] == "Q":points =+ 10
    #         if cards[i] == "K":points =+ 10
    #         if cards[i] == "A":
    #             if 21 - points <= 10:
    #                 points =+ 11
    #             else:
    #                 points =+ 1
    # return points


print(points(deal()))
        

    