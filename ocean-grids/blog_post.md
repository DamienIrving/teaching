# Data analysis on ocean model grids

Since making the shift from an atmosphere-based PhD to an ocean-based postdoc, I've spent more time than I'd like getting my head around ocean model grids. In particular, the convention for modelling groups participating in the CMIP5 project was to archive ocean variables on the native model grid. Some of the CMIP5 ocean models run on a rectilinear grid (i.e. a regular latitude/longitude grid like the atmosphere model), but most are run on some sort of curvilinear grid (i.e. a grid where the coordinate lines are curved). The details of these curvilinear grids are not typically available to those who download CMIP5 data, but the (netCDF) data files do contain auxillary coordinate information that specifies the location of each curvilinear grid point in two dimensional latitude-longitude space.

At some point, most analysis of CMIP5 ocean data involves remapping from the native curvilinear grid to a regular latitude/longitude grid (e.g. so that a simple contour plot on geographic grid can be produced). I've found that the level of complexity involved in this remapping depends on whether you're dealing with a scalar (e.g. temperature, salinity, potential density) or vector (e.g. water velocity, mass transport) quantity, and also whether there are conservation properties that need to be maintained (e.g. conservation of energy or moisture). 

The discussion that follows is my attempt to step through each level of complexity, exploring the software packages and analysis approaches out there for remapping from a curvilinear to rectilinear grid. When it comes to software my main focus is Python, as it is rapidly emerging as the language of choice in climate science. Where the scientific Python ecosystem is found wanting, I'll discuss other solutions.



## 1. Scalar to scalar, conservation not required

Let's start with most simple case, where you've got a scalar quantity such as temperature and you want to remap from a curvilinear to rectilinear grid. Let's say you're doing this in order to create a simple plot of the SST climatology, so you're not worried about conservation (i.e. it doesn't matter if the global mean temperature changes by 0.01 degrees or something after it's all done).

In Python, your options are either the [`regrid_weighted_curvilinear_to_rectilinear`](https://scitools.org.uk/iris/docs/latest/iris/iris/experimental/regrid.html?highlight=regrid_weighted_curvilinear_to_rectilinear#iris.experimental.regrid.regrid_weighted_curvilinear_to_rectilinear) function that comes with Iris, or the xESMF package (which will be easier for xarray users).

TODO: Notebook using these two.  


https://github.com/DamienIrving/ocean-analysis/issues/2

## 2. Scalar to scalar, conservation required

In order to infer meridional heat transports from netTOA, OHU and OHC data, it is critical that the zonal integration of these quantities conserves the global sum. This is obviously trivial for models run on a regular latitude-longitude grid, but it is not for curvilinear grids. Regridding from a curvilinear to rectilinear grid typically results in a non-conservative zonal integral, so it is necessary to adopt a different approach. Similar to a recent study of heat transport into the Arctic Ocean (Nummelin 2017), we got around this problem by making use of the fact that curvilinear CMIP5 data files come with auxillary coordinate information that specifies the location of each grid point in two dimensional latitude-longitude space. For each individual one degree latitude band, we therefore simply added up all grid cells whose auxillary coordinate falls within that band. Likewise, hemispheric values where calculated by adding up all grid cells whose auxillary coordinate falls within a given hemisphere.


My zonal aggregation method is fine for single level, but can be very slow for multiple depths.


## 3. Vector to scalar, conservation required

From https://journals.ametsoc.org/doi/full/10.1175/JCLI-D-18-0058.1
Three methods were tested to accurately calculate HO in the seven models for which hfbasin was not available...
a. Using a sum of net surface flux and rate of change of ocean heat content to calculate an “implied” meridional heat transport

b. Convert hfy and hfx into northward and eastward components using the grid angle at each grid cell (if you have that information). While in principle this approach should produce an accurate meridional heat transport, small differences were found when compared to heat transport directly output from the model at all locations where the grid was curved. Investigation revealed that the grid angle is given for the p points of the grid cells (i.e., the center of each grid cell), while the hfy and hfx were given on the top and bottom and left and right edges of the grid cell, respectively, as per a standard C-grid configuration. Thus the angles given are not accurate for the locations of hfy and hfx, hence the small differences in the calculated heat transport when compared to the heat transport output directly from the model. The differences manifest themselves with sharp changes from one latitude to the next.
This might be solved with https://xgcm.readthedocs.io/en/latest/

c. zigzag method and is shown schematically in Fig. 2. In this method, grid cells are selected along a line of single latitude. A zonal boundary is then identified from the edges of these grid cells, and the fluxes across this boundary are summed to give the meridional transport at the respective latitude. At latitudes where the model grid is not curved (Fig. 2, light gray boxes), identified grid cells are on a single model grid row, and the derived meridional heat flux is composed entirely of the ocean heat transport in the y direction. However, at latitudes closer to the model grid poles where the grid is curved, the identified cells at a single latitude are not on the same row, thus the transport across the boundary includes heat transport in both the y and x directions. Depending upon the direction in which the boundary is crossed, some of these values may be negative, for example, hfy that is southward transport due to extreme grid curvature. The process was repeated at each latitude to obtain a complete meridional ocean heat transport HO.

## 4. Vector to vector

https://github.com/DamienIrving/ocean-analysis/issues/6



Other stuff:

- Difference between finite difference, finite element and spectral grids: http://www.oc.nps.edu/nom/modeling/grids.html 
