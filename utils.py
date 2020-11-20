from deck import  Deck
from card import Card
from collections import Counter
import re

def create_hand(strings):
    cards = []
    for item in strings:
        cards.append(Card(int(re.sub(r"[S,H,D,C]",'',item)),re.sub(r"\d+",'',item)))
    return cards



def check_pairs(cards):
    #print(cards)
    counter= Counter([card.rank for card in cards])
    #print(counter)
    if (Counter(counter.values())[2]==1):
        return True
    else:
        return False
    

def check_two_pairs(cards):
    #print(cards)
    counter= Counter([card.rank for card in cards])
    #print(counter)
    if (Counter(counter.values())[2]==2):
        return True
    else:
        return False

    
def check_trips(cards):
    #print(cards)
    counter= Counter([card.rank for card in cards])
    meta_counter = Counter(counter.values())
    #print(counter)
    if (meta_counter[3]==1 and meta_counter[2] != 1):
        return True
    else:
        return False

def check_straight(cards):
    values = [card.rank for card in cards]
    if sorted(values) == list(range(min(values),max(values)+1)):
        return True
    else:
        if sorted(values) ==  [2,3,4,5,14]:
            return True
        return False

def check_flush(cards):
    counter= Counter([card.suit for card in cards])
    meta_counter = Counter(counter.values())
    if (meta_counter[5] == 1):
        return True
    else:
        return False
    
def check_quads(cards):
    #print(cards)
    counter= Counter([card.rank for card in cards])
    meta_counter = Counter(counter.values())
    #print(counter)
    if (meta_counter[4]==1):
        return True
    else:
        return False

def check_full_house(cards):
    #print(cards)
    counter= Counter([card.rank for card in cards])
    meta_counter = Counter(counter.values())
    #print(meta_counter)
    #print(counter)
    if (meta_counter[2]==1 and meta_counter[3]==1):
        return True
    return 0
def check_straight_flush(cards):
    if check_flush(cards) and check_straight(cards):
        return True
    return 0

def check_hand(cards):
    assert(len(cards)==5)
    value = [1,
        check_pairs(cards)*2,
        check_two_pairs(cards)*3,
        check_trips(cards)*4,
        check_straight(cards)*5,
        check_flush(cards)*6,
        check_full_house(cards)*7,
        check_quads(cards)*8,
        check_straight_flush(cards)*9,
    ]
    return max(value)

def get_cards_with_frequency(hand, f):
    counter = Counter([card.rank for card in hand])
    return sorted([card_freq for card_freq in counter if counter[card_freq]==f])


def compare_hand(hand_a,hand_b):
    a = check_hand(hand_a)
    b = check_hand(hand_b)
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        ## Case for two high card
        if a == 1 and b == 1:
            if max([card.rank for card in hand_a]) > max([card.rank for card in hand_b]):
                return 1
            elif max([card.rank for card in hand_a]) < max([card.rank for card in hand_b]):
                return -1
            else:
                return 0
        ## Case for pairs
        if a == 2 and b == 2:
            if get_cards_with_frequency(hand_a,2)[-1] > get_cards_with_frequency(hand_b,2)[-1]:
                return 1
            elif get_cards_with_frequency(hand_a,2)[-1] < get_cards_with_frequency(hand_b,2)[-1]:
                return -1
            else:
                if get_cards_with_frequency(hand_a,1)> get_cards_with_frequency(hand_b,1):
                    return 1
                elif get_cards_with_frequency(hand_a,1)< get_cards_with_frequency(hand_b,1):
                    return -1
                else:
                    return 0
        
        ## Case for two two pairs
        if a == 3 and b == 3:
            if get_cards_with_frequency(hand_a,2)[-1] > get_cards_with_frequency(hand_b,2)[-1]:
                return 1
            elif get_cards_with_frequency(hand_a,2)[-1] < get_cards_with_frequency(hand_b,2)[-1]:
                return -1
            else:
                if get_cards_with_frequency(hand_a,2)[-2] > get_cards_with_frequency(hand_b,2)[-2]:
                    return 1
                elif get_cards_with_frequency(hand_a,2)[-2] < get_cards_with_frequency(hand_b,2)[-2]:
                    return -1
                else:
                    if get_cards_with_frequency(hand_a,1)> get_cards_with_frequency(hand_b,1):
                        return 1
                    elif get_cards_with_frequency(hand_a,1)< get_cards_with_frequency(hand_b,1):
                        return -1
                    else:
                        return 0
        ## Case for trips
        if a == 4 and b == 4:
            if get_cards_with_frequency(hand_a,3)[-1] > get_cards_with_frequency(hand_b,3)[-1]:
                return 1
            elif get_cards_with_frequency(hand_a,3)[-1] < get_cards_with_frequency(hand_b,3)[-1]:
                return -1
            else:
                if get_cards_with_frequency(hand_a,1)> get_cards_with_frequency(hand_b,1):
                    return 1
                elif get_cards_with_frequency(hand_a,1)< get_cards_with_frequency(hand_b,1):
                    return -1
                else:
                    return 0
                
        
  
    
        ## Check for straight
        
        if a == 5 and b == 5:
            ranks_a = [card.rank for card in hand_a]
            ranks_b = [card.rank for card in hand_b]
            
            if sorted(ranks_a)[-2] > sorted(ranks_b)[-2]:
                return 1
            elif sorted(ranks_a)[-2] < sorted(ranks_b)[-2]:
                return -1
            else:
                return 0
        
        ## Check for flush
        if a == 6 and b == 6:
            ranks_a = [card.rank for card in hand_a]
            ranks_b = [card.rank for card in hand_b]
            
            if max(ranks_a) > max(ranks_b):
                return 1
            elif max(ranks_a) < max(ranks_b):
                return -1
            else:
                return 0
        
        
        ## Case for two full house 
        if a == 7 and b == 7:
            counter_a= Counter([card.rank for card in hand_a])
            counter_b= Counter([card.rank for card in hand_b])
            
            if list(counter_a.keys())[list(counter_a.values()).index(3)] > list(counter_b.keys())[list(counter_b.values()).index(3)]:
                return 1
            elif list(counter_a.keys())[list(counter_a.values()).index(3)] < list(counter_b.keys())[list(counter_b.values()).index(3)]:
                return -1
            else:
                if list(counter_a.keys())[list(counter_a.values()).index(2)] > list(counter_b.keys())[list(counter_b.values()).index(2)]:
                    return 1
                elif list(counter_a.keys())[list(counter_a.values()).index(2)] < list(counter_b.keys())[list(counter_b.values()).index(2)]:
                    return -1
                else:
                    return 0
        
        ##Check for quads
        if a == 8 and b == 8:
            if get_cards_with_frequency(hand_a,4)[-1] > get_cards_with_frequency(hand_b,4)[-1]:
                return 1
            elif get_cards_with_frequency(hand_a,4)[-1] < get_cards_with_frequency(hand_b,4)[-1]:
                return -1
            else:
                if get_cards_with_frequency(hand_a,1)> get_cards_with_frequency(hand_b,1):
                    return 1
                elif get_cards_with_frequency(hand_a,1)< get_cards_with_frequency(hand_b,1):
                    return -1
                else:
                    return 0

        ## Check for straight flush
        if a == 9 and b == 9:
            ranks_a = [card.rank for card in hand_a]
            ranks_b = [card.rank for card in hand_b]
            
            if max(ranks_a) > max(ranks_b):
                return 1
            elif max(ranks_a) < max(ranks_b):
                return -1
            else:
                return 0
        

    