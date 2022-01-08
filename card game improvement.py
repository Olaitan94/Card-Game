# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:46:41 2020

@author: Ibironke
"""

    
class card(object):
    
    def __init__(self):
        self.suits = ['clubs','diamonds','hearts','spades']
        self.ranks = ['Ace',2,3,4,5,6,7,8,9,10,'Jack','Queen','King']
        self.deck = deck = [[i,j] for i in self.ranks for j in self.suits]
    
    def display_deck(self):
        for char in self.deck:
            print (f'{char[0]} of {char[1]}')
            
    def draw_(self,deck,list):
        from random import choice
        self = choice(deck)
        deck.remove(self)
        return self
        
        
    def play_cards(self):
        plays = []    #This list will contain all the different cards drawn. new card drawn will be compared to the last card in the list. if same rank or suit, player has worn
        cont = input('press 0 to end game or any other to continue:')    #This is for termination of the game.
        x = True
        while x is True and cont != '0':
            ready = input('press enter to play as player 1:') 
            player1 = self.draw_(self.deck,plays)
            print(f'{player1[0]} of {player1[1]}.')
            if len(plays) == 0:
                plays.append(player1)
            elif player1[0] == plays[-1][0] or player1[1] == plays[-1][1] or player1 == plays[-1]:
                plays.append(player1)
                print(f'player1 has won! Congratulations.')
                x = False
                break
            else:
                plays.append(player1)
            ready2 = input('press enter to play as player 2:')
            player2 = self.draw_(self.deck,plays)
            print(f'{player2[0]} of {player2[1]}.')
            if player2[0] == plays[-1][0] or player2[1] == plays[-1][1] or player2 == plays[-1]:
                plays.append(player2)
                print('Player2 has won. Congratulations.')
                x = False
                break
            else:
                plays.append(player2)
            cont = input('press 0 to end game or any other to continue:')
        print('Game Over!')



#improvements: try to create a player class and use this store player names and all    
#what if the list is empty and no winner?
card1 = card()
list = []
print(card1.draw_(card1.deck,list))
print(card1.deck)
