#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 14:14:17 2023

@author: sharjeelshahid
"""

import random
import sys


ACE = 11
KING = 10
QUEEN = 10
JACK = 10
TEN = 10
NINE = 9
EIGHT = 8
SEVEN = 7
SIX = 6
FIVE = 5
FOUR = 4
THREE = 3
TWO = 2

deckofcards = {
  11 : 8,
  10 : 36,
  9 : 8,
  8: 8,
  7: 8,
  6: 8,
  5: 8,
  4: 8,
  3: 8,
  2: 8
}

dealerFirst = random.choice(list(deckofcards))
deckofcards[dealerFirst] -= 1

playerFirst = random.choice(list(deckofcards))
deckofcards[playerFirst] -= 1

dealerSecond = random.choice(list(deckofcards))
deckofcards[dealerSecond] -= 1

playerSecond = random.choice(list(deckofcards))
deckofcards[playerSecond] -= 1


print(f"Dealer draws {dealerFirst}")
print(f"Player draws {playerFirst}")
print(f"Player draws {playerSecond}")

def player_hits():
    playerHits = random.choice(list(deckofcards))
    deckofcards[playerHits] -= 1
    print(playerHits)
    return playerHits
    
    

playerChoice = input("Hit or Stand? ")
playerTotal = playerFirst + playerSecond
dealerTotal = dealerFirst + dealerSecond

while playerChoice == "Hit" and playerTotal < 22:
    playerTotal += player_hits()
    if playerTotal >= 22:
        break
    playerChoice = input("Hit or Stand? ")

    
if playerTotal > 21:
    print("Dealer Wins")
    sys.exit()
    

print(f"Dealer reveals {dealerSecond}")

while dealerTotal < 17:
    dealerTotal += player_hits()


if dealerTotal > 16 and dealerTotal < 22:
    if dealerTotal > playerTotal:
            print("Dealer Wins")
    elif dealerTotal == playerTotal:
        print("Draw")
    else:
        print("Player Wins")
else:
    print("Player Wins")
       
            
            
       
            
    
                 
        


