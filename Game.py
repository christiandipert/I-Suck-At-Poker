import poker
import random
from typing import List

class Poker:
    
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.pot = 0
        self.unsorted_deck = self.create_deck()
        self.shuffled_deck = self.shuffle_deck(self.unsorted_deck)
        self.hands = self.deal_hands()
        self.players = [[] for _ in range(numPlayers)]  # Initialize an empty hand for each player
        
    def create_deck(self) -> List[poker.Card]:
        return list(poker.Card)
    
    def shuffle_deck(self, deck: List[poker.Card]) -> List[poker.Card]:
        random.shuffle(deck)
        return deck
    
    def deal_hands(self):
        return [(self.shuffled_deck.pop(), self.shuffled_deck.pop()) for _ in range(self.numPlayers)]
    
    def deal_cards(self):
        self.flop = [self.shuffled_deck.pop() for _ in range(3)]
        self.turn = self.shuffled_deck.pop()
        self.river = self.shuffled_deck.pop()
        print(len(self.shuffled_deck))
        
