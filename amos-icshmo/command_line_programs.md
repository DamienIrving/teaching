# Command line programs

We've arrived at the point where we have successfully defined the functions
required to plot the precipitation data.

We could continue to execute these functions from the Jupyter notebook,
but in most cases notebooks are simply used to try things out
and/or take notes on a new data analysis task.
Once you've scoped out the task
(as we have for plotting the precipitation climatology),
that code can be transferred to a Python script
so that it can be executed at the command line.
It's likely that your data processing workflows will include
command line utilities from the CDO and NCO projects in addition to Python code,
so the command line is the natural place to manage your workflows
(e.g. using shell scripts or make files).

In general, the first thing that gets added to any Python script is the following:

```
if __name__ == '__main__':
    main()
```

The reason we need these two lines of code
is that running a Python script in bash is very similar to importing that file in Python. 
The biggest difference is that we don’t expect anything to happen when we import a file, 
whereas when running a script we expect to see some output
(e.g. an output file, figure and/or some text printed to the screen).

The `__name__` variable exists to handle these two situations.
When you import a Python file `__name__` is set to the name of that file
(e.g. when importing script.py, `__name__` is `script`),
but when running a script in bash `__name__` is always set to `__main__`.
The convention is to call the function that produces the output `main()`,
but you can call it whatever you like.

The next thing you'll need is a library to parse the command line for input arguments.
The most widely used option is 
[argparse](https://docs.python.org/3/library/argparse.html): 

```
$ cat script_template.py

import argparse

#
# All your functions (that will be called by main()) go here.
#

def main(inargs):
    """Run the program."""

    print('Input file: ', inargs.infile)
    print('Output file: ', inargs.outfile)


if __name__ == '__main__':

    description='Print the input arguments to the screen.'
    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("outfile", type=str, help="Output file name")

    args = parser.parse_args()            
    main(args)
```

By running `script_template.py` at the command line
we'll see that argparse handles all the input arguments:

```
$ python script_template.py in.nc out.nc
Input file:  in.nc
Output file:  out.nc
```

It also generates help information for the user:

```
$ python script_template.py -h
usage: script_template.py [-h] infile outfile

Print the input arguments to the screen.

positional arguments:
  infile      Input file name
  outfile     Output file name

optional arguments:
  -h, --help  show this help message and exit
```

and issues errors when users give the program invalid arguments:

```
$ python script_template.py in.nc
usage: script_template.py [-h] infile outfile
script_template.py: error: the following arguments are required: outfile
``` 

Using this template as a starting point,
we can add the functions we developed previously to start writing our
`plot_precipitation_climatology.py` script.

```
$ cat plot_precipitation_climatology.py

import argparse
import iris
iris.FUTURE.netcdf_promote = True
import matplotlib.pyplot as plt
import iris.plot as iplt
import iris.coord_categorisation
import cmocean
import numpy

def read_data(fname, month):
    """Read an input data file"""
    
    cube = iris.load_cube(fname, 'precipitation_flux')
    
    iris.coord_categorisation.add_month(cube, 'time')
    cube = cube.extract(iris.Constraint(month=month))
    
    return cube

def convert_pr_units(cube):
    """Convert kg m-2 s-1 to mm day-1"""
    
    cube.data = cube.data * 86400
    cube.units = 'mm/day'
    
    return cube

def plot_data(cube, month, cmap=cmocean.cm.haline_r):
    """Plot the data."""
        
    fig = plt.figure(figsize=[12,5])    
    iplt.contourf(cube, cmap=cmap, 
                  levels=numpy.arange(0, 10),
                  extend='max')

    plt.gca().coastlines()
    cbar = plt.colorbar()
    cbar.set_label(str(cube.units))
    
    title = '%s precipitation climatology (%s)' %(cube.attributes['model_id'], month)
    plt.title(title)

def main(inargs):
    """Run the program."""

    cube = read_data(inargs.infile, inargs.month)    
    cube = convert_pr_units(cube)
    clim = cube.collapsed('time', iris.analysis.MEAN)
    plot_data(clim, inargs.month)
    plt.savefig(inargs.outfile)

if __name__ == '__main__':
    description='Plot the precipitation climatology.'
    parser = argparse.ArgumentParser(description=description)
    
    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("month", type=str, help="Month to plot")
    parser.add_argument("outfile", type=str, help="Output file name")

    args = parser.parse_args()
```

```
$ python plot_precipitation_climatology.py data/pr_Amon_ACCESS1-3_historical_r1i1p1_200101-200512.nc May pr_Amon_ACCESS1-3_historical_r1i1p1_200101-200512-clim.png
```

**Challenge:** Take the `plot_precipitation_climatology.py` script
and make the following improvements
(you may need to browse the 
[argparse](https://docs.python.org/3/howto/argparse.html)
tutorial for ideas)

1. The `parser.add_argument()` function has an optional `choices` keyword argument.
Use it to define the valid input months (i.e. `['Jan', 'Feb', ...]`).

2. Add an optional argparse argument for the color palette and set the default to `cmocean.cm.haline_r`

3. Add a true/false optional argparse argument to allow the user to add gridlines to the plot (hint: the code for plotting gridlines is `plt.gca().gridlines()`)  

4. Add an optional argparse argument that allows the user to specify the tick levels used in the colorbar 
