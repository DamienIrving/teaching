# Command line programs

We've arrived at the point where we have successfully defined the functions required to plot the precipitation data.

```
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


def mask_ocean(cube, sftlf_cube):
    """Mask ocean using a sftlf (land surface fraction) file"""
        
    ocean_mask = numpy.where(sftlf_cube.data < 50, True, False)
    
    cube.data = numpy.ma.asarray(cube.data)
    cube.data.mask = ocean_mask
    
    return cube


def plot_data(cube, month, cmap):
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


def plot_pr_climatology(pr_file, sftlf_file, month, cmap=cmocean.cm.haline_r):
    """Plot the precipitation climatology.

    Args:
      pr_file (str): Precipitation data file
      sftlf_file (str): Land surface fraction data file
      month (str): Month (3 letter abbreviation, e.g. Jun)
      cmap: matplotlib colormap

    """

    cube = read_data(pr_file, month)    
    cube = convert_pr_units(cube)
    clim = cube.collapsed('time', iris.analysis.MEAN)

    sftlf_cube = iris.load_cube(sftlf_file, 'land_area_fraction')
    clim = mask_ocean(clim, sftlf_cube)

    plot_data(clim, month, cmap)

```

We could continue to execute these functions from the Jupyter notebook, but in most cases notebooks are simply used to try things out and/or take notes on a new data analysis task. Once you've scoped out the task (as we have for plotting the precipitation climatology), that code can be transferred to a Python script so that it can be executed at the command line. It's likely that your data processing workflows will include command line utilities from the CDO and NCO projects in addition to Python code, so the command line is the natural place to manage your workflows (e.g. using shell scripts or make files).

In general, a Python script that can be executed from the command line will be structured as follows:


```
$ cat script_template.py

```

