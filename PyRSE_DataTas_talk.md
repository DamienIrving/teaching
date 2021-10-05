# Abstract

Research Software Engineering with Python

Most researchers these days have picked up enough coding to get their own work done.
The next frontier is writing code with and for others.
Academic journals are (slowly) moving towards requiring code to be made available with research papers,
and it's increasingly necessary for researchers to know how to collaboratively develop,
package and release software for use by team members and the wider research community.
With this skills progression in mind,
a group of experienced data science educators recently teamed up
to write Research Software Engineering with Python.
The book is a ready-to-go university semester course (or self study guide)
aimed at helping researchers go from writing code for themselves,
to creating tools that help their entire field advance.
The book covers the entire lifecycle of a real data science project,
from initial setup and code development
through to a fully automated data processing pipeline and published software package.
One of the authors - Damien Irving -
is a data scientist at the CSIRO Climate Science Centre in Hobart.
At this event, Damien will walk us through the data science project presented in the book,
briefly touching upon a series of important concepts, tools, skills and best practices along the way.
If you're interested in taking the next step with your Python programming,
this event is a great opportunity to get a feel for what skills you already have,
what skills you might need to pick up, and how they all fit together in the bigger picture.
Damien will also have a few free copies of the book to give away.


# Introduction

Data Scientist at the CSIRO Climate Science Centre.

For the best part of a decade, I’ve volunteered as an instructor with The Carpentries,
which is a global community committed to teaching foundational coding and data science skills to researchers.

The audience at these workshops is typically researchers who are self-taught programmers
(i.e. they are able to cobble together enough Python or R to clean, analyse and plot their research data)
and we expose them to a number coding best practices that have solid foundations in research and experience and that improve productivity and reliability.

A big part of the Carpentries success is the two-day format
(it’s not an overwhelming time commitment for busy researchers),
but over the years I’ve often wondered what we’d teach if we had more time.
With an entire semester, for instance,
you could take a researcher through the entire lifecycle of a data analysis project,
from the initial setup and code development through to a fully automated data processing pipeline and published software package.

A few of years ago, Greg Wilson (who co-founded The Carpentries)
assembled a small group of Carpentries instructors to try and write such a book.
I very happily joined in, and Research Software Engineering with Python was published in August this year.

Today I wanted to walk you all through the data science project presented in the book,
briefly touching upon a series of important concepts, tools, skills and best practices along the way.
If you're interested in taking the next step with your Python programming,
this will hopefully allow you to get a feel for what skills you already have,
what skills you might need to pick up, and how they all fit together in the bigger picture.


# Overview

The data analysis task that we focus on relates to a fascinating result in the field of quantitative linguistics.
Zipf’s Law states that the second most common word in a body of text appears half as often as the most common,
the third most common appears a third as often, and so on.
To test whether Zipf’s Law holds for a collection of classic novels that are freely available from Project Gutenberg,
we write a software package that counts and analyzes the word frequency distribution in any arbitrary body of text.

In the process of writing and publishing this Python package to verify Zipf’s Law,
the book covers how to do the following:

- Organise small and medium-sized data science projects.
- Use the Unix shell to efficiently manage your data and code.
- Write Python programs that can be used on the command line.
- Use Git and GitHub to track and share your work.
- Work productively in a small team where everyone is welcome.
- Use Make to automate complex workflows.
- Enable users to configure your software without modifying it directly.
- Test your software and know which parts have not yet been tested.
- Find, handle, and fix errors in your code.
- Publish your code and research in open and reproducible ways.
- Create Python packages that can be installed in standard ways.

(We assuming you're already using Python for data analysis.)


# Getting started

## Project structure

An abbreviated version of the project directory tree as it appears toward the end of the book:

zipf/
├── .gitignore
├── CITATION.md
├── CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── Makefile
├── bin
│   ├── book_summary.sh
│   ├── collate.py
│   ├── countwords.py
│   └── ...
├── data
│   ├── README.md
│   ├── dracula.txt
│   ├── frankenstein.txt
│   └── ...
├── docs
│   └── ...
├── results
│   ├── collated.csv
│   ├── dracula.csv
│   ├── dracula.png
│   └── ...
└── ...

## Software installation

In order to conduct our analysis, we need to install the following software:

- A Bash shell
- Git version control
- A text editor
- Python 3 (via the Anaconda distribution)
- GNU Make


# Unix Shell

A more powerful version of Finder / Windows Explorer. 
- Organise and interrogate files, coordinate workflows, etc

(In the book we look at all the basics - how to move around, copy, delete, etc)

Three shortest books:
```bash
$ wc -l *.txt | sort -n | head -n 3
```

Book summary information:
```bash
$ cat book_summary.sh
```

```
# Get desired information from a Project Gutenberg eBook.
# Usage: bash book_summary.sh /path/to/file.txt what_to_look_for
head -n 17 $1 | tail -n 8 | grep $2
```

```bash
$ bash book_summary.sh ../data/frankenstein.txt Author
$ bash book_summary.sh ../data/frankenstein.txt Release
```

Find all the books and their authors:
```
$ grep "Author:" $(find . -name "*.txt")
```

# Command line programs

The Jupyter Notebook, PyCharm, and other graphical interfaces are great for prototyping code and exploring data,
but eventually we may need to apply our code to thousands of data files,
run it with many different parameters, or combine it with other programs as part of a data analysis pipeline.
The easiest way to do this is often to turn our code into a standalone program
that can be run in the Unix shell just like other command-line tools.

Write some code to count words:

```python
import string
from collections import Counter

with open('data/dracula.txt', 'r') as reader:
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks] 
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)

print(word_counts)
```

Put it in a function:

```python
def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks] 
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts


with open('data/dracula.txt', 'r') as reader:
    word_counts = count_words(reader)
print(word_counts)
```

Initial script for counting words (`countwords.py`):

```python
"""
Count the occurrences of all words in a text
and output them in CSV format.
"""

import sys
import argparse
import string
import csv
from collections import Counter


def collection_to_csv(collection, num=None):
    """Write collection of items and counts in csv format."""
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])


def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts

    
def main(args):
    """Run the command line program."""
    word_counts = count_words(args.infile)
    collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)
```

```bash
$ python bin/countwords.py data/dracula.txt -n 10
$ head -n 500 data/dracula.txt | python bin/countwords.py --n 10
```

```bash
$ python bin/countwords.py data/dracula.txt > results/dracula.csv
$ python bin/countwords.py data/moby_dick.txt > results/moby_dick.csv
$ python bin/countwords.py data/jane_eyre.txt > results/jane_eyre.csv
```



Write a second scrpt for collating word counts from multiple files (`collate.py`)

```python
"""
Combine multiple word count CSV-files
into a single cumulative count.
"""

import sys
import csv
import argparse
from collections import Counter


def collection_to_csv(collection, num=None):
    """Write collection of items and counts in csv format."""
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])


def update_counts(reader, word_counts):
    """Update word counts with data from another reader/file."""
    for word, count in csv.reader(reader):
        word_counts[word] += int(count)


def main(args):
    """Run the command line program."""
    word_counts = Counter()
    for fname in args.infiles:
        with open(fname, 'r') as reader:
            update_counts(reader, word_counts)
    collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infiles', type=str, nargs='*',
                        help='Input file names')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)

```

```
$ python bin/collate.py results/dracula.csv results/moby_dick.csv results/jane_eyre.csv -n 10
```

Write a module for the duplicated function (`utilities.py`):

```python

"""Collection of commonly used functions."""

import sys
import csv


def collection_to_csv(collection, num=None):
    """
    Write out collection of items and counts in csv format.

    Parameters
    ----------
    collection : collections.Counter
        Collection of items and counts
    num : int
        Limit output to N most frequent items
    """
    collection = collection.most_common()
    if num is None:
        num = len(collection)
    writer = csv.writer(sys.stdout)
    writer.writerows(collection[0:num])
```

After making this change, `countwords.py` looks like this:

```
"""
Count the occurrences of all words in a text
and write them to a CSV-file.
"""

import argparse
import string
from collections import Counter

import utilities as util


def count_words(reader):
    """Count the occurrence of each word in a string."""
    text = reader.read()
    chunks = text.split()
    npunc = [word.strip(string.punctuation) for word in chunks]
    word_list = [word.lower() for word in npunc if word]
    word_counts = Counter(word_list)
    return word_counts


def main(args):
    """Run the command line program."""
    word_counts = count_words(args.infile)
    util.collection_to_csv(word_counts, num=args.num)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('infile', type=argparse.FileType('r'),
                        nargs='?', default='-',
                        help='Input file name')
    parser.add_argument('-n', '--num',
                        type=int, default=None,
                        help='Output n most frequent words')
    args = parser.parse_args()
    main(args)
```

We also write a plotting script:

```bash
$ python bin/plotcounts.py results/jane_eyre.csv --outfile results/jane_eyre.png
```

# Git

Version control works by storing a master copy of your code in a repository,
which you can’t edit directly.
Instead, you check out a working copy of the code, edit that code, then commit changes back to the repository.
In this way, version control records a complete revision history (i.e., of every commit),
so that you can retrieve and compare previous versions at any time.
This is useful from an individual viewpoint,
because you don’t need to store multiple (but slightly different) copies of the same script (Figure 6.1).
It’s also useful from a collaboration viewpoint,
because the system keeps a record of who made what changes and when.

```bash
$ git init .
$ git add .
$ git status
$ git commit -m "Add scripts, novels, word counts, and plots"
```

https://github.com/amira-khan/zipf

branching, conflicts...

Most experienced developers use a branch-per-feature workflow.
What exactly is a “feature”?
These rules make sense for small projects:

- Anything cosmetic that is only one or two lines long can be done in master and committed right away.
  Here, “cosmetic” means changes to comments or documentation: nothing that affects how code runs, not even a simple variable renaming.
- A pure addition that doesn’t change anything else is a feature 
- Every change to code that someone might want to undo later in one step is a feature.

The hardest thing about using a branch-per-feature workflow is sticking to it for small changes.
As the first point in the list above suggests, most people are pragmatic about this on small projects;
on large ones, where dozens of people might be committing,
even the smallest and most innocuous change needs to be in its own branch so that it can be reviewed.

Pull requests


# Working in teams

Clearly the success of a software project depends on more than just writing good code
(e.g. R as a language sucks but has great community).

Inclusivity
Code of conduct
Licenses (for software, data and reports)
Issue tracking
Prioritising
Meetings, decision making (Martha's rules), handling conflict
Bug reports


# Automation

It’s easy to run one program to process a single data file,
but what happens when our analysis depends on many files,
or when we need to re-do the analysis every time new data arrives?
What should we do if the analysis has several steps that we have to do in a particular order?

If we try to keep track of this ourselves,
we will inevitably forget some crucial steps and it will be hard for other people to pick up our work.
Instead, we should use a build manager to keep track of what depends on what and run our analysis programs automatically.
These tools were invented to help programmers compile complex software, but can be used to automate any workflow.

Make works as follows:

- A user can describe which files depend on each other by writing rules in a Makefile. 
- Every time the operating system creates, reads, or changes a file, it updates a timestamp on the file to show when the operation took place.
  Make can compare these timestamps to figure out whether files are newer or older than one another.
- When the user runs Make, the program checks all of the rules in the Makefile and runs the commands needed to update any that are out of date. 
  If there are transitive dependencies—i.e., if A depends on B and B depends on C—then Make will trace them through and run all of the commands it needs to in the right order.


```make
.PHONY: all clean help settings results

COUNT=bin/countwords.py
COLLATE=bin/collate.py
PARAMS=bin/plotparams.yml
PLOT=bin/plotcounts.py
SUMMARY=bin/book_summary.sh
DATA=$(wildcard data/*.txt)
RESULTS=$(patsubst data/%.txt,results/%.csv,$(DATA))

## all : regenerate all results.
all : results/collated.png

## results : regenerate result for all books.
results : ${RESULTS}

## results/collated.png: plot the collated results.
results/collated.png : results/collated.csv $(PARAMS)
	python $(PLOT) $< --outfile $@ --plotparams $(word 2,$^)

## results/collated.csv : collate all results.
results/collated.csv : $(RESULTS) $(COLLATE)
	@mkdir -p results
	python $(COLLATE) $(RESULTS) > $@

## results/%.csv : regenerate result for any book.
results/%.csv : data/%.txt $(COUNT)
	@bash $(SUMMARY) $< Title
	@bash $(SUMMARY) $< Author
	python $(COUNT) $< > $@

## clean : remove all generated files.
clean :
	rm $(RESULTS) results/collated.csv results/collated.png

## settings : show variables' values.
settings :
	@echo COUNT: $(COUNT)
	@echo DATA: $(DATA)
	@echo RESULTS: $(RESULTS)
	@echo COLLATE: $(COLLATE)
	@echo PARAMS: $(PARAMS)
	@echo PLOT: $(PLOT)
	@echo SUMMARY: $(SUMMARY)

## help : show all commands.
help :
	@grep -h -E '^##' ${MAKEFILE_LIST} | sed -e 's/## //g' \
	| column -t -s ':'
```

```bash
$ make all
```

Make a change to the collated script and run `make all` again.


# Configuring programs

So far we've used command-line options to configure/control our scripts and programs
(i.e. so we don't edit them directly, which is error prone and ruins version control).
As our programs or workflows become more complex,
we may want to use up to four layers of configuration:

1. A system-wide configuration file for general settings.
2. A user-specific configuration file for personal preferences.
3. A job-specific file with settings for a particular run.
4. Command-line options to change things that commonly change.

This is sometimes called overlay configuration because each level overrides the ones above it.

This concept can be difficult to understand in the abstract,
so to see overlay configuration in action we consider a common task in data science:
tweaking (e.g. changing the size of the labels) the appearance of a plot.

## 1. Edit the system-wide Matplotlib configuration file

```python
import matplotlib as mpl
mpl.matplotlib_fname()
```

`/Users/irv033/opt/anaconda3/lib/python3.8/site-packages/matplotlib/mpl-data/matplotlibrc`

`matplotlibrc` lists all the default settings as comments.

The default size of the X and Y axis labels is “medium”, as is the size of the tick labels:
```yaml
#axes.labelsize    : medium  ## fontsize of the x and y labels
#xtick.labelsize   : medium  ## fontsize of the tick labels
#ytick.labelsize   : medium  ## fontsize of the tick labels
```

We can uncomment those lines and change the sizes to “large” and “extra large”:
```yaml
axes.labelsize     : x-large  ## fontsize of the x and y labels
xtick.labelsize    : large    ## fontsize of the tick labels
ytick.labelsize    : large    ## fontsize of the tick labels
```

(YAML is the most common format for config files - we have a whole appendix on it in the book)

Since the matplotlibrc file sets system-wide defaults,
we will now have big labels by default for all plotting we do in the future, which we may not want. 
Secondly, we want to package our Zipf’s Law code and make it available to other people.
That package won’t include our matplotlibrc file, and we don’t have access to the one on their computer,
so this solution isn’t as reproducible as others.


## 2. Create a user-specific Matplotlib style sheet

```python
import matplotlib.pyplot as plt
print(plt.style.available)
```

The convention is to store custom style sheets in a stylelib sub-directory in the Matplotlib configuration directory. 
The directory can be located by running the following command:

```python
mpl.get_configdir()
```

Once we’ve created the new sub-directory:
```
$ mkdir /Users/irv033/.matplotlib/stylelib
```
we can add a new file called `big-labels.mplstyle` that has the same YAML format as the matplotlibrc file:

```yaml
axes.labelsize   : x-large  ## fontsize of the x and y labels
xtick.labelsize  : large    ## fontsize of the tick labels
ytick.labelsize  : large    ## fontsize of the tick labels
```

To use this new style, we would just need to add one line to `plotcounts.py`:

```python
plt.style.use('big-labels')
```

Using a custom style sheet leaves the system-wide defaults unchanged,
and it’s a good way to achieve a consistent look across our personal data visualization projects.
However, since each user has their own stylelib directory,
it doesn’t solve the problem of ensuring that other people can reproduce our plots.

## 4. Add some new command-line options to `plotcounts.py`.

Hmatplotlibrc has hundreds of parameters we could change,
so the number of new arguments can quickly get out of hand if we want to tweak other aspects of the plot.

## 3. Create a job-specific configuration file to set plotting options in `plotcounts.py`.

Pass a YAML file full of Matplotlib parameters to `plotcounts.py`.

e.g. `plotparams.yml` reads as:

```yaml
# Plot characteristics
axes.labelsize   : x-large  ## fontsize of the x and y labels
xtick.labelsize  : large    ## fontsize of the tick labels
ytick.labelsize  : large    ## fontsize of the tick labels
```

```bash
$ python bin/plotcounts.py results/jane_eyre.csv --outfile results/jane_eyre.png --plotparams plotparams.yml
```

# Testing

## Assertions

```python
frequencies = [13, 10, 2, -4, 5, 6, 25]
total = 0.0
for freq in frequencies[:5]:
    assert freq >= 0.0, 'Word frequencies must be non-negative'
    total += freq
print('total frequency of first 5 words:', total)
```

## Unit tests

Following these rules, we can create a test_zipfs.py script in your bin directory that contains the test we just developed:

```bash
$ cat test_data/risk.txt
```

```python
from collections import Counter

import countwords


def test_word_count():
    """Test the counting of words.

    The example poem is Risk, by Anaïs Nin.
    """
    risk_poem_counts = {'the': 3, 'risk': 2, 'to': 2, 'and': 1,
      'then': 1, 'day': 1, 'came': 1, 'when': 1, 'remain': 1,
      'tight': 1, 'in': 1, 'a': 1, 'bud': 1, 'was': 1,
      'more': 1, 'painful': 1, 'than': 1, 'it': 1, 'took': 1,
      'blossom': 1}
    expected_result = Counter(risk_poem_counts)
    with open('test_data/risk.txt', 'r') as reader:
        actual_result = countwords.count_words(reader)
    assert actual_result == expected_result
```













