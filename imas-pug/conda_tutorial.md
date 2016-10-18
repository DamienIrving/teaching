# Package management in Python

## Background

See [this post](https://drclimate.wordpress.com/2014/10/30/software-installation-explained/)
for a detailed discussion of software installation. 
In summary, the Python package installer (`pip`) only works for libraries written in pure Python.
Many scientific Python libraries have C and/or Fortran dependencies,
so the easy solution to this problem is to use a distribution like Anaconda or Canopy, 
which come with all the most popular libraries pre-installed.
These distributions also come with a package manager for installing libraries that weren't pre-installed.
This tutorial focuses on `conda`, which is the package manager associated with Anaconda
(as we'll see, it's better than the Canopy package manager).

## Installation

* Anaconda: https://www.continuum.io/downloads
* Windows users will also need a terminal emulator: https://git-for-windows.github.io/
  * If you have any troube, see the [Software Carpentry install instructions](https://swcarpentry.github.io/workshop-template/) 

## Basic usage

Anaconda comes with around 75 of the most widely used libraries (and their depedencies).

In addition, there are around 330 libraries available via `conda install`,
which can be installed via the Navigator or at the command line as per the following example:  
```
$ conda install xarray
```
### Side note: Miniconda

It should be noted that if you don't want to install the entire Anaconda distribution,
which is quite large, you can install [Miniconda](http://conda.pydata.org/miniconda.html) instead.
It essentially comes with conda and nothing else.


## Advanced usage

This is all great, but up until now Anaconda gives us nothing that Canopy doesn't.
The real advantage of Anaconda is the [Anaconda Cloud](https://anaconda.org) website,
where the community can contribute conda installation packages.

You can use `conda search -f xarray` (or the Navigator) to find out if the packge you want is in the 330.
If it's not, search Anaconda Cloud and find the command line entry needed to install the package. e.g:
```
$ conda install -c https://conda.anaconda.org/scitools iris
```

([conda-forge](https://conda-forge.github.io/) has been launched to try and avoid the issue where there are multiple versions of the same package)

### Environments

It could take a long time to install all your libraries one-by-one,
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
```

(The resulting file `imas-pug` has a bug in that the required channels aren't listed.
You can either add them manually or use [this work-around](https://github.com/conda/conda/issues/2350#issuecomment-211725309).)

You can then upload the environment to your account at Anaconda Cloud:

```
$ conda env upload -f imas-pug
```

so that others can re-create your environment as follows:

```
$ conda env create damienirving/imas-pug
$ source activate imas-pug
```

(To delete an environment `conda env remove -n imas-pug`)  
(To delete anaconda, just delete the folder)


### Side note: conda kapsel

To make the management of environments even easier, [conda kapsel](https://www.continuum.io/blog/developer-blog/automate-your-readme-conda-kapsel-beta-1) has been released.


## Help

* Main website: http://conda.pydata.org/docs/index.html (includes link to Google Group for help questions)  
* Further reading: https://drclimate.wordpress.com/2016/04/13/keeping-up-with-continuum/


