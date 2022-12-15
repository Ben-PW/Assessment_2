# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:06:27 2022

@author: u48730bp
"""
#import model8

class Bombsquad:
    
    """
    Class used to find unique bomb value and location of value
    
    ...
    
    Attributes
    -------
    env : arr
        a 2D array representing the environment the agents move inside
        
    new : list
        a list containing the numeric value of the bomb location
    
    vals : dict
        dictionary containing the values found in env
    
    Methods
    -------
    find_value()
        searches all values in env and returns unique value
    
    find_bomb()
        returns index (coordinates) of unique value
    """
    
    def __init__(self, environment, new):
        
        self.environment = environment
        
        self.vals = {}
        
        self.new = new
        
        
    def find_value (self):
        
        """ Searches array for odd value out, stoes unique value in 'new' list
        
        Parameters
        -------
        vals : 
        """
        
        for rowlist in self.environment:
        
            for i in rowlist:
        
                if i not in self.vals: # If integer not detected in self.vals dictionary
        
                    self.vals[i] = 0 # set the recorded number of the vals to zero
        
                self.vals[i] += 1 # Otherwise, add 1 to the existing value
        
                for new_val in self.vals: 
                    
                    if new_val > 0: # find_vals() shows all other values in environment are 0, ideally change to be less data specific

                        self.new.append(new_val) # Add the value to the 'new' list
                        
                        
    
    def find_bomb (self):
        
        for i, x in enumerate(self.environment):

            if self.new[0] in x: # if first value in 'new' is found in a row of environment

                return (i, x.index(self.new[0])) # return the index of that value