import random
import os

def deal():
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    random.shuffle(deck)
    hand = []
    for i in range(2):
        card = deck.pop()
        if card == 11:card = "J"
        if card == 12:card = "Q"
        if card == 13:card = "K"
        if card == 14:card = "A"
        hand.append(card)
    return hand

def point(hand):
    points=0

    for i in range(len(hand)):
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
    print("Witaj w grze Blackjack")
    print("Zaczynasz z $1000")
    money = 1000
    while money > 0:
        bet = int(input("Ile chcesz obstawić?"))
        if bet > money:
            print("Nie masz tyle pieniędzy")
            bet = int(input("Ile chcesz obstawić?"))
        hand = deal()
        points = point(hand)
        print("Masz", points, "punktów")
        while points < 21:
            choice = input("Czy chcesz dobrać kartę? (t/n)")
            if choice == "t":
                hand = hit(hand)
                points = point(hand)
                print("Masz ", points, "punktów")

            else:
                break
        if points > 21:
            print("Przegrałeś")
            money -= bet
            print("Pozostało ci", money, "$")
        else:
            print("Masz ", points, "punktów")
            dealer = deal()
            dealer_points = point(dealer)
            print("Krupier ma", dealer_points, "punktów")
            if dealer_points > 21:
                print("Wygrałeś")
                money += bet
                print("Pozostało ci", money, "$")
            elif dealer_points > points:
                print("You lose")
                money -= bet
                print("Pozostało ci", money, "$")
            elif dealer_points < points:
                print("You win")
                money += bet
                print("Pozostało ci", money, "$")
            else:
                print("Remis")
                print("Pozostało ci", money, "$")
    print("Koniec gry")
    print("Skończyły ci się pieniądze")

main()
