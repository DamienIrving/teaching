## Workshop outline

Task: Write a command line program that plots the precipitation climatology for a selected month of the year. It must be able to handle any arbitrary CMIP5 data file and the user must have the option to apply a land or ocean mask.

#### 0. Tour of the stack

i.e. What libraries are we going to use for the task? [This post](https://drclimate.wordpress.com/2016/10/04/the-weatherclimate-python-stack/) summarises the stack.

#### 1. Install libraries using conda

See [conda.md](https://github.com/DamienIrving/teaching/blob/master/amos-icshmo/conda.md)

#### 2. Interacting with Python

Brief walk through Python at the command line, ipython at the command line, popular IDE's (e.g. Spyder) and finally the Jupyter notebook.

#### 3. Visualising CMIP data

See [visualising_cmip_data.ipynb](https://github.com/DamienIrving/teaching/blob/master/amos-icshmo/visualising_cmip_data.ipynb)

#### 4. Functions / modular code

See [functions.ipynb](https://github.com/DamienIrving/teaching/blob/master/amos-icshmo/functions.ipynb)

#### 5. Command line programs

Starting from a template script, put the code in and get it running.  
Challenge: add some minor custom options (tick levels, palette, gridlines, advanced: projection).  
(Introduce pdb along the way.)  
See [command_line_programs.md](https://github.com/DamienIrving/teaching/blob/master/amos-icshmo/command_line_programs.md).  

#### 6. Version control with git

Create repo.  
Track a minor cosmetic changes to the code (e.g. improved docstring).  

#### 7. Vectorisation

Introduce how to create and apply the mask.  
Challenge: Get them to add that functionality into the script. Commit/push to git/GitHub once it's working. 
See [vectorisation.ipynb](https://github.com/DamienIrving/teaching/blob/master/amos-icshmo/vectorisation.ipynb)

#### 8. Testing and defensive programming

Add assertions to script. Commit/push to git/GitHub once you're done.   
(do [SWC assertions example](http://swcarpentry.github.io/python-novice-inflammation/08-defensive/) first if there's time).

#### 9. Data provenace

Create timestamp functions.  
Put them in a separate module and import them.  
Add those module files to git/GitHub.  
