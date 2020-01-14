# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 20:12:00 2020

@author: Joseph Van Kessel
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = ["Annie","*Ben","*Carla"]
##
#BUG: Number of victory card and curse cards have been swithched
#only 12 curse cards and 20 of each victory card
##
nC, nV = testUtility.InitnVnC(player_names)

box = testUtility.GetBoxes(nV)

#The supply always has these cards
supply, supply_order = testUtility.BuildSupply(player_names, nV, nC, box)

#Costruct the Player objects
players = testUtility.BuildPlayers(player_names)

#Play the game
testUtility.PlayGame(supply, supply_order, players)

#Final score
testUtility.GetFinalScore(players)
