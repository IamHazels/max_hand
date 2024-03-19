from enum import Enum
import random

class Suit(Enum):
    SPADES = 4
    HEARTS = 3
    DIAMONDS = 2
    CLUBS = 1



class PlayingCard:
    
    def __init__(self,rank,suit):
        self._rank = rank
        self._suit = suit 
        
    def get_rank(self):
        return self._rank 
    
    def get_suit(self):
        return self._suit 
    
    
    def set_hand(self, hand):
        self._hand = hand 
        
        
class Player:
    def __init__(self,name):
        self._name = name
        self._hand = []
        
    def get_name(self):
        return self._name
        
    def get_hand(self):
        return self._hand 
    
    def strongest_hand(self):
        if len(self._hand) == 2:
            if self._hand[0].get_rank()> self._hand[1].get_rank():
                return self._hand[0]
            elif self._hand[0].get_rank()< self._hand[1].get_rank():
                return self._hand[1]
            elif self._hand[0].get_suit().value > self._hand[1].get_suit().value:
                return self._hand[0]
            else:
                return self._hand[1]
            
class Cheater(Player):
    def strongest_card(self):
        if random.randint(1,10) <= 2:
            return PlayingCard(14, Suit.SPADES)
        else:
            return super().strongest_card()
    
class Deck:
    
    def __init__(self):
        self._cards = []
        for i in range(13):
            self._cards.append(PlayingCard(i+2, Suit.SPADES))
            self._cards.append(PlayingCard(i+2, Suit.DIAMONDS))
            self._cards.append(PlayingCard(i+2, Suit.HEARTS))
            self._cards.append(PlayingCard(i+2, Suit.CLUBS))
        
    def get_cards(self):
        return self._cards 
    
    def shuffle(self):
        for _ in range(200):
            i, j = random.randint(0,51), random.randit(0,51)
            self._cards[i], self._cards[j] = self._cards[j], self._cards[i]
            
    def draw(self, n):
        if n> len(self._cards):
            return None
        drawn = []
        for _ in range(n):
            c = self._cards.pop()
            drawn.append(c)
        return drawn 
    
class Game:
    
    def __init__(self,players, deck):
        self._players = players
        self._deck = deck
        self._score = {}
        for p in players:
            self._score[p.get_name()] = 0
        
    def show_score(self):
        print("Score:")
        print("_ _ _ _ _ _")
        for k, v in self._score.items():
            print(f'{k}: {v}')
        print('\n')
        
    def play_round(self):
        winning_card = None
        winning_player = None
        for p in self._players:
            hand = self._deck.draw(2)
            p.set_hand(hand)
            print(f'player {p.get_name()} is dealt: [{hand[0]}, {hand[0]}]')
            if winning_card is None or (p.strongest_card().get_rank()> winning_card.get_rank()) or ((p.strongest_card().get_rank == winning_card.get_rank()) and (p.strongest_card().get_suit().value > winning_card.get_suit().value)):
                winning_card = p.strongest_card()
                winning_player = p
                
        print(f'PLAYER {winning_player.get_name()} WINS THIS ROUND\n')
        self._score[winning_player.get_name()] += 1
        self.show_score()
            