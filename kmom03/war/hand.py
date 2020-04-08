"""
Contains the class to create the players used in the War game.
"""

class Hand():
    """
    Creates the players and divides the card deck between the players.
    """
    def __init__(self, cards):
        """
        Initializes a list to save the player's cards into and creates a
        current_card variable for use.
        """
        if cards == isinstance(cards, list):
            self.cards = cards
        else:
            self.cards = list(cards)
        self.current_card = None

    def draw_card(self):
        """
        Pops a card out of the player's deck.
        """
        self.current_card = self.cards.pop()
