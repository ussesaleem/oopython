"""
Contains code for unittesting of the War game.
"""

import unittest
from card import Card
from deck import Deck
from hand import Hand

class CardTest(unittest.TestCase):
    """
    Testing of the Card class.
    """
    def test_create_cards(self):
        """
        Test to create a card (__init__ function).
        """
        cards = Card("Spades", "A")
        self.assertEqual(cards.suit, "Spades")
        self.assertEqual(cards.value, "A")

    def test_value_score(self):
        """
        Test to return a value of the card.
        """
        cards = Card("Spades", "A")
        self.assertEqual(cards.value_score(), 14)

class HandTest(unittest.TestCase):
    """
    Testing of the Hand class.
    """
    def test_cards_list(self):
        """
        Tests if the card attribute is initiated as a list.
        """
        cards = Hand("A")
        self.assertIsInstance(cards.cards, list)

    def test_pop_card(self):
        """
        Tests if the pop function returns None, as initiated as
        no current_card is currently active.
        """
        cards = Hand(["A", "2", "3"])
        self.assertNotEqual(cards.draw_card(), "3")

class DeckTest(unittest.TestCase):
    """
    Testing of the Deck class.
    """
    def test_deck(self):
        """
        Tests if the deck used in the method shuffle_deck is not
        empty as the deck is initiated through the Deck class.
        """
        deck = Deck()
        self.assertIsNotNone(deck.deck)

if __name__ == "__main__":
    unittest.main(verbosity=3)
