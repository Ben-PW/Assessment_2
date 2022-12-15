# Development and bugs

This file contains information regarding the testing and development process behind this code. It also details any issues with the final version of the code, as well as any failed attempts.
&nbsp;
## Table of contents

* [Development process](#process)
* [Development stages](#stages2)
    - [Base_code_1](#based2)
    - [Behaviour_graph_2](#behave2)
    - [Stopping_cond_3](#stahp2)
    - [Density_plot_4](#dense2)
    - [Read_class_5](#read2)
    - [Remove_input_req_6](#input2)
    - [GUI_7f](#GUI2)
    - [Bomb_class_8](#bomb2)
    - [Better_bomb_9](#bomb22)
* [Testing](#test)
* [Issues and bugs](#issues)
* [Failed implementations](#fails)
* [Future directions](#future)
&nbsp;
<a name='process'></a>
## Development process

The development process used to create this code was a type of [iterative and incremental](https://outomated.com/types-of-software-development-life-cycle-models/) model, wherein each iteration of the code is intended to be a functioning package, and where each iteration represents a functional improvement over the last. One of the reasons for selecting this model was that I was initially unsure how to impliment some of the requirements of the code. Iterative development allowed me to begin with somewhat functional code and test which additions successfully integrated with the existing model. It also made identifying the sources of errors easier, as I could compare the altered code with the code I began with, narrowing down the sources of errors to new changes.
&nbsp;
<a name='stages2'></a>
### Development stages
<a name='based2'></a>
1. Base_code_1
    * bacteria_framework.py: initial, non-functional, framework for bacteria class
    * model.py: initial code added to develop upon
<a name='behave2'></a>
2. Behaviour_graph_2
    * bacteria_framework.py: overall framework of behaviour developed, no stopping condition capeability
    * model2.py: initial code added to find bomb location, create agents, iterate behaviour and generate graph
<a name='stahp2'></a>
3. Stopping_cond_3
    * bacteria_framework3.py: functional code, stopping condition capeability added
    * model3.py: functional code, stopping condition added by appending landed bacteria to a set
    * wind.RASTER: csv file containing raster data with one unique value representing the bombing location
<a name='dense2'></a>
4. Density_plot_4
    * bacteria_framework4.py: agents alter environment when landing to permit plotting landing locations
    * model4.py: no significant changes
    * wind.RASTER
<a name='read2'></a>
5. Read_class_5
    * bacteria_framework5.py: no changes
    * model5.py: functions to read data in/out replaced with dedicated class
    * readwrite.py: code for class dedicated to reading data in and out
    * wind.RASTER
<a name='input2'></a>
6. Remove_input_req_6
    * bacteria_framework6.py: pass statement added to improve efficiency
    * bomb.py: initial code added for class to perform functions to find bomb (nonfunctional)
    * model6.py: alterations so that bomb finding functions are less specific to values in wind.RASTER
    * readwrite.py: no changes
    * wind.RASTER
<a name='GUI2'></a>
7. GUI_7f  
**NB** 'f' in filename indicates failed attempt
    * bacteria_framework7.py: no changes
    * model7.py: minor changes to improve efficiency in bacteria generation
    * model7_animation_attempt.py: non functional, detailed later
    * model7_GUI_attempt.py: non functional, detailed later
    * wind.RASTER
<a name='bomb2'></a>
8. Bomb_class_8
    * bacteria_framework8.py: no changes
    * bomb.py: bomb class now functional, documentation added
    * model8.py: minor changes
    * readwrite.py: no changes
    * wind.RASTER: 
<a name='bomb22'></a>
9. Better_bomb_9
    * bacteria_framework8.py: no changes
    * bomb2.py: bomb finding functions overhauled into one, generalisable function. readwrite and bomb classes combined into one class with useful functions for    script
    * model9.py: additional checks added for new function
&nbsp;
<a name='test'></a>
## Testing
Testing for bugs was primarily accomplished through print and count statements to ensure class methods were being implimented as intended. These may not be present in later versions of code as unchanged, previously tested code often had test statements removed to improve legibility. 

An example of this is that bacteria are coded to append +15 to their location when they land, rather than 1. This is due to the colour scaling employed by the matplotlib.pyplot call. Whilst, initially, it appeared that bacteria were not appending to the environment as there was no discernable difference in the rendered pyplot, this was actually due to the difference between the bomb location value (255) and the cumulative value of multiple bacteria landing in one location (e.g 15). I found this as the print statements indicated that the environment was being appended to, and applying the old (code iteration < 8) find_vals() function to the environment after the model had been run indicated that values in the array had indeed been changed. The plotting function did not actually render the colour change caused by the bacteria landing as the difference in numerical value was so large. This led to bacteria appending the environment by 15 when they landed. 

This was also how the changes < 2 restriction was applied to the find_bomb() method in the bomb2.Bomb class. Print statements indicated it was returning the index after the bomb location due to a flaw in the code.

Testing for efficiency was accomplished by implementing the time.time() method. Time was calculated before and after key functions to determine how long they were taking. 

This was very useful in reducing the time required to simulate the bacteria movements from roughly 25 seconds down to < 10. This was accomplished by simply adding an 
```
else:
    pass
```
statement at the end of bacteria_framework6.py, which allowed the loop to skip a large amount of needless computation. 
&nbsp;
<a name='issues'></a>
## Issues and bugs


This section details current bugs or issues with the final version of the code. The first section if the title indicates the code or criteria causing the bug, the second section indicates the file it applies to. Note the bugs detailed here will only be those remaining in the 9th iteration, as this is the version of the code intended to be used. 


**Bomb location = Environment[0][0]: Better_bomb_9, bomb2.py**


This issue only applies if the unique value representing the bomb (within the 2D array representing the environment) is the first value within the first list checked by the code. This is due to how the find_bomb() method within the bomb class locates the unique value; find_bomb() loops through the array checking that each value is the same as the last. When a change is detected, the loop returns the index of the point causing the change. This is done by limiting the loop to run only whilst the number of changes detected is less than 2. 

This means that, if the unique value was the very first value checked by the loop, it would not return Environment[0][0] as the index, but rather Environment[0][1], as this was the point at which the value 'changed' as far as the find_bomb() method is concerned. This issue could potentially be solved by calling a count method each time a new value was detected, and then selecting the value with the lowest count at the end of the loop, however due to time constraints I wasn't able to implement this


**Multiple bomb locations: Better_bomb_9, bomb2.py**

This issue applies if more than one unique value is present within the 2D array. The current find_bomb() will return the first unique value found and terminate at that point. 

The code for find_bomb() is included below for reference (documentation omitted):

```Ruby
def find_bomb(self):
        
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
    
    
```
&nbsp;
<a name='fails'></a>
## Failed implementations

**Implementing a GUI and animation**

I attempted to implement a GUI using Tkinter (see iteration 7 folder). I intended to animate the environment as it was appended to by the bacteria, allowing the user to watch as the denisty plot was constructed. Unfortunately, for 'model7_animation_attempt.py' this animation runs without being tied to the run function. Additionally, the animation attempts to display the bacteria, which is not informative due to their density being the variable of interest. 

In the GUI attempt (model7_GUI_attempt.py), the GUI appeared to work insofar that the running of the model was tied to interacting with the GUI. However, the ouput was not rendered in the GUI.

One complication in doing this was that this project was performed over two different devices. Potentially due to hardware limitations on the first device, when these implementations were first attempted, the code would not run and gave errors. This could be related to forum posts on stackoverflow indicating that the error messages my code was giving may have been related to [memory issues](https://stackoverflow.com/questions/73892881/error-fail-to-create-pixmap-with-tk-getpixmap-in-tkimgphotoinstancesetsize-wh). Forum users recommended switching from the 'TkAgg' backend to the 'Agg' backend, however this led to further issues which I was unable to solve on the old device. The second device I used did not have these limitations and managed to actually run the code in iteration 7 without giving errors, however I only discovered this at the final stage of this project, as I gained access to the new device after I had already marked iteration 7 as a failed implementation. 

Given more time, I would have liked to work out the issues with the GUI and animation implementation, however this was not feasible in the time frame left to me.
&nbsp;
<a name='future'></a>
## Future directions

**GUI**  
I would like to have properly implemented a GUI for this project. I believe the main issue with my code for this in the iteration 7 folder was that I could not find a way to set the plot of the environment as the canvas for the Tkinter GUI (see [this stack overflow thread](https://stackoverflow.com/questions/25498937/embed-a-pyplot-in-a-tkinter-window-and-update-it) for a someone witha similar question), and have it update with each stage of the model. Solving this would have hopefully allowed me to animate the model and allow the user to interact that way. 

**Automatic plot scaling**  
Another aspect of the code I was interested in was to create a function that would calculate the appropriate matplotlib.pyplot x and y axes. The idea behind this was, if the find_bomb() method could determine the unique point automatically, then the numerical value of the surrounding, non-unique points could also be stored. After iterating the behaviour of the bacteria in the script, a function could be written to calculate the spread of the agents, id est find the list with the earliest appended value and find the index within the list of said value (min x coordinate), doing the same for the list with the furthest appended value (max x coordinate). Then, finding which lists within the array were the first and last to have altered values within them would give maximum and minimum y values. 

My aim here was that these values could be caclulated automatically and passed into the matplotlib.pyplot call, meaning that the rendered graph could be automatically fitted to any size of array and match agents that move a lot or move very little. This would also require changing the code in the bacteria_framework8.py file, as the agents are currently specified to an environment of 300x300 (see below):

```Ruby
if self.height > 0: # If height is above zero

            if random.random() <= 0.1: # 10% chance to move North
    
                self.y = (self.y + 1) % 300
    
                #print('y+1')
    
            elif random.random() > 0.1 and random.random() <= 0.2: # 10% chance to move South
    
                self.y = (self.y - 1) % 300
    
                #print('y-1')
```

however I'm sure this could be achieved by altering this to read something like:

```Ruby
len1 = len(environment[0]) # max y of environment
len2 = len(environment[0][0]) # max x of environment assuming all lists are equal length

if self.height > 0: # If height is above zero

            if random.random() <= 0.1: # 10% chance to move North
    
                self.y = (self.y + 1) % len1 # then do the same for x with len2
    
                #print('y+1')
```

This last section wasn't implemented in the final code as it wasn't necessary, however I would be very interested in seeing if I could find a way to work the automatic plot scaling idea.  

