# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:42:26 2022

@author: u48730bp
"""

########################## MODEL

import matplotlib.pyplot

import bacteria_framework8

import time

import bomb2

######################### Create classes


a = 'wind.raster' # Define as 'a' to pass to class
environment = [] # Will contain data representing environment

# Helper has methods to read/write environment and find bomb location
helper = bomb2.Bomb(a, environment)


######################### Load environment

t1 = time.time()

helper.readin() # Reads raster data (a) into 'environment

t2 = time.time()

print('Environment loaded, time elapsed : ', round(t2-t1,3))


######################### Create agents

num_bacteria = 5000

bacteria = [] # create list to store generated agents

landed = [] # create list to store number of landed bacteria

y = helper.find_bomb()[0] # access first value of bomb index (y coordinate of bomb)
x = helper.find_bomb()[1] # access second value of bomb index (x coordinate of bomb)
                        # assign now instead of having to iterate loop num_bacteria times

t4 = time.time()
print('Bomb location found at (y=',helper.find_bomb()[0],'x=',helper.find_bomb()[1],').',
      'Time elapsed : ', round(t4-t2,3))   


for i in range(num_bacteria): # append required values to the bacteria class instances

    bacteria.append(bacteria_framework8.Bacteria(environment, x, y, i, landed))


t5 = time.time()
print(num_bacteria, 'bacteria generated, time elapsed : ', round(t5-t4,3))

 

################################ Iterate behaviour

 
while len(landed) < num_bacteria: # Don't stop model until all bacteria have landed
    
    for i in range(num_bacteria): 
    
           
        bacteria[i].move() # Iterate horizontal movement
    
        bacteria[i].risefall() # Vertical movement and landing


t6 = time.time()
print('Movement simulated, time elapsed : ', round(t6-t5,3))



#################### Create density plot

matplotlib.pyplot.xlim(40, 120)

matplotlib.pyplot.ylim(120, 200)

matplotlib.pyplot.imshow(environment)

matplotlib.pyplot.show()


t7 = time.time()
print('Plotting complete, time elapsed : ', round(t7-t6,3))
print('Total time elapsed : ', round(t7-t1,3))


helper.readout() # Create export environment
