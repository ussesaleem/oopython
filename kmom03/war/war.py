"""
Contains the class with the logic of the War game.
"""
from hand import Hand
from deck import Deck

class War():
    """
    Contains the logic of the game, using the hands and decks created in the
    card-, deck- and hand- files.
    """
    def __init__(self):
        """
        Initializes the game deck and creates the players as well as creating
        an empty list to represent the deck on the "table".
        """
        self.game_deck = Deck()
        self.game_deck.shuffle_deck()

        self.player1 = Hand(self.game_deck.deck[0:26])
        self.player2 = Hand(self.game_deck.deck[26:52])

        self.drawdeck = []

    def game_logic(self):
        """
        Contains the logic of the game to draw the player's cards and compare
        the values if the suit is the same, giving the deck of the table to
        the player with the highest value.
        """
        while True:
            choice = input("Press any key to continue... (or q to quit) ")

            if choice != "q":
                try:
                    self.player1.draw_card()
                    print("\nPlayer 1 drew " + str(self.player1.current_card))
                    self.drawdeck.append(self.player1.current_card)
                    self.player2.draw_card()
                    print("Player 2 drew " + str(self.player2.current_card) +
                          "\n")
                    self.drawdeck.append(self.player2.current_card)
                except IndexError:
                    player1_cards = len(self.player1.cards)
                    player2_cards = len(self.player2.cards)
                    if player1_cards == 0:
                        print("Player 1 lost the game.\n")
                    elif player2_cards == 0:
                        print("Player 2 lost the game.\n")
                    break

                player1_suit = self.player1.current_card.suit
                player2_suit = self.player2.current_card.suit

                if player1_suit == player2_suit:
                    if self.player1.current_card < self.player2.current_card:
                        print("Player 2 won the deck.")
                        self.player2.cards.extend(self.drawdeck)
                        self.drawdeck = []
                        print("\nStatus:\n" +
                              "Player 1 has " + str(len(self.player1.cards)) +
                              " cards.\n" +
                              "Player 2 has " + str(len(self.player2.cards)) +
                              " cards.\n")

                    elif self.player1.current_card > self.player2.current_card:
                        print("Player 1 won the deck.")
                        self.player1.cards.extend(self.drawdeck)
                        self.drawdeck = []
                        print("\nStatus:\n" +
                              "Player 1 has " + str(len(self.player1.cards)) +
                              " cards.\n" +
                              "Player 2 has " + str(len(self.player2.cards)) +
                              " cards.\n")
                else:
                    continue

            elif choice == "q":
                print("Bye!")
                break


warDeck = War()
warDeck.game_logic()
