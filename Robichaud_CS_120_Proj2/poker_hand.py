"""defines a hand of playing cards"""

from deck import *
from card import *

MAX_HAND_SIZE = 5
FLUSH = 4
TWO_PAIR = 3
PAIR = 2
HIGH_CARD = 1
SAME_HAND = 0

class PokerHand:

    def __init__(self, card_list):
        """
        constructor = initializes the instance variables

        :param card_list: list of cards
        """
        self.__full_hand = card_list.copy()

    def add_card(self, given_card):
        """
        adds a playing card to the hand only if their hand isn't full

        :param given_card: Card object
        """
        if len(self.__full_hand) < MAX_HAND_SIZE:
            self.__full_hand.append(given_card)

    def get_ith_card(self, index):
        """
        given an index (int >= 0) as a parameter,
        return the card (the Card object) at that index
        
        :param index: index #
        :return card at given index
        """
        return self.__full_hand[index]

    def __str__(self):
        """
        return string version of Hand, one per line
        """
        to_return = ""
        for card in self.__full_hand:
            to_return = to_return + str(card) + '\n'
        return to_return

    def __ranks_in_hand(self):
        """
        return a list of the ranks in the hand, in order from greatest rank to least rank
        """
        self.ranks = []
        for card_index in range(0, MAX_HAND_SIZE):
            card = self.get_ith_card(card_index)
            rank = card.get_rank()
            self.ranks.append(rank)
        sorted_ranks = sorted(self.ranks, reverse=True)
        return sorted_ranks

    def __suits_in_hand(self):
        """
        return a list of the suits in the hand
        """
        self.suits = []
        for i in range(0, MAX_HAND_SIZE):
            card = self.get_ith_card(i)
            suit = card.get_suit()
            self.suits.append(suit)
        return self.suits

    def check_hand(self, ranks, suits):
        """
        checks which type of hand it is

        :param ranks: a list of the current ranks in the hand
        :param suits: a list of the current suits in the hand
        :return hand_value: integer where flush = 4, two-pair = 3, pair = 2, high card = 1 
        """
        if self.__is_flush(suits):
            hand_value = FLUSH
        elif self.__is_two_pair(ranks):
            hand_value = TWO_PAIR
        elif self.__is_pair(ranks):
            hand_value = PAIR
        elif self.__is_high_card():
            hand_value = HIGH_CARD
        return hand_value

    def __is_flush(self, suits):
        """
        decides whether the hand is a flush or not

        :param suits: a list containing the suit of each card in hand
        :return boolean: True if it contains a flush, false if not
        """
        if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
            return True
        else:
            return False

    def __is_two_pair(self, ranks):
        """
        decides whether the hand contains a two pair or not

        :param ranks: a list containing the rank of each card in hand
        :return boolean: True if hand contains a two pair
        """
        counts = {}
        pairs = 0
        for rank in ranks:
            if rank in counts:
                counts[rank] += 1
                if counts[rank] == 2:
                    pairs += 1
            else:
                counts[rank] = 1
        for count in counts.values():
            if count >= 4:
                pairs += 1
        if pairs >= 2:
            return True

    def __is_pair(self, ranks):
        """
        decides whether the hand contains a pair or not

        :param ranks: a list containing the rank of each card in hand
        :return boolean: True if hand contains a pair
        """
        len_ranks = len(ranks)
        for i in range(0, len_ranks - 1):
            for j in range(i + 1, len_ranks):
                if ranks[i] == ranks[j]:
                    return True

    def __is_high_card(self):
        """
        if it's none of the other three types of hands, it's automatically a
        high card hand

        :return boolean: Always returns True
        """
        return True

    def __compare_flush(self, other_hand, my_ranks, other_ranks):
        """
        compare which hand of type flush is better by comparing the high cards in each hand.

        :param other_hand: Hand of other player to compare with
        :param my_ranks: List of current ranks in my hand
        :param other_ranks: List of current ranks in other hand
        :return the difference between the high card value of each hand
        """
        return self.__compare_high_cards(other_hand, my_ranks, other_ranks)

    def __compare_two_pair(self, other_hand, my_ranks, other_ranks):
        """
        compares both pairs of ranks-- in my hand and other hand -- and determines which pair is better (higher number),
        then returns the difference between the rank values.
        If the higher pair values are different, return the difference of the pair values
        If the higher pair values are the same, compare the lower pair value of each hand. If those values differ,
        return the difference of the two. If their values are the same, return the difference of the high card values.

        :param other_hand: Hand of other player to compare with
        :param my_ranks: List of current ranks in my hand
        :param other_ranks: List of current ranks in other hand
        :return the difference of whichever components vary, whether it's the first pair, second pair, or high card
        """
        my_higher_pair = self.__obtain_pair_value(my_ranks)
        my_lower_pair = self.__obtain_pair_value(my_ranks)
        other_higher_pair = other_hand.__obtain_pair_value(other_ranks)
        other_lower_pair = other_hand.__obtain_pair_value(other_ranks)
        if my_higher_pair != other_higher_pair:
            return my_higher_pair - other_higher_pair
        elif my_higher_pair == other_higher_pair:
            if my_lower_pair != other_lower_pair:
                return my_lower_pair - other_lower_pair
            else:
                return self.__compare_high_cards(other_hand, my_ranks, other_ranks)

    def __obtain_pair_value(self, ranks):
        """
        given a list of ranks, retrieve the rank of the pair, pop both occurrences of the rank out of the list,
        then return the rank value

        :param ranks: a list containing the rank of each card in hand
        :return boolean: True if it contains a pair
        """
        len_ranks = len(ranks)
        for i in range(0, len_ranks - 1):
            for j in range(i + 1, len_ranks):
                if ranks[i] == ranks[j]:
                    pair_value = ranks[i]
                    ranks.remove(pair_value)
                    ranks.remove(pair_value)
                    return pair_value

    def __compare_pair(self, other_hand, my_ranks, other_ranks):
        """
        compares which pair of ranks -- in my hand and other hand -- is better (higher number), then return
        the difference between the rank values. If the pair is the same (ex: both pair of 8's), then compare their
        high card values and return the difference.

        :param other_hand: Hand of other player to compare with
        :param my_ranks: List of current ranks in my hand
        :param other_ranks: List of current ranks in other hand
        :return difference of pair values if the ranks differ, or if they're equal, return the difference of the
        high card of each hand
        """
        my_pair = self.__obtain_pair_value(my_ranks)
        other_pair = other_hand.__obtain_pair_value(other_ranks)
        if my_pair == other_pair:
            return self.__compare_high_cards(other_hand, my_ranks, other_ranks)
        else:
            return my_pair - other_pair

    def __obtain_high_card_value(self, ranks):  # Do I need to include hand values as param??
        """
        given a list of ranks, retrieve the value of the highest rank, pop it out of the list,
        then return in.
        Note that we are popping at index 0 because the list of ranks is already in order
        from greatest to least number.

        :param ranks: List of ranks in hand
        :return high_card: highest rank in list
        """
        high_card = ranks.pop(0)
        return high_card

    def __compare_high_cards(self, other_hand, my_ranks, other_ranks):
        """
        compares the rank of the high card in both my hand and other hand. If the ranks are the same, compare the
        next high card's with each other. If they're the same, repeat the process until their values differ,
        then return the difference of the two. If all high cards are the same, return 0.

        :param other_hand: Hand of other player to compare with
        :param my_ranks: List of current ranks in my hand
        :param other_ranks: List of current ranks in other hand
        :return difference between the high card of each hand, 0 if they're the same hand
        """
        my_high_card = self.__obtain_high_card_value(my_ranks)
        other_high_card = other_hand.__obtain_high_card_value(other_ranks)
        my_current_high_card = my_high_card
        other_current_high_card = other_high_card
        while my_current_high_card == other_current_high_card:
            if len(my_ranks) > 0:
                my_current_high_card = self.__obtain_high_card_value(my_ranks)
                other_current_high_card = other_hand.__obtain_high_card_value(other_ranks)
            else:
                return SAME_HAND
        return my_current_high_card - other_current_high_card

    def compare_to(self, other_hand):
        """
        Determines which of two poker hands is worth more. Returns an int
        which is either positive, negative, or zero depending on the comparison.
        
        :param self: The first hand to compare
        :param other_hand: The second hand to compare
        :return: a negative number if self is worth LESS than other_hand,
        zero if they are worth the SAME (a tie), and a positive number if
        self is worth MORE than other_hand
        """
        my_ranks = self.__ranks_in_hand().copy()
        my_suits = self.__suits_in_hand().copy()
        other_ranks = other_hand.__ranks_in_hand()
        other_suits = other_hand.__suits_in_hand()
        my_type = self.check_hand(my_ranks, my_suits)
        other_type = other_hand.check_hand(other_ranks, other_suits)
        if my_type != other_type:
            return my_type - other_type
        elif my_type == FLUSH:
            return self.__compare_flush(other_hand, my_ranks, other_ranks)
        elif my_type == TWO_PAIR:
            return self.__compare_two_pair(other_hand, my_ranks, other_ranks)
        elif my_type == PAIR:
            return self.__compare_pair(other_hand, my_ranks, other_ranks)
        elif my_type == HIGH_CARD:
            return self.__compare_high_cards(other_hand, my_ranks, other_ranks)