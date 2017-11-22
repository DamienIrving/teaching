# Package management in Python

## Background

See [this post](https://drclimate.wordpress.com/2014/10/30/software-installation-explained/)
for a detailed discussion of software installation. 
In summary, the Python package installer ([pip](https://pip.pypa.io)) only works for libraries written in pure Python.
Many scientific Python libraries have C and/or Fortran dependencies,
so the easy solution to this problem is to use a distribution like Anaconda or Canopy, 
which come with all the most popular libraries pre-installed.
These distributions also come with a package manager for installing libraries that weren't pre-installed.
This tutorial focuses on [conda](https://conda.io/docs/), which is the package manager associated with Anaconda
(as we'll see, it's better than the Canopy package manager).

## Installation

* Anaconda: https://www.continuum.io/downloads
* Windows users will also need a terminal emulator: https://git-for-windows.github.io/
  * If you have any troube, see the [Software Carpentry install instructions](https://swcarpentry.github.io/workshop-template/) 

## Basic usage

Anaconda comes with around 75 of the most widely used libraries (and their depedencies).

In addition, there are around 330 libraries available via `conda install`,
which can be installed via the Anaconda Navigator graphical user interface or at the command line.
For instance, installing the popular `xarray` library can be achieved
by simply entering the following at the command line:  
```
$ conda install xarray
```
You can use `conda search -f xarray` (or the Navigator) to find out if the packge you want is in the 330.

### (Side note: Miniconda)

If you don't want to install the entire Anaconda distribution,
you can install [Miniconda](http://conda.pydata.org/miniconda.html) instead.
It essentially comes with conda and nothing else.


## Advanced usage

This is all great, but up until now Anaconda gives us nothing that Canopy doesn't.
The real advantage of Anaconda is the [Anaconda Cloud](https://anaconda.org) website,
where the community can contribute conda installation packages.

Search Anaconda Cloud to find the command line entry needed to install the package. e.g:
```
$ conda install -c https://conda.anaconda.org/scitools iris
```

In many cases, there are many versions of the same package up on Anaconda Cloud.
[conda-forge](https://conda-forge.github.io/) has been launched to have a central place for just a single version.
You can therefore expand the selection of packages available via `conda install` beyond the chosen 330 by adding conda-forge:
```
$ conda config --add channels conda-forge
```

### Environments

Now we can go ahead and use conda to install the libraries we need for this lesson.
Rather than install everything in the same place
(which can get unweidly if you've got mutliple data science projects on the go)
it's common practice to create separate environments
for the various projects you're working on. 

Let's call this environment `pyaos-lesson`
and include the [jupyter](https://jupyter.org/) library (so we can use the jupyter notebook),
[iris](http://scitools.org.uk/iris/) (for handling our CMIP5 data),
[cmocean](http://matplotlib.org/cmocean/) (for nice color palettes) and 
[gitpython](http://gitpython.readthedocs.io)
(for integrating version control information into data provenance):

```
$ conda create -n pyaos-lesson jupyter iris cmocean gitpython
$ source activate pyaos-lesson
```
If we list all the libraries in this new envrionment,
we can see that jupyter, iris, cmocean, gitpython
and all their required dependencies have been installed:

```
$ conda list
```

(it's `source deactivate` to exit)

You can have lots of different environments:

```
$ conda info --envs
```

and you can export them (to a YAML configuration file) for others to use:

```
$ conda env export -n pyaos-lesson -f pyaos-lesson
```

You can then upload the environment to your account at Anaconda Cloud:

```
$ conda env upload -f pyaos-lesson
```

so that others can re-create your environment as follows:

```
$ conda env create damienirving/pyaos-lesson
$ source activate pyaos-lesson
```

(To delete an environment `conda env remove -n pyaos-lesson`)  
(To delete anaconda, just delete the folder)


### (Side note: conda kapsel)

To make the management and sharing of environments even easier, [conda kapsel](https://www.continuum.io/blog/developer-blog/automate-your-readme-conda-kapsel-beta-1) has been released.


## Help
  
* Further reading: https://drclimate.wordpress.com/2016/04/13/keeping-up-with-continuum/
