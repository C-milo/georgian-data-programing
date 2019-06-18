# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 15:11:49 2019

@author: C-milo and Nuthan
"""

'''
Create a deck of cards class. Internally, the deck of cards should use another class, a card class. Your requirements are:

The Deck class should have a deal method to deal two cards from the deck one for the user and one for the opponent (computer) 
After the cards are dealt, tell the user which one is bigger or if they are equal say WAR, then remove the cards from the deck.
There should be a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
'''
import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class Deck:
    # Defines cards in deck, uses Card class to construct an object with each possible card combination.
    def __init__(self):
        self.deck = list() #List of Card objects
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.deck_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
        
        for s in suits:
            for v in values:
                self.deck.append(Card(s, v))

    #Makes sure deck has all 52 cards and then rearranges them randomly.
    def shuffle(self): 
        self.deck = random.sample(self.deck, len(self.deck))
        
    #Deal two cards from the deck, one for the user and one for the opponent.
    #Tells which one is bigger or declares WAR, removes the cards from deck and gives a point to the winner.
    def deal(self):
        p1 = self.deck.pop(0)
        p2 = self.deck.pop(0)
        print(f'Player: {p1.value} {p1.suit}')
        print(f'Computer: {p2.value} {p2.suit}')
        if  self.deck_values[p1.value] > self.deck_values[p2.value]:
            print('Player 1 wins  this round +1  point')
            return 'p1'
        elif self.deck_values[p1.value] < self.deck_values[p2.value]:
            print('Computer wins  this round +1  point')
            return 'p2'
        else:
            print('WAR')            
            return 'WAR'

while True:
    input('Welcome, press any key to continue :')
    war = Deck()
    war.shuffle()
    player_points = 0    
    computer_points = 0
    game = str()
    
    while len(war.deck) > 0:
        points = war.deal()
        if points == 'p1':
            player_points += 1
        elif points == 'p2':
            computer_points += 1
        else:
            None
        input('Press any key to continue.')
    print('Player total points = ',   player_points)
    print('Computer total points = ',   computer_points)
    game = input('Do you want to play again? (Type Yes to continue else type anything.)')
    if game == 'Yes':
        continue
    else:
        break