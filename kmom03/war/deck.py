"""
Contains the class to hold the card deck containing 52 cards.
"""
import random
from card import Card

class Deck():
    """
    Gets the deck of cards from file card and shuffles them.
    """

    def __init__(self):
        """
        Creates the deck of cards.
        """
        suit = ["Spades", "Hearts", "Clubs", "Diamonds"]
        value = [
            "A",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "J",
            "Q",
            "K"
            ]
        self.deck = []

        for s in suit:
            for v in value:
                self.deck.append(Card(s, v))

    def __repr__(self):
        """
        Uses the __repr__ function from the Card class to create the different
        suits and combines the values for each suit.
        """
        out = ""
        for card in self.deck:
            out += card.__repr__() + ", "
        out = out[:-2]
        return out

    def shuffle_deck(self):
        """
        Shuffles the deck of cards.
        """
        random.shuffle(self.deck)
        return
