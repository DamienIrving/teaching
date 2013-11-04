---
title: Python teaching material
---

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

**1. Introduction: Data Analysis** (python-intro.ipynb)
An introductory example of how to perform typical data analysis tasks in Python
* Topics: importing libraries/modules, calling functions/attributes (modules) or 
  methods/members (classes), reading and storing data, variable assignment, indexing 
  (including slice and stride), basic plotting (matplotlib), array operations

**2. Creating Functions** (python-functions.ipynb)
Functions allow you to write code in small re-usable chunks, which enhances code 
readability and reduces duplication.
* Topics: defining functions, call stack, doc strings, positional and keyword arguments 

**3. Analysing Multiple Datasets** (python-loops.ipynb)
   * *Topics:* loops (if, while)
   * *Main point:* get the computer to complete repetitive tasks for you
   * *Notebook:* python-loops.ipynb

**4. Making Choices**
   * *Topics:* RGB color schemes, lists, tuples, conditional statements
   * *Notebook:* python-conditionals.ipynb

**5. Testing and Defensive Programming**
   * *Topics:* unit testing, assertions
   * *Main point:* how, why, and when to test your code
   * *Notebook:* python-testing.ipynb

**6. Errors**
   * *Topics:* debugger tools,  
   * *Main point:*
   * *Notebook:* python-errors.ipynb

**7. Interacting with the Command Line**
   * *Topics:* sys.argv, argparse
   * *Main point:* write code that gives options at the command line, so you don't have to 
     continually manually edit your code (also aids documentation)
   * *Notebook:* python-cmdline.ipynb

**8. Number Crunching**
   * *Topics:* linear algebra, data types, matrix programming, floating point arithmetic
   * *Main point:* there are some things you to know when dealing with numbers... 
   * *Notebook:* python-numerical.ipynb