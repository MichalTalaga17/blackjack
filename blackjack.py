import os
import random


def deal():
    hand = []
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            card = "J"
        if card == 12:
            card = "Q"
        if card == 13:
            card = "K"
        if card == 14:
            card = "A"
        hand.append(card)
    return hand


def points(hand):
    points = 0
    cards = len(hand)
    print(hand)
    for i in range(cards):
        if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
            points += 10
        elif hand[i] == "A":
            if points <= 10:
                points += 11
            else:
                points += 1
        else:
            points += hand[i]
    return points


def hit(hand):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand


def main():
    os.system("cls")
    print("Welcome to Blackjack")
    print("You start with 1000 points")
    points = 1000
    while points > 0:
        os.system("cls")
        print("You have " + str(points) + " points")
        bet = int(input("How much do you want to bet? "))
        if bet > points:
            print("You don't have that many points")
            input("Press enter to continue")
            continue
        hand = deal()
        points = points - bet
        print("Your hand is " + str(hand))
        print("Your hand is worth " + str(points(hand)))
        while points(hand) < 21:
            choice = input("Do you want to hit or stay? ")
            if choice == "hit":
                hand = hit(hand)
                print("Your hand is " + str(hand))
                print("Your hand is worth " + str(points(hand)))
            elif choice == "stay":
                break
            else:
                print("Please enter hit or stay")
                input("Press enter to continue")
                continue
        if points(hand) == 21:
            print("You got 21!")
            points = points + bet*2
            input("Press enter to continue")
        elif points(hand) > 21:
            print("You busted!")
            input("Press enter to continue")
        else:
            print("You stayed at " + str(points(hand)))
            input("Press enter to continue")
    print("You are out of points")
    input("Press enter to continue")


main()
