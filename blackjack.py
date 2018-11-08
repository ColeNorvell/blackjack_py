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
        self.card = []

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

print("game working?")
