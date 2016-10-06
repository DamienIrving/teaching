# Debugging and Profiling

## The Python Debugger

To debug from the point an error occurs:  
`$ python -m pdb myscript.py`

To debug from a particular point in the script:
* Import the debugger in your script: `import pdb`
* Set a tracer in your script: `pdb.set_trace()`
* Run script and it will stop at the tracer:
  * `n`: next command, not stepping into sub-functions
  * `s`: next command, stepping into sub-functions
  * `c`: continue running script
  
## Time profiling

Install:  
`$ conda install line_profiler`

Add a decorator in your script before the function you want to profile:
```
@profile
def my_function(data):
    ...
    return result
```

Run from the command line:  
`$ kernprof -l -v myscript.py`  

`-l`: recognise the `@profile` decorator in your script  
`-v`: display timing information once the script has finished

## Memory profiling

Install:  
`$ conda install memory_profiler`

Add a decorator in your script before the function you want to profile:
```
@profile
def my_function(data):
    ...
    return result
```

Run from the command line:  
`$ python -m memory_profiler my_script.py`





