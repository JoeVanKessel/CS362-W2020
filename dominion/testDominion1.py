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

for i in range(10):
    player_names.append("Too Many Players")


nV, nC = testUtility.InitnVnC(player_names)

box = testUtility.GetBoxes(nV)

#The supply always has these cards
supply, supply_order = testUtility.BuildSupply(player_names, nV, nC, box)

#Costruct the Player objects
#Bug: player objects are constructed for each letter in Annie
players = testUtility.BuildPlayers(player_names)

#Play the game
testUtility.PlayGame(supply, supply_order, players)

#Final score
testUtility.GetFinalScore(players)
