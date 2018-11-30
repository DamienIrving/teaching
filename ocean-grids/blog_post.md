# Data analysis on ocean model grids

Since making the shift from an atmosphere-based PhD to an ocean-based postdoc, I've spent more time than I'd like getting my head around ocean model grids. In particular, the convention for modelling groups participating in CMIP5 was to archive ocean variables on the native model grid. Some of the CMIP5 ocean models run on a rectilinear grid (i.e. a regular latitude/longitude grid like the atmosphere model), but most are run on some sort of curvilinear grid (i.e. a grid where the coordinate lines are curved). The details of these curvilinear grids are in most cases not widely available, but the (netCDF) data files do contain auxillary coordinate information that specifies the location of each curvilinear grid point in two dimensional latitude-longitude space.

At some point, most analysis of CMIP5 ocean data involves remapping from the native curvilinear grid to a regular latitude/longitude grid. I've found that the level of complexity involved in this remapping depends on whether you're dealing with a scalar or vector quantity, and whether there are conservation properties that need to be maintained (e.g. conservation of energy or moisture). 

The discussion that follows is my attempt to step through each level of complexity, exploring the software packages and analysis approaches currently used for remapping from a curvilinear to rectilinear grid. 


## 1. Scalar quantity

The most simple case involves remapping a scalar quantity such as temperature or salinity from a curvilinear to rectilinear grid. There are a number of libraries out there for doing this, which I've had varying degrees of success in implementing:

| Language      | Library / Package           | Implementation |
| :------------ | :-------------              | :-----         |
| Python (iris) | [`regrid_weighted_curvilinear_to_rectilinear`](https://scitools.org.uk/iris/docs/latest/iris/iris/experimental/regrid.html?highlight=regrid_weighted_curvilinear_to_rectilinear#iris.experimental.regrid.regrid_weighted_curvilinear_to_rectilinear) | Successfully implemented, see [notebook](https://github.com/DamienIrving/teaching/blob/master/ocean-grids/scalar_example.ipynb) |
| Python (xarray) | [xESMF](https://xesmf.readthedocs.io/en/latest/Curvilinear_grid.html) | Successfully implemented, see [notebook](https://github.com/DamienIrving/teaching/blob/master/ocean-grids/scalar_example.ipynb) |
| NCL | [rcm2rgrid](https://www.ncl.ucar.edu/Document/Functions/Built-in/rcm2rgrid.shtml) | Haven't tried |
| NCO | [ncremap](http://nco.sourceforge.net/nco.html#ncremap-netCDF-Remapper) | Problems, see [discussion thread](https://sourceforge.net/p/nco/discussion/9830/thread/da8a8a58/) |


## 2. Scalar quantity with conservation

The next level of complexity involves remapping a scalar quantity such as ocean heat content (OHC), where it can be important to conserve the global total. The remapping packages listed above approximately conserve the global mean, but unfortunately not the global sum. This is presumably because some ocean area/volume is gained or lost as the continents subtly change shape between the old and new grid. One of the reasons why CMIP5 ocean data is archived on the native model grid is that providing remapped data would make it impossible to close energy budgets.

To work around this problem, people tend to devise their own scheme for moving from curvilinear to rectilinear space. This typically involves making use of the auxillary coordinate information contained in the CMIP5 data files. For instance, in calculating the zonally integrated OHC (while conserving the global total), [Nummelin et al (2017)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2016GL071333) essentially iterate over each one degree latitude band, adding up the OHC from all grid cells whose auxillary coordinate falls within that band.    

## 3. Vector quantity

The most complex case is when remapping vector quantities such as heat flux (hf) or water velocity. The x and y components of such variables are archived as two separate variables (e.g. hfx and hfy). The complexity arises because the x and y directions on a curvilinear grid are not everywhere the same as the x (eastward) and y (northward) directions on a geographic latitude/longitude grid. This means you can't apply the aforementioned software packages or work-arounds to move from curvilinear to rectilinear space - any remapping requires the use of information from both the native x and y components.

The most obvious solution to this problem would be to convert the native x and y components into eastward and northward components using the grid angle at each grid cell. Unfortunately, the CMIP5 modelling groups didn't archive a grid angle variable, and even if they did it turns out that complications can arise. Using grid angles obtained for the NorESM1-M model, [Outten et al (2018)](https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-18-0058.1) calculated the northward heat transport from the native hfx and hfy components and found small differences compared to the northward heat transport output directly from the model (the hfbasin variable). Investigation revealed that the grid angle was given for the p points of the grid cells (i.e. the center of each grid cell), while the hfy and hfx were given on the top and bottom and left and right edges of the grid cell, respectively, as per a standard [C-grid configuration](http://www.oc.nps.edu/nom/modeling/grids.html). Thus the angles given were not precisely accurate for the locations of hfy and hfx. It's possible that these issues might be overcome using the [xgcm](https://xgcm.readthedocs.io/en/latest/) package (which interpolates variables from one position to another on a C-grid), but the use of that package requires detailed knowledge of the grid configuration (i.e. you need to know that it's a C-grid in the first place), which isn't readily accessible for most CMIP5 models.

The "zigzag" solution that Outten et al (2018) came up with was somewhat similar to the scalar work-around described above. In their method, grid cells were selected along a line of single latitude. A zonal boundary was then identified from the edges of these grid cells, and the fluxes across this boundary were summed to give the meridional transport at the respective latitude. At latitudes close to the model grid poles where the grid is curved, the identified cells at a single latitude were not on the same row, thus the transport across the boundary included heat transport in both the y and x directions. The process was repeated at each latitude to obtain the complete meridional ocean heat transport.

Where possible, others get around the vector quantity issue by converting to scalar quantities. For instance, when dealing with water velocity it is possible to use helmholtz decomposition to write each vector in terms of the streamfunction and velocity potential. These scalar quantities can be remapped to a rectilinear grid, and then gradients can be calculated on the new grid to recover the eastward and northward components of the water velocity.

## Conclusion

Once you move beyond the simple case of remapping a scalar quantity (where conservation isn't important) from a curvilinear to rectilinear grid, there aren't any "off the shelf" software packages available for the job. It's difficult to think of a simple solution for remapping when conservation of the global sum is required (changing the shape of the continents is unavoidable), but we could do much better when it comes to vector quantities. If grid angles and configurations were archived/documented, it would be possible to write software packages that ingest that information in order to perform the remapping.


