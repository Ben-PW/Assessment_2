# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 16:41:23 2022

@author: u48730bp
"""
import csv

class Bomb:
    
    """
    Designed to help with tasks in assessment, reads data in and out as well as
    finding index of unique value. 
    
    ...
    
    Attributes
    -------
    environment : arr
        a 2D array representing the environment the agents move inside
        
    a : txt
        a text file in csv format containing raster data (300x300) to generate
        the environment
    
    Methods
    -------
    
    find_bomb() 
        returns index (coordinates) of unique value
        
    readin()
        reads RASTER data into 2D array (environment)
        
    readout()
        converts environment back into RASTER data file
        
    """
    
    def __init__(self, a, environment):
        
        self.a = a # RASTER file 
        
        self.environment = environment # Environment list
        
        
        
    def find_bomb(self):
        
        """
        Method of 'Bomb' class
        
        Iterates over values in array and returns index of unique value
        Bacteria will be generated from this point
        
        Will locate any unique numerical value, however if array contains multiple it 
        will only return the first. Additinally, if intended bomb location is at
        environment[0][0], this method will instead return environment[0][1]. This
        issue is unique to bomb locations of environment[0][0].
        
        -------
        No parameters, acts on environment as attribute of class
        
        -------
        Returns index of bomb location
        
        """
        
        # Search for unique value
        bomb_value = None # Create empty value
        bomb_index = None # Create empty value
        changes = 0
          
        for i in range(len(self.environment)): # Iterate over lists
          
              
          for j in range(len(self.environment[i])): # Iterate within lists
                
                
            if self.environment[i][j] != bomb_value and changes < 2:  
                # If n(changes) is not restricted, function will return
                # bomb_index[i][j+1]
                                                     
                    bomb_value = self.environment[i][j] # Current value = bomb
                    bomb_index = (i, j) # Index of current value = index of bomb
                    changes = (changes + 1)
                
        return bomb_index # Return index of bomb
    
  
    
  
    def readin(self):
        
        """
        Method of 'Bomb' class
        
        Reads 'a' RASTER data into 'environment' array
        
        -------
        No parameters, acts on 'a' and 'environment' as attributes of class
        using csv.reader
        """

        txt = open(self.a, newline = '') 
        
        reader = csv.reader(txt, quoting = csv.QUOTE_NONNUMERIC) # Create csv reader class
        
        for row in reader:
        
            rowlist = [] # define each row in data as a list
        
            for value in row:
        
                rowlist.append(value) # append each value in the row to the list
        
            self.environment.append(rowlist) # append each list of values to the environment list
        
        txt.close() # Close file
        
        
        
    def readout(self):
        
        """
        Method of 'Bomb' class
        
        Converts environment data into txt file 
        
        -------
        No parameters, acts on 'environment' as attribute of class
        using csv.writer
        """
        
        with open('out.txt', 'w', newline='') as f:
        
            writer = csv.writer(f, delimiter=',') # writer = csv.writer class
            
            for row in self.environment:
                
                writer.writerow(row) # write csv row for each list of data in env
        
