"""
defines properties and behavior of a single playing card
"""

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
SUITS = ["H", "D", "S", "C"]

class Card:

    def __init__(self,new_rank,new_suit):
        """
        constructor = initializes the instance variables

        :param new_rank: rank of card: 2,3,4 ... 11 = Jack , 12 = Queen, 13 = King, 14 = Ace
        :param new_suit: card's suit: "Clubs","Hearts",etc.
        """
        self.__card_contents = {'rank': new_rank, 'suit': new_suit}

    def get_rank(self):
        """ getter for rank (2,3,4, etc.) """
        return self.__card_contents['rank']

    def get_suit(self):
        """ getter for suit """
        return self.__card_contents['suit']

    def __str__(self):
        """
        returns string version of the card like 'Jack of Clubs'
        """
        rank = self.get_rank()
        suit = self.get_suit()
        if rank == 11:
            rank_string = "Jack"
        elif rank == 12:
            rank_string = "Queen"
        elif rank == 13:
            rank_string = "King"
        elif rank == 14:
            rank_string = "Ace"
        else:
            rank_string = str(rank)
        if suit == "D":
            suit_string = "Diamonds"
        elif suit == "S":
            suit_string = "Spades"
        elif suit == "C":
            suit_string = "Clubs"
        elif suit == "H":
            suit_string = "Hearts"
        return rank_string + " of " + suit_string