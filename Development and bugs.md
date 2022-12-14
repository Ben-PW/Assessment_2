# Development and bugs

This file contains information regarding the development process behind this code. It also details issues encountered and how they were solved, as well as any issues that I was unable to solve.

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
* [Issues and bugs](#issues)

<a name='process'></a>
### Development process

The development process used to create this code was a type of [iterative and incremental](https://outomated.com/types-of-software-development-life-cycle-models/) model, wherein each iteration of the code is intended to be a functioning package, and where each iteration represents a functional improvement over the last. One of the reasons for selecting this model was that I was initially unsure how to impliment some of the requirements of the code. Iterative development allowed me to begin with somewhat functional code and test which additions successfully integrated with the existing model. It also made identifying the sources of errors easier, as I could compare the altered code with the code I began with, narrowing down the sources of errors to new changes.

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

<a name='issues'></a>
### Issues and bugs

This section details current bugs or issues with the final version of the code

