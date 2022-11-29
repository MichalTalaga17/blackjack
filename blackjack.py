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
    for i in range(cards):
        if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
            points += 10
        elif hand[i] == "A":
            if points >= 11:
                points += 1
            else:
                points += 11
        else:
            points += hand[i]
    return points

def hit(hand):
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(deck)
    card = deck.pop()
    if card == 11:card = "J"
    if card == 12:card = "Q"
    if card == 13:card = "K"
    if card == 14:card = "A"
    hand.append(card)
    return hand

def main():

    os.system('cls')
    print("Welcome to Blackjack")
    print("You have $1000 to start with")
    money = 1000
    while money > 0:
        bet = int(input("How much would you like to bet?"))
        if bet > money:
            print("You don't have that much money")
            bet = int(input("How much would you like to bet?"))
        hand = deal()
        points = points(hand)
        print("You have", points, "points")
        while points < 21:
            choice = input("Hit or Stay?")
            if choice == "Hit":
                hand = hit(hand)
                points = points(hand)
                print("You have", points, "points")
            else:
                break
        if points > 21:
            print("You busted")
            money -= bet
            print("You have", money, "left")
        else:
            print("You have", points, "points")
            print("The dealer has", dealer, "points")
            if points > dealer:
                print("You win!")
                money += bet
                print("You have", money, "left")
            elif points == dealer:
                print("It's a tie")
                print("You have", money, "left")
            else:
                print("You lose")
                money -= bet
                print("You have", money, "left")
    print("You have no more money")
    print("Thanks for playing")

main()

        

    