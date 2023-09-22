from testing import *
from poker_hand import *

def test_poker_hand_class():
    start_tests("Starting tests on hand types (player 1 (p1) hand vs. player 2 (p2) hand) determind which is better")
    test_flush_vs_two_pair()
    test_flush_vs_pair()
    test_flush_vs_high_card()
    test_two_pair_vs_flush()
    test_pair_vs_flush()
    test_high_card_vs_flush()
    test_high_card_vs_low_card()
    test_low_card_vs_high_card()
    test_high_high_vs_high_low()
    test_high_low_vs_high_high()
    test_3high_vs_2high_1low()
    test_2high_1low_vs_3high()
    test_4high_vs_3high_1low()
    test_3high_1low_vs_4high()
    test_5high_vs_4high_1low()
    test_4high_1low_vs_5high()
    test_same_exact_high_card()
    test_high_pair_vs_low_pair()
    test_low_pair_vs_high_pair()
    test_same_pair_high_vs_low()
    test_same_pair_low_vs_high()
    test_same_pair_2high_vs_1high_1low()
    test_same_pair_1high_1low_vs_2high()
    test_same_pair_3_high_vs_2high_1low()
    test_same_pair_2high_1low_vs_3high()
    test_same_pair_same_high_card()
    test_high_pair_high_pair_vs_low_pair_low_pair()
    test_low_pair_low_pair_vs_high_pair_high_pair()
    test_high_pair_high_pair_vs_high_pair_low_pair()
    test_high_pair_low_pair_vs_high_pair_high_pair()
    test_same_two_pair_highcard_vs_lowcard()
    test_same_two_pair_lowcard_vs_highcard()
    test_same_two_pair_same_high_card()
    test_4_of_a_kind_high_vs_low()
    test_4_of_a_kind_low_vs_high()
    test_4_of_a_kind_vs_pair()
    test_both_flush_highcard_vs_lowcard()
    test_both_flush_highcard_vs_lowcard()
    test_both_flush_2highcards_vs_1highcard_1lowcard()
    test_both_flush_1highcard_1lowcard_vs_2highcards()
    test_both_flush_3highcards_vs_2highcards_1lowcard()
    test_both_flush_2highcards_1lowcard_vs_3highcards()
    test_both_flush_4highcards_vs_3highcards_1lowcard()
    test_both_flush_3highcards_1lowcard_vs_4highcards()
    test_both_flush_5highcard_vs_4highcard_1lowcard()
    test_both_flush_4highcard_1lowcard_vs_5highcard()
    test_same_exact_flush()
    finish_tests()

def test_flush_vs_two_pair():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'D')
    card3 = Card(3, 'D')
    card4 = Card(12, 'D')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(3, 'S')
    card9 = Card(5, 'D')
    card10 = Card(2, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test flush hand vs two pair hand"
    expected = 1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_flush_vs_pair():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'D')
    card3 = Card(3, 'D')
    card4 = Card(12, 'D')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(7, 'S')
    card9 = Card(5, 'D')
    card10 = Card(2, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test flush hand vs pair hand"
    expected = 2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)


def test_flush_vs_high_card():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'D')
    card3 = Card(3, 'D')
    card4 = Card(12, 'D')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(2, 'C')
    card8 = Card(9, 'S')
    card9 = Card(5, 'D')
    card10 = Card(12, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test flush hand vs high card"
    expected = 3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)


def test_two_pair_vs_flush():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(2, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(12, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'D')
    card8 = Card(7, 'D')
    card9 = Card(9, 'D')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two-pair hand vs flush hand"
    expected = -1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_pair_vs_flush():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(2, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'D')
    card8 = Card(7, 'D')
    card9 = Card(9, 'D')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test pair hand vs flush hand"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_card_vs_flush():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'D')
    card8 = Card(7, 'D')
    card9 = Card(9, 'D')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test high card hand vs flush hand"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_card_vs_low_card():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(7, 'S')
    card9 = Card(9, 'H')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: high card of p1 is higher than p2"
    expected = 2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)


def test_low_card_vs_high_card():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(7, 'S')
    card9 = Card(9, 'H')
    card10 = Card(14, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: high card of p1 is lower than p2"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_high_vs_high_low():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(3, 'C')
    card4 = Card(12, 'H')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(7, 'S')
    card9 = Card(9, 'H')
    card10 = Card(13, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: high card's are the same. second high card of p1 is higher than p2 " +\
          "(13,12 vs. 13,9)"
    expected = 3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_low_vs_high_high():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(3, 'C')
    card4 = Card(7, 'H')
    card5 = Card(13, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(7, 'S')
    card9 = Card(9, 'H')
    card10 = Card(13, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: high card's are the same. second high card of p1 is lower than p2 " +\
          "(13,7 vs. 13,9)"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_3high_vs_2high_1low():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(6, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: first 2 high card's are the same. third high card of p1 is higher than p2" +\
          " (13,12,11 vs. 13,12,6)"
    expected = 5
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_2high_1low_vs_3high():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(4, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(3, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(5, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(6, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: first 2 high card's are the same. third high card of p1 is lower than p2" +\
          " (13,12,4 vs. 13,12,6)"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_4high_vs_3high_1low():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(14, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(14, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(5, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: first 3 high card's are the same. fourth high card of p1 is higher than p2" +\
          " (14,13,12,11 vs. 14,13,12,5)"
    expected = 6
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_3high_1low_vs_4high():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(14, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(4, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(14, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands: first 3 high card's are the same. fourth high card of p1 is lower than p2" +\
          " (14,13,12,4 vs. 14,13,12,11)"
    expected = -7
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_5high_vs_4high_1low():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(14, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(3, 'D')
    card7 = Card(14, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands which have the same ranks except for the last number. last rank of p1 hand is " +\
          "higher than p2: (14,13,12,11,10 vs. 14,13,12,11,3)"
    expected = 7
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_4high_1low_vs_5high():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(14, 'S')
    card3 = Card(13, 'C')
    card4 = Card(12, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'D')
    card7 = Card(14, 'C')
    card8 = Card(13, 'S')
    card9 = Card(12, 'H')
    card10 = Card(11, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands which have the same ranks except for the last number. last rank of p1 hand is " +\
          "lower than p2: (14,13,12,11,10 vs. 14,13,12,11,3)"
    expected = -8
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_exact_high_card():
    player1_hand = []
    card1 = Card(10, 'S')
    card2 = Card(9, 'D')
    card3 = Card(8, 'C')
    card4 = Card(7, 'D')
    card5 = Card(6, 'H')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'D')
    card7 = Card(9, 'H')
    card8 = Card(8, 'C')
    card9 = Card(7, 'S')
    card10 = Card(6, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two high card hands where every rank is the same (10,9,8,7,6 vs. 10,9,8,7,6)"
    expected = 0
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_pair_vs_low_pair():
    player1_hand = []
    card1 = Card(13, 'D')
    card2 = Card(13, 'S')
    card3 = Card(3, 'C')
    card4 = Card(6, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'D')
    card7 = Card(8, 'C')
    card8 = Card(2, 'S')
    card9 = Card(4, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: p1 hand pair value higher than p2 (13,13 vs 8,8)"
    expected = 5
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_low_pair_vs_high_pair():
    player1_hand = []
    card1 = Card(4, 'D')
    card2 = Card(6, 'S')
    card3 = Card(3, 'C')
    card4 = Card(6, 'H')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'D')
    card7 = Card(8, 'C')
    card8 = Card(2, 'S')
    card9 = Card(4, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: p1 hand pair value lower than p2 (6,6 vs 8,8)"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_high_vs_low():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(2, 'C')
    card4 = Card(6, 'H')
    card5 = Card(8, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(2, 'S')
    card9 = Card(4, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, high card of p1 is higher than p2 (10,10,8 vs 10,10,4)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_low_vs_high():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(2, 'C')
    card4 = Card(6, 'H')
    card5 = Card(5, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(9, 'S')
    card9 = Card(4, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, high card of p1 is higher than p2 (10,10,6 vs 10,10,9)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_2high_vs_1high_1low():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(9, 'C')
    card4 = Card(6, 'H')
    card5 = Card(5, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(9, 'S')
    card9 = Card(4, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, 1st high card is same. 2nd high card of p1 is" +\
          "higher than p2 (10,10,9,6 vs 10,10,9,4)"
    expected = 2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_1high_1low_vs_2high():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(9, 'C')
    card4 = Card(2, 'H')
    card5 = Card(5, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(9, 'S')
    card9 = Card(8, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, 1st high card is same. 2nd high card of p1 is" +\
          "higher than p2 (10,10,9,5 vs 10,10,9,8)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_3_high_vs_2high_1low():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(9, 'C')
    card4 = Card(8, 'H')
    card5 = Card(7, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(9, 'S')
    card9 = Card(8, 'D')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, 1st high card is same. 2nd high card of p1 is" +\
          "higher than p2 (10,10,9,8,7 vs 10,10,9,8,3)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_2high_1low_vs_3high():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(9, 'C')
    card4 = Card(8, 'H')
    card5 = Card(2, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(9, 'S')
    card9 = Card(8, 'S')
    card10 = Card(5, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, 1st high card is same. 2nd high card of p1 is" +\
          "higher than p2 (10,10,9,8,2 vs 10,10,9,8,5)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_pair_same_high_card():
    player1_hand = []
    card1 = Card(4, 'D')
    card2 = Card(4, 'S')
    card3 = Card(9, 'C')
    card4 = Card(8, 'H')
    card5 = Card(7, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(4, 'H')
    card7 = Card(4, 'C')
    card8 = Card(9, 'S')
    card9 = Card(8, 'C')
    card10 = Card(7, 'H')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type pair: pair value is the same, 1st high card is same. 2nd high card of p1 is" +\
          "higher than p2 (4,4,9,8,7 vs 4,4,9,8,7)"
    expected = 0
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_pair_high_pair_vs_low_pair_low_pair():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(7, 'C')
    card4 = Card(7, 'H')
    card5 = Card(8, 'S')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'D')
    card7 = Card(8, 'C')
    card8 = Card(2, 'S')
    card9 = Card(2, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: higher pair value of p1 is higher than p2 (10,10 vs 8,8)"
    expected = 2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_low_pair_low_pair_vs_high_pair_high_pair():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(2, 'S')
    card3 = Card(4, 'C')
    card4 = Card(4, 'H')
    card5 = Card(3, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'D')
    card7 = Card(8, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(2, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: higher pair value of p1 is higher than p2 (4,4,2,2 vs 8,8,5,5)"
    expected = -4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_pair_high_pair_vs_high_pair_low_pair():
    player1_hand = []
    card1 = Card(8, 'D')
    card2 = Card(8, 'S')
    card3 = Card(7, 'C')
    card4 = Card(7, 'H')
    card5 = Card(4, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'H')
    card7 = Card(8, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: higher pair value of p1 is same as p2. next pair of p1 is higher than p2 " +\
          "(8,8,7,7 vs 8,8,5,5)"
    expected = 2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_high_pair_low_pair_vs_high_pair_high_pair():
    player1_hand = []
    card1 = Card(8, 'D')
    card2 = Card(8, 'S')
    card3 = Card(4, 'C')
    card4 = Card(7, 'H')
    card5 = Card(4, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(8, 'H')
    card7 = Card(8, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: higher pair value of p1 is same as p2. next pair of p1 is lower than p2 " +\
          "(8,8,4,4 vs 8,8,5,5)"
    expected = -1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_two_pair_highcard_vs_lowcard():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(5, 'C')
    card4 = Card(5, 'D')
    card5 = Card(14, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(3, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: both pairs are of the same ranks. high card of p1 is higher than p2 " +\
          "(10,10,5,5,14 vs 10,10,5,5,3)"
    expected = 11
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_two_pair_lowcard_vs_highcard():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(5, 'C')
    card4 = Card(5, 'D')
    card5 = Card(2, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(13, 'D')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: both pairs are of the same ranks. high card of p1 is higher than p2 " +\
          "(10,10,5,5,2 vs 10,10,5,5,13)"
    expected = -11
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_two_pair_same_high_card():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(5, 'C')
    card4 = Card(5, 'D')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'H')
    card7 = Card(10, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'H')
    card10 = Card(11, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type two pair: both pairs are of the same ranks. high card is the same rank too. " +\
          "(10,10,5,5,11 vs 10,10,5,5,11)"
    expected = 0
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_4_of_a_kind_high_vs_low():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(10, 'S')
    card3 = Card(10, 'H')
    card4 = Card(10, 'C')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(5, 'H')
    card7 = Card(5, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'D')
    card10 = Card(11, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type four-of-a-kind: rank of four-of-a-kind in p1's hand is higher than p2 " +\
          "(10,10,10,10 vs 5,5,5,5)"
    expected = 5
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_4_of_a_kind_low_vs_high():
    player1_hand = []
    card1 = Card(2, 'D')
    card2 = Card(2, 'S')
    card3 = Card(2, 'H')
    card4 = Card(2, 'C')
    card5 = Card(11, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(5, 'H')
    card7 = Card(5, 'C')
    card8 = Card(5, 'S')
    card9 = Card(5, 'D')
    card10 = Card(11, 'S')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type four-of-a-kind: rank of four-of-a-kind in p1's hand is lower than p2 " +\
          "(2,2,2,2, vs 5,5,5,5)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_highcard_vs_lowcard():
    player1_hand = []
    card1 = Card(11, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first high card in p1's hand is higher than p2 (D: 11 vs C: 10)"
    expected = 1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_lowcard_vs_highcard():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first high card in p1's hand is lower than p2 (D: 10 vs C: 14)"
    expected = -4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_2highcards_vs_1highcard_1lowcard():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(12, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first high card in hands are same. second high card in p1 hand is" +\
          "higher than in p2 (D: 14,12 vs C: 14,9)"
    expected = 3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_1highcard_1lowcard_vs_2highcards():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(11, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first high card in hands are same. second high card in p1 hand is" +\
          "lower than in p2 (D: 14,9 vs C: 14,11)"
    expected = -2
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_3highcards_vs_2highcards_1lowcard():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(13, 'D')
    card3 = Card(12, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(13, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 2 high cards in hands are same. third high card in p1 hand" +\
          "is higher than in p2 (D: 14,13,12 vs C: 14,13,8)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_2highcards_1lowcard_vs_3highcards():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(13, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(13, 'C')
    card8 = Card(11, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 2 high cards in hands are same. third high card in p1 hand" +\
          "is lower than in p2 (D: 14,13,8 vs C: 14,13,11)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_4highcards_vs_3highcards_1lowcard():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(13, 'D')
    card3 = Card(12, 'D')
    card4 = Card(11, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(13, 'C')
    card8 = Card(12, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 3 high cards in hands are same. fourth high card in p1 hand" +\
          "is higher than in p2 (D: 14,13,12,11 vs C: 14,13,12,7)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_3highcards_1lowcard_vs_4highcards():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(13, 'D')
    card3 = Card(12, 'D')
    card4 = Card(5, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(13, 'C')
    card8 = Card(12, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 3 high cards in hands are same. fourth high card in p1 hand" +\
          "is lower than in p2 (D: 14,13,12,6 vs C: 14,13,12,7)"
    expected = -1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_5highcards_vs_3highcards_1lowcard():
    player1_hand = []
    card1 = Card(14, 'D')
    card2 = Card(13, 'D')
    card3 = Card(12, 'D')
    card4 = Card(11, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(14, 'C')
    card7 = Card(13, 'C')
    card8 = Card(12, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 3 high cards in hands are same. fourth high card in p1 hand" +\
          "is higher than in p2 (D: 14,13,12,11 vs C: 14,13,12,7)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)















def test_both_flush_5highcard_vs_4highcard_1lowcard():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(2, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 4 high cards in hands are same. last high card in p1's hand" +\
          "is higher than p2 (D: 10,9,8,7,6 vs C: 10,9,8,7,2)"
    expected = 4
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_both_flush_4highcard_1lowcard_vs_5highcard():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(2, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(5, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: rank of first 4 high cards in hands are same. last high card in p1's hand" +\
          "is lower than p2 (D: 10,9,8,7,2 vs C: 10,9,8,7,5)"
    expected = -3
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)

def test_same_exact_flush():
    player1_hand = []
    card1 = Card(10, 'D')
    card2 = Card(9, 'D')
    card3 = Card(8, 'D')
    card4 = Card(7, 'D')
    card5 = Card(6, 'D')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(10, 'C')
    card7 = Card(9, 'C')
    card8 = Card(8, 'C')
    card9 = Card(7, 'C')
    card10 = Card(6, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test two hands of type flush: each high card is the same exact rank (10,9,8,7,6 vs. 10,9,8,7,6"
    expected = 0
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)


def test_4_of_a_kind_vs_pair():
    player1_hand = []
    card1 = Card(3, 'S')
    card2 = Card(3, 'H')
    card3 = Card(3, 'C')
    card4 = Card(3, 'D')
    card5 = Card(6, 'H')
    player1_hand.append(card1)
    player1_hand.append(card2)
    player1_hand.append(card3)
    player1_hand.append(card4)
    player1_hand.append(card5)
    my_hand = PokerHand(player1_hand)
    player2_hand = []
    card6 = Card(13, 'D')
    card7 = Card(13, 'H')
    card8 = Card(12, 'C')
    card9 = Card(8, 'S')
    card10 = Card(6, 'C')
    player2_hand.append(card6)
    player2_hand.append(card7)
    player2_hand.append(card8)
    player2_hand.append(card9)
    player2_hand.append(card10)
    other_hand = PokerHand(player2_hand)
    value_of_my_hand = my_hand.compare_to(other_hand)
    msg = "test compare_to of 3,3,3,3,6 vs. 13,13,12,8,6"
    expected = 1
    actual = value_of_my_hand
    assert_equals(msg, expected, actual)



test_poker_hand_class()