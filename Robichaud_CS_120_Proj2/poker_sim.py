"""
A simple user-implemented game of poker where the user declares which of two hands are better
and gets a point when they guess correctly.

Project 2:
Dylan Robichaud
CS-120 with Chris
04/27/23

I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""

from deck import *
from poker_hand import *

STARTING_POINTS = 0
POINT_EARNED = 1
NUMBER_OF_PLAYERS = 2
CARD_TOTAL_OF_N_HANDS = MAX_HAND_SIZE * NUMBER_OF_PLAYERS
PLAYER_1_WON = 1
PLAYER_2_WON = 2
TIED_GAME = 3

def deal_n_cards(deck_of_cards):
    """
    given a deck of cards, deal a hand of cards and return that hand

    :param deck_of_cards: Deck of cards
    """
    hand = []
    for count in range(MAX_HAND_SIZE):
        dealt_card = deck_of_cards.deal()
        hand.append(dealt_card)
    hand_of_cards = PokerHand(hand)
    return hand_of_cards

def deck_is_insufficient_to_deal_more(deck_of_cards):
    """
    given a deck of cards, determine if it has enough cards to deal to n amount of players, return True if it doesn't
    have enough cards

    :param deck_of_cards: Deck of playing cards
    :return boolean: True if it does not have enough cards to deal to n players
    """
    if deck_of_cards.deck_size() < (CARD_TOTAL_OF_N_HANDS):
        return True

def get_winner(player1_hand, player2_hand):
    """
    given the hand of player1 and player2, return which hand is better

    :param player1_hand: Player 1's hand of cards
    :param player2_hand: Player 2's hand of cards
    :return integer: 1 if player 1 wins, 2 if player 2 wins, 3 if tied game.
    """
    winner = player1_hand.compare_to(player2_hand)
    if winner > 0:
        return PLAYER_1_WON
    elif winner < 0:
        return PLAYER_2_WON
    else:
        return TIED_GAME

def main():
    deck_of_cards = Deck()
    game_over = False
    deck_of_cards.shuffle()
    player1_points = STARTING_POINTS
    while not game_over:
        if deck_is_insufficient_to_deal_more(deck_of_cards):
            print("Game over: No cards left in deck")
            game_over = True
        else:
            player1_hand = deal_n_cards(deck_of_cards)
            print("Player1's Hand:" + "\n" + str(player1_hand))
            player2_hand = deal_n_cards(deck_of_cards)
            print("Player2's Hand:" + "\n" + str(player2_hand))
            actual_winner = get_winner(player1_hand, player2_hand)
            guessed_winner = input("Which hand wins? ( Player1 = 1 || Player2 = 2 || Tie = 3 )")
            if guessed_winner == str(actual_winner):
                player1_points += POINT_EARNED
                print("Correct!")
                print()
            else:
                print("You lost :( ")
                game_over = True
    print("You earned a total of ", player1_points, " points!")


if __name__ == '__main__':
    main()