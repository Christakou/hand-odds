class Card:
    def __init__(self,rank,suit):
        if rank == 'A':
            self.rank = 14
        else:
            self.rank = rank
        self.suit = suit
        
        self.card = str(rank)+suit
    def getRank(self):
        return self.rank
    def getSuit(self):
        return self.suit
    def getCard(self):
        return self.card
    def __str__(self):
        if self.rank == 14:
            return '\''+'A'+self.suit+'\''
        return '\''+str(self.rank)+self.suit+'\''
    def __repr__(self):
        if self.rank == 14:
            return  '\''+'A'+self.suit+'\''
        return '\''+str(self.rank)+self.suit+'\''
    
    def __eq__(self,other):
        if (self.rank == other.rank)and(self.suit == other.suit):
            return True
        return False
    
    