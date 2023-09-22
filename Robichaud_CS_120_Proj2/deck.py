"""defines a standard deck of 52 playing cards"""

from card import *
import random

class Deck:

    def __init__(self):
        """
        constructor: initializes the instance variables
        """
        self.__deck_contents = []
        for rank in RANKS:
            for suit in SUITS:
                new_card = Card(rank,suit)
                self.__deck_contents.append(new_card)

    def shuffle(self):
        """
        Shuffles the deck of cards
        """
        random.shuffle(self.__deck_contents)
        return self.__deck_contents

    def deal(self):
        """
        Deals the top card off the deck and returns it.
        Return None if deck is empty

        :return: Card on top of the deck
        """
        if len(self.__deck_contents) == 0:
            return None
        else:
            return self.__deck_contents.pop(0)

    def deck_size(self):
        """
        returns the number of cards left in the deck as an integer
        """
        return len(self.__deck_contents)

    def __str__(self):
        """
        returns string version of Deck, one card per line
        ex:
        9 of Diamonds
        Ace of Spades
        8 of Clubs
        etc.
        """
        to_return = ""
        for card in self.__deck_contents:
            to_return=to_return + str(card) + "\n"
        return to_return