# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:44 2022

@author: u48730bp
"""

############################### BACTERIA FRAMEWORK

import random

 

class Bacteria():
    
    """
    Class built to represent bacteria from brief, allows them vertical and 
    horizontal movement as well as storing the location of their landing and 
    the number of bacteria that have landed.
    
    ...
    
    Attributes
    -------
    
    environment : arr
        a 2D array representing the environment the agents move inside
    
    x : int
        integer representing x coordinate of bomb location
    
    y : int
        integer representing y coordinate of bomb location
    
    i : int
        integer representing number of individual agent (1 : len(num_bacteria))
    
    landed : list
        list containing 'i' of all landed bacteria
    
    height : int
        integer representing height of agent (default = 75)
    
    Methods
    -------
    
    Move()
        Bacteria may move 1m North (10% chance), East (75% chance), South (10%
        chance) or West (5% chance)
    
    Risefall()
        When height is greater than 75m, move 1m higher (20% chance), remain
        level (10% chance), or fall (70% chance)
        When height is less than 75m, fall 1m (100% chance)
        
    """

    def __init__(self, environment, x, y, i, landed):

        self.x = x

        self.y = y

        self.environment = environment

        self.height = 75
        
        self.i = i
        
        self.landed = landed

       

    def move(self):
        
        """
        Method of 'Bacteria' class
        
        Bacteria may move 1m North (10% chance), East (75% chance), South (10%
        chance) or West (5% chance)
        
        -------
        No parameters, acts upon x, y and environment as attributes of the 
        'Bacteria' class, increases/reduces self.x and self.y according to 
        random.random() outcome
        """
        
        if self.height > 0: # If height is above zero

        #rand = random.random()

            if random.random() <= 0.1: # 10% chance to move North
    
                self.y = (self.y + 1) % 300
    
                #print('y+1')
    
            elif random.random() > 0.1 and random.random() <= 0.2: # 10% chance to move South
    
                self.y = (self.y - 1) % 300
    
                #print('y-1')
    
            elif random.random() > 0.2 and random.random() <= 0.95: # 75% chance to move East
    
                self.x = (self.x + 1) % 300
    
                #print('x+1')
    
            else:
    
                self.x = (self.x - 1) % 300 # 5% chance to move West
    
                #print('x-1')

        else:
            pass # If height not above zero, don't move

                

    def risefall(self):
        
        """
        Method of 'Bacteria' class
        
        When height is greater than 75m, move 1m higher (20% chance), remain
        level (10% chance), or fall (70% chance)
        When height is less than 75m, fall 1m (100% chance)
        
        When height reaches 0, bacteria instance is added to 'landed' list and
        cannot move or fall any further. The numerical value of the integer
        representing the location (self.environment[self.x][self.y]) is increased, 
        allowing plotting of density
        
        -------
        No parameters, acts upon self.height, self.environment and self.landed
        as attributes of class
        """

        if self.height > 0: # If height of bacteria is above ground

            if self.height >= 75: # If height is equal/greater than 75

                if random.random() <= 0.2: # 20% chance to increase height

                    self.height = (self.height + 1)
                    #print('rising')

                elif random.random() > 0.2 and random.random() <= 0.3: # 10% chance to stay level
                    #print('level')
                    pass

                else:

                    self.height = (self.height - 1) # Otherwise height will reduce by 1
                    #print('falling (75+)')

            else:

                    self.height = (self.height - 1) # If height is sub 75, reduce height by 1
                    #print('falling (75-')

        else:

            seen = set(self.landed) # If height is not greater than 0, add to list of landed bacteria
            
            if self.i not in seen:

                self.landed.append(self.i) # Only add to landed list if it is not already in the list
                
                self.environment[self.y][self.x] += 15 # New arrivals add to local value, 15 selected as seems to visualise well
                #print('storing location')
            
            else:
                pass

            #print('Bacteria landed')
