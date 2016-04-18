# Conda tutorial

## Background

See [this post](https://drclimate.wordpress.com/2014/10/30/software-installation-explained/)
for a detailed discussion of software installation. 
In summary, the Python package installer (`pip`) only works for libraries written in pure Python.
Many scientific Python libraries have C and/or Fortran dependencies, 
so Continuum Analystics have developed their own package manager called `conda` to deal with this issue.

## Installation

* Anaconda: https://www.continuum.io/downloads
* Windows users will also need a terminal emulator: https://git-for-windows.github.io/
  * If you have any troube, see the [Software Carpentry install instructions](https://swcarpentry.github.io/workshop-template/) 

## Basic usage

Anaconda comes with around 75 of the most widely used libraries (and their depedencies).

In addition, there are around 330 libraries available via `conda install`,
which can be installed via the Navigator or at the command line as follows:  
```
$ conda install xarray
```

## Advanced usage

This is all great, but up until now Anaconda gives us nothing that Canopy doesn't.
The real advantage of Anaconda is anaconda.org -
the community can contribute conda installation packages.

So can use `conda search -f xarray` (or the Navigator) to find out if the packge you want is in the 330.
If it's not, search [Anaconda Cloud](https://anaconda.org)
```
$ conda install -c https://conda.anaconda.org/scitools iris
```

([conda-forge](https://conda-forge.github.io/) has been launched to try and avoid this issue where there are lots of version of the same package)

## Environments

It could take a long time to install all the libraries you use one-by-one,
so instead we can create a conda environment.

First, define a `.yml` file with a list of the libraries you want:

```
$ cat environment.yml

name: imas-pug
channels:
    - ioos
    - scitools
dependencies:
    - python=2.7
    - jupyter
    - iris
    - gsw
```

Then generate that environment:

```
$ conda env create environment.yml
$ source activate imas-pug
$ conda list
```

(it's `source deactivate` to exit)

You can have lots of different environments:

```
$ conda info --envs
```

and you can export them for others to use:

```
$ conda env export -n imas-pug -f imas-pug
$ cat imas-pug
```

```
$ conda env upload -f imas-pug
```

which can then be installed as follows:

```
$ conda env create damienirving/imas-pug
$ source activate imas-pug
```

(To delete an environment `conda env remove -n imas-pug`)  
(To delete anaconda, just delete the folder)

## Miniconda

If you're working on a remote machine (e.g. at NCI),
you might not have space for all of Anaconda.
Instead, install [Miniconda](http://conda.pydata.org/miniconda.html).
It essentially comes with conda and nothing else.


## Help

* Main website: http://conda.pydata.org/docs/index.html (includes link to Google Group)  
* GitHub issues for packages on anaconda.org ([example](https://github.com/ajdawson/windspharm/issues/66))  
* Further reading: https://drclimate.wordpress.com/2016/04/13/keeping-up-with-continuum/


