"""
Contains the class to color code and value code the cards.
"""

class Card():
    """
    Creates a deck of cards (52 cards).
    """
    def __init__(self, suit, value):
        """
        Initializes the suit and value for each card.
        """
        self.suit = suit
        self.value = value

    def __repr__(self):
        """
        Returns a string with the value and suit.
        """
        return str(self.value) + " of " + self.suit

    def value_score(self):
        """
        Assigns an integer value to each card to be used in the __lt__ and
        __gt__ methods.
        """
        points = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }
        return points[self.value]

    def __lt__(self, other):
        """
        Compares if player's current card value is less than the other player's.
        """
        return self.value_score() < other.value_score()

    def __gt__(self, other):
        """
        Compares if player's current card value is greater than the other
        player's.
        """
        return self.value_score() > other.value_score()
