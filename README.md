# Assessment_2
Repo for second assessment in Andy Turner's module

## Table of contents
* [Introduction](#introduction)
* [Description of contents](#contents)
    - [Base_code_1](#based)
    - [Behaviour_graph_2](#behave)
    - [Stopping_cond_3](#stahp)
    - [Density_plot_4](#dense)
    - [Read_class_5](#read)
    - [Remove_input_req_6](#input)
    - [GUI_7f](#GUI)
    - [Bomb_class_8](#bomb)
    - [Better_bomb_9](#bomb2)

<a name="introduction"></a>
### Introduction
The aim of this code is to generate a simulated environment containing a 'bacteria bomb'. This bomb is located on top of a building 75m in the air and, upon detonation, will release 5000 bacteria to drift down to the ground. This script generates the 5000 bacteria and simulates their movement as they descend through the atmosphere. It then stores their location and generates a heat map of where the various bacteria landed. The data represented by this heat map will also be saved as a text file. The final version of this code will function with any 300x300 raster style file, as long as it contains 1 unique value amongst other, identical values. 


<a name="contents"></a>
### Description of contents
This repo contains all the files for the second assessment of the programming for social scientists module. The final version of the code can be found in the 'Better_bomb_9' file. Versions of the code at each stage of development can be found in the relevant folders, formatted as '[code alteration]_[code iteration]' (i.e. 'Better_bomb_9' indicates that improving the 'bomb' class was the alteration made, and that this alteration resulted in the 9th iteration of the development process).
<a name='based'></a>
1. Base_code_1
    * bacteria_framework.py: initial, non-functional, framework for bacteria class
    * model.py: initial code added to develop upon
<a name='behave'></a>
2. Behaviour_graph_2
    * bacteria_framework.py: overall framework of behaviour developed, no stopping condition capeability
    * model2.py: code added to find bomb location, create agents, iterate behaviour and generate graph
<a name='stahp'></a>
3. Stopping_cond_3
    * bacteria_framework3.py: functional code, stopping condition capeability added
    * model3.py: functional code, stopping condition added by appending landed bacteria to a set
    * wind.RASTER: csv file containing raster data with one unique value representing the bombing location
<a name='dense'></a>
4. Density_plot_4
    * bacteria_framework4.py: agents alter environment when landing to permit plotting landing locations
    * model4.py: no significant changes
    * wind.RASTER
<a name='read'></a>
5. Read_class_5
    * bacteria_framework5.py: no changes
    * model5.py: functions to read data in/out replaced with dedicated class
    * readwrite.py: code for class dedicated to reading data in and out
    * wind.RASTER
<a name='input'></a>
6. Remove_input_req_6
    * bacteria_framework6.py: pass statement added to improve efficiency
    * bomb.py: initial code added for class to perform functions to find bomb (nonfunctional)
    * model6.py: alterations so that bomb finding functions are less specific to values in wind.RASTER
    * readwrite.py: no changes
    * wind.RASTER
<a name='GUI'></a>
7. GUI_7f  
**NB** 'f' in filename indicates failed attempt
    * bacteria_framework7.py: no changes
    * model7.py: minor changes to improve efficiency in bacteria generation
    * model7_animation_attempt.py: non functional, detailed later
    * model7_GUI_attempt.py: non functional, detailed later
    * wind.RASTER
<a name='bomb'></a>
8. Bomb_class_8
    * bacteria_framework8.py: no changes
    * bomb.py: bomb class now functional, documentation added
    * model8.py: minor changes
    * readwrite.py: no changes
    * wind.RASTER: 
<a name='bomb2'></a>
9. Better_bomb_9
    * bacteria_framework8.py: no changes
    * bomb2.py: bomb finding functions overhauled into one, generalisable function. readwrite and bomb classes combined into one class with useful functions for    script
    * model9.py: additional checks added for new function



