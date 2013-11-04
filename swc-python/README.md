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

**1. Introduction to Data Analysis** (python-intro.ipynb) 

An introductory example of how to perform typical data analysis tasks in Python. 
* Topics: importing libraries/modules, calling functions/attributes (modules) or 
  methods/members (classes), reading and storing data, variable assignment, indexing 
  (including slice and stride), basic plotting, array operations
  
  
**2. Creating Functions** (python-functions.ipynb) 

Use functions to make code easier to re-use and easier to understand. 
* Topics: defining functions, the call stack, doc strings, positional and keyword 
  arguments 
  
  
**3. Analysing Multiple Datasets** (python-loops.ipynb) 

Use lists and arrays to store related values, and loops to repeat operations on them.
* Topics: loops, lists
  
  
**4. Making Choices** (python-conditionals.ipynb) 

Have programs make choices based on the values they are manipulating. 
* Topics: RGB color schemes, tuples, conditional statements
  
  
**5. Testing and Defensive Programming** (python-testing.ipynb) 

The how, why and when of testing your code and programming defensively. 
* Topics: unit testing, assertions
  
  
**6. Errors** (python-errors.ipynb) 

* Topics: debugger tools,  
  
  
**7. Interacting with the Command Line** (python-cmdline.ipynb) 

Write code that allows the user to specify options at the command line, so you don't have 
to manually edit your code every time you want to make a minor change.
* Topics: parsing the command line, help documentation
  
  
**8. Number Crunching** (python-numerical.ipynb) 

Tips to speed up your code and avoid bugs when dealing with numbers. 
* Topics: linear algebra, numerical data types, matrix programming, floating point 
  arithmetic