Python teaching content
=======================

This directory contains the Python related content that I teach to novice (or beginner 
level) users at Software Carpentry bootcamps. The best way to learn how to program is to 
do something useful, so this introduction to Python is built around a common scientific 
task: data analysis.

Our real goal isn't to teach you Python, but to teach you the basic concepts that all 
programming depends on. We use Python in our lessons because:

1.  we have to use *something* for examples;
2.  it's free, well-documented, and runs almost everywhere;
3.  it has a large (and growing) user base among scientists; and
4.  experience shows that it's easier for novices to pick up than most other languages.

Each lesson is saved as a separate IPython notebook. To download and view them,
first clone my teaching repository,

    git clone https://github.com/DamienIrving/teaching.git

then navigate to this directory and fire up the IPython notebook:

    cd teaching/swc-python/
    ipython notebook &


Lessons
-------

### 1. Introduction to Data Analysis

An introductory example of how to perform typical data analysis tasks in Python. (python-intro.ipynb)

*Topics:* importing libraries/modules, calling functions/attributes (modules) or 
methods/members (classes), reading and storing data, variable assignment, indexing 
(including slice and stride), basic plotting, array operations
  
  
### 2. Creating Functions

Use functions to make code easier to re-use and easier to understand. (python-functions.ipynb) 

*Topics:* defining functions, the call stack, doc strings, positional and keyword arguments 
  

### 3. Analysing Multiple Datasets

Use lists and arrays to store related values, and loops to repeat operations on them. (python-loops.ipynb)

*Topics:* loops, lists
  

### 4. Making Choices 

Have programs make choices based on the values they are manipulating. (python-conditionals.ipynb) 

*Topics:* RGB color schemes, tuples, conditional statements
  

### 5. Testing and Defensive Programming

Know the how, why and when of testing your code and programming defensively. (python-testing.ipynb)

*Topics:* unit testing, assertions
  

### 6. Errors

(python-errors.ipynb)

*Topics:* debugger tools  
  

### 7. Interacting with the Command Line

Write code that allows the user to specify options at the command line, so you don't have 
to manually edit your code every time you want to make a minor change. (python-cmdline.ipynb)

*Topics:* parsing the command line, help documentation
  

### 8. Number Crunching 

Make use of libraries that have been optimised to handle large numeric arrays quickly and reliably.
Be aware of the issues associated with floating point arithmetic. (python-numerical.ipynb)

*Topics:* linear algebra, numerical data types, matrix programming, floating point arithmetic
