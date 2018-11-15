import random
import sys

class Card:
    def __init__(self, suit, value, face, ace):
        self.suit = suit
        self.value = value
        self.face = face
        self.ace = ace


class Deck:
    def __init__(self):
        # Create a List to Hold all of the Cards in our Deck
        self.card = []
        # Fill self.card List With Instances of the Class "Card" Starting with Spades
        self.card.append(Card("Spades", 2, False, False))
        self.card.append(Card("Spades", 3, False, False))
        self.card.append(Card("Spades", 4, False, False))
        self.card.append(Card("Spades", 5, False, False))
        self.card.append(Card("Spades", 6, False, False))
        self.card.append(Card("Spades", 7, False, False))
        self.card.append(Card("Spades", 8, False, False))
        self.card.append(Card("Spades", 9, False, False))
        self.card.append(Card("Spades", 10, False, False))
        # Create Hearts
        self.card.append(Card("Hearts", 2, False, False))
        self.card.append(Card("Hearts", 3, False, False))
        self.card.append(Card("Hearts", 4, False, False))
        self.card.append(Card("Hearts", 5, False, False))
        self.card.append(Card("Hearts", 6, False, False))
        self.card.append(Card("Hearts", 7, False, False))
        self.card.append(Card("Hearts", 8, False, False))
        self.card.append(Card("Hearts", 9, False, False))
        self.card.append(Card("Hearts", 10, False, False))
        # Create Clubs
        self.card.append(Card("Clubs", 2, False, False))
        self.card.append(Card("Clubs", 3, False, False))
        self.card.append(Card("Clubs", 4, False, False))
        self.card.append(Card("Clubs", 5, False, False))
        self.card.append(Card("Clubs", 6, False, False))
        self.card.append(Card("Clubs", 7, False, False))
        self.card.append(Card("Clubs", 8, False, False))
        self.card.append(Card("Clubs", 9, False, False))
        self.card.append(Card("Clubs", 10, False, False))
        # Create Diamonds
        self.card.append(Card("Diamonds", 2, False, False))
        self.card.append(Card("Diamonds", 3, False, False))
        self.card.append(Card("Diamonds", 4, False, False))
        self.card.append(Card("Diamonds", 5, False, False))
        self.card.append(Card("Diamonds", 6, False, False))
        self.card.append(Card("Diamonds", 7, False, False))
        self.card.append(Card("Diamonds", 8, False, False))
        self.card.append(Card("Diamonds", 9, False, False))
        self.card.append(Card("Diamonds", 10, False, False))
        # Create Face Cards and Ace for Suit Spades
        self.card.append(Card("Spades", 10, "King", False))
        self.card.append(Card("Spades", 10, "Queen", False))
        self.card.append(Card("Spades", 10, "Jack", False))
        self.card.append(Card("Spades", 11, False, True))
        # Create Face Cards and Ace for Suit Hearts
        self.card.append(Card("Hearts", 10, "King", False))
        self.card.append(Card("Hearts", 10, "Queen", False))
        self.card.append(Card("Hearts", 10, "Jack", False))
        self.card.append(Card("Hearts", 11, False, True))
        # Create Face Cards and Ace for Suit Clubs
        self.card.append(Card("Clubs", 10, "King", False))
        self.card.append(Card("Clubs", 10, "Queen", False))
        self.card.append(Card("Clubs", 10, "Jack", False))
        self.card.append(Card("Clubs", 11, False, True))
        # Create Face Cards and Ace for Suit Diamonds
        self.card.append(Card("Diamonds", 10, "King", False))
        self.card.append(Card("Diamonds", 10, "Queen", False))
        self.card.append(Card("Diamonds", 10, "Jack", False))
        self.card.append(Card("Diamonds", 11, False, True))

    def shuffle(self):
        # print(self.card[25].suit)
        placeholder = self.card[card_one]

class Hand:
    def __init__(self):
        self.card = []

class PokerPlayer:
    def __init__(self, dealer):
        self.dealer = dealer  # dealer is a boolean value
        self.hand = Hand()

player = PokerPlayer(False)
dealer = PokerPlayer(True)
deck = Deck()

print(deck.card[25].suit)
print(deck.card[25].value)
print(deck.card[25].face)
print(deck.card[25].ace)

deck.shuffle()
