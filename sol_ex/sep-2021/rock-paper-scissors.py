#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:26:55 2021

@author: gif
"""

import random
import time

print("""
      Rock-Paper-Scissors Game
      Please choose one of them
      
      1-Rock
      2-Paper
      3-Scissors
      4-Exit game
      
      Rules
      
      1-Rock beats scissors
      2-Scissors beats paper
      3-Paper beats rock
      
      Have Fun!
      
      """)

while True:
    
    user_1 = int(input("Your choose: "))
    
    if user_1 ==4:
        print("Game Over!")
        break
    elif user_1 >= 5:
        print("Please choose 1 to 4!")
        
    else:
        
        Game = {1:"Rock", 2:"Paper", 3:"Scissors"}
        
        AI_1 = random.randint(1,3)
        
        AI = Game.get(AI_1)
        user = Game.get(user_1)
        
        if user == "Rock" and AI =="Scissors":
            time.sleep(0.1)
            print("I choose scissors, You WIN!")
        
        elif user == "Rock" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, You Lose!")
            
        elif user == "Paper" and AI == "Scissors":
            time.sleep(0.1)
            print("I choose scissors, You LOSE!")
            
        elif user == "Paper" and AI == "Rock":
            time.sleep(0.1)
            print("I choose rock, You WIN!")
            
        elif user == "Scissors" and AI == "Paper":
            time.sleep(0.1)
            print("I choose paper, You WIN!")
            
        elif user == "Scissors" and AI == "Rock":
            time.sleep(0.1)
            print("I choose rock, You LOSE!")
            
        else:
            print("Draw, Please continue.")