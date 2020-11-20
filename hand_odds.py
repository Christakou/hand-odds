import functools
from utils  import create_hand, compare_hand
from itertools import combinations
from collections import Counter
from deck import Deck
import time


def determine_winner(hands, board):
    #print(hands,'Hands')
    #print(board,'BOARD')
    key=functools.cmp_to_key(lambda a, b: compare_hand(a, b))
    best_hands = []
    for index, hand in enumerate(hands):
        best_hands.append(sorted(list(combinations(hand+board,5)),key=key)[-1])
    winner_index = best_hands.index(sorted(best_hands,key=key)[-1])
    #print(winner_index)
    return winner_index
    


def simulate_play(your_hand,cards_shown,number_of_opponents):
    board = []
    try:
        your_hand = create_hand(your_hand)
        cards_shown = create_hand(cards_shown)
        board += cards_shown
    except Exception as e:
        print(e)
    new_deck = Deck().reshuffle()
    new_deck.remove_cards(your_hand)
    hands = []
    hands+= [your_hand]

    for i in range(number_of_opponents):
        hands.append(new_deck.deal(2))
    board+=new_deck.deal(5-len(cards_shown))
    return determine_winner(hands, board)


