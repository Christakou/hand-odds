from card import Card
import  re 
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.discarted = []
        ranks = range(2,15)
        suits = ['S','H','D','C']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank,suit))
    def shuffle(self):
        random.shuffle(self.cards)
        return self
    
    def remove_cards(self, list_of_cards_to_remove):
        self.cards = [card for card in self.cards if card not in list_of_cards_to_remove]
        
    def deal(self, number=1, card_list = None):
        if self.count() >= number:
            dealed_cards = [self.cards.pop() for a in range(number)]
            [self.discarted.append(card) for card in dealed_cards]
            return dealed_cards
        else:
            dealed_cards = [self.cards.pop() for a in range(self.count())]
            [self.discarted.append(card) for card in dealed_cards]
            return dealed_cards
    def count(self):
        return len(self.cards)
    def reshuffle(self):
        self.__init__()
        return self.shuffle()
