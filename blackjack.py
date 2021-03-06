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
        self.top_card = 0
        for i in range(1000):
            firstRandomCardIndex = random.randint(0,51)
            secondRandomCardIndex = random.randint(0,51)
            placeholder = self.card[firstRandomCardIndex]
            self.card[firstRandomCardIndex] = self.card[secondRandomCardIndex]
            self.card[secondRandomCardIndex] = placeholder

    def deal(self):
        return self.card[self.top_card - 1]
        self.top_card = self.top_card + 1

class PokerPlayer:
    def __init__(self, dealer):
        self.dealer = dealer  # dealer is a boolean value
        self.hand = []
        self.number_of_cards_held = 0

player = PokerPlayer(False)
dealer = PokerPlayer(True)
deck = Deck()

deck.shuffle()

player.hand.append(deck.deal())
dealer.hand.append(deck.deal())
player.hand.append(deck.deal())
dealer.hand.append(deck.deal())

print("Dealers First Card: " + dealer.hand[0].suit)
print("Dealers Second Card: " + dealer.hand[1].suit)
print("Players First Card: " + player.hand[0].suit)
print("Players Second Card: " + player.hand[1].suit)
