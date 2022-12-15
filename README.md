# Assessment_2
Repo for second assessment in Andy Turner's module

For information on development, failed implementations and current issues with code, see [Development and bugs](https://github.com/Ben-PW/Assessment_2/blob/main/Development%20and%20bugs.md)

## Table of contents
* [Introduction](#introduction)
* [Running the code](#run)
* [Description of repo contents](#contents)


<a name="introduction"></a>
### Introduction
The aim of this code is to generate a simulated environment containing a 'bacteria bomb'. This bomb is located on top of a building 75m in the air and, upon detonation, will release 5000 bacteria to drift down to the ground. This script generates the 5000 bacteria and simulates their movement as they descend through the atmosphere. It then stores their location and generates a heat map of where the various bacteria landed. The data represented by this heat map will also be saved as a text file. The final version of this code will function with any 300x300 raster style file with any values, as long as it contains 1 unique value amongst other, identical values. 

<a name='run'></a>
### Running the code
To run any of the functional versions of this code (all excluding verisions 1 and 7), simply download all of the files contained within the folder of the version you would like to run. Store these files in a common folder on your device. From there, run the file titled 'model[iteration number]', either through a Python IDE or directly via the command line. The model file will import the relevant files from the folder it is saved in and save the output as a text file entitled 'out.txt' in that same folder. 

<a name="contents"></a>
### Description of repo contents
This repo contains all the files for the second assessment of the programming for social scientists module. The final version of the code can be found in the 'Better_bomb_9' file. Versions of the code at each stage of development can be found in the relevant folders, formatted as '[code alteration]_[code iteration]' (i.e. 'Better_bomb_9' indicates that improving the 'bomb' class was the alteration made, and that this alteration resulted in the 9th iteration of the development process).
<a name='based'></a>
1. Base_code_1
    * bacteria_framework.py
    * model.py
<a name='behave'></a>
2. Behaviour_graph_2
    * bacteria_framework.py
    * model2.py
<a name='stahp'></a>
3. Stopping_cond_3
    * bacteria_framework3.py
    * model3.py
    * wind.RASTER
<a name='dense'></a>
4. Density_plot_4
    * bacteria_framework4.py
    * model4.py
    * wind.RASTER
<a name='read'></a>
5. Read_class_5
    * bacteria_framework5.py
    * model5.py
    * readwrite.py
    * wind.RASTER
<a name='input'></a>
6. Remove_input_req_6
    * bacteria_framework6.py
    * bomb.py
    * model6.py
    * readwrite.py
    * wind.RASTER
<a name='GUI'></a>
7. GUI_7f  
**NB** 'f' indicates failed attempt
    * bacteria_framework7.py
    * model7.py
    * model7_animation_attempt.py
    * model7_GUI_attempt.py
    * wind.RASTER
<a name='bomb'></a>
8. Bomb_class_8
    * bacteria_framework8.py
    * bomb.py
    * model8.py
    * readwrite.py
    * wind.RASTER
<a name='bomb2'></a>
9. Better_bomb_9
    * bacteria_framework8.py
    * bomb2.py
    * model9.py
    * wind.RASTER










