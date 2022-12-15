# Assessment_2
Repo for second assessment in Andy Turner's module

For information on development, failed implementations and current issues with code, see [Development and bugs](https://github.com/Ben-PW/Assessment_2/blob/main/Development%20and%20bugs.md)

## Table of contents
* [Introduction](#introduction)
* [Running the code](#run)
* [Description of repo contents](#contents)
* [License](#license)
* [Sources](#source)


<a name="introduction"></a>
### Introduction
The aim of this code is to generate a simulated environment containing a 'bacteria bomb'. This bomb is located on top of a building 75m in the air and, upon detonation, will release 5000 bacteria to drift down to the ground. This script generates the 5000 bacteria and simulates their movement as they descend through the atmosphere. It then stores their location and generates a heat map of where the various bacteria landed. The data represented by this heat map will also be saved as a text file. The final version of this code will function with any 300x300 raster style file with any values, as long as it contains 1 unique value amongst other, identical values. 

<a name='run'></a>
### Running the code
To run any of the functional versions of this code (all excluding verisions 1 and 7), simply download all of the files contained within the folder of the version you would like to run. Store these files in a common folder on your device. From there, run the file titled 'model[iteration number]', either through a Python IDE or directly via the command line. The model file will import the relevant files from the folder it is saved in and save the output as a text file entitled 'out.txt' in that same folder. You could also use your own raster file! As long as the file contains duplicates of the same value with one 'odd one out', the code will treat the odd value as the bomb location. Please note, however, that the plotting functions are built around the current source data, so adjusting the plot x and y axes may be required oif you use your own. 

<a name="contents"></a>
### Description of repo contents
This repo contains all the files for the second assessment of the programming for social scientists module. The final version of the code can be found in the 'Better_bomb_9' file. Versions of the code at each stage of development can be found in the relevant folders, formatted as '[code alteration]_[code iteration]' (i.e. 'Better_bomb_9' indicates that improving the 'bomb' class was the alteration made, and that this alteration resulted in the 9th iteration of the development process).

For a more detailed description of the contents of each folder, please see [here](https://github.com/Ben-PW/Assessment_2/blob/main/Development%20and%20bugs.md)
<a name='based'></a>
1. Base_code_1: initial code framework, non functional
    * bacteria_framework.py
    * model.py
<a name='behave'></a>
2. Behaviour_graph_2: updated, still non functional
    * bacteria_framework.py
    * model2.py
<a name='stahp'></a>
3. Stopping_cond_3: functional code, no density plot
    * bacteria_framework3.py
    * model3.py
    * wind.RASTER
<a name='dense'></a>
4. Density_plot_4: added density plot capeability
    * bacteria_framework4.py
    * model4.py
    * wind.RASTER
<a name='read'></a>
5. Read_class_5: designated class for reading data in and out
    * bacteria_framework5.py
    * model5.py
    * readwrite.py
    * wind.RASTER
<a name='input'></a>
6. Remove_input_req_6: bomb finding functions made more flexible to data
    * bacteria_framework6.py
    * bomb.py
    * model6.py
    * readwrite.py
    * wind.RASTER
<a name='GUI'></a>
7. GUI_7f: failed implementations
**NB** 'f' indicates failed attempt
    * bacteria_framework7.py
    * model7.py
    * model7_animation_attempt.py
    * model7_GUI_attempt.py
    * wind.RASTER
<a name='bomb'></a>
8. Bomb_class_8: class created for bomb finding functions
    * bacteria_framework8.py
    * bomb.py
    * model8.py
    * readwrite.py
    * wind.RASTER
<a name='bomb2'></a>
9. Better_bomb_9: bomb finding functions overhauled, 'read' class combined
    * bacteria_framework8.py
    * bomb2.py
    * model9.py
    * wind.RASTER
&nbsp;
<a name='license'></a>
### License

This repo and the code within it are licensed under an [MIT](https://en.wikipedia.org/wiki/MIT_License) or 'Expat License' with the following terms:  
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


&nbsp;
<a name='source'></a>
### Sources

General issues with code: [stackoverflow](https://stackoverflow.com/)  
Guidance on properly documenting code: [realpython](https://realpython.com/documenting-python-code/#commenting-vs-documenting-code)  
Attempting to implement Tkinter: [tkdocs](https://tkdocs.com/tutorial/canvas.html)  
ReadMe guidance: [freecodecamp](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)








