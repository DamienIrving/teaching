---
title: Research Software Engineering with Python
---

![](https://i.imgur.com/xDy67Hx.jpg)
[https://merely-useful.tech/py-rse/](https://merely-useful.tech/py-rse/)
Damien Irving, CSIRO Climate Science Centre

---

## Data analysis project

----

**Zipf’s Law** states that the second most common word in a body of text appears half as often as the most common, the third most common appears a third as often, and so on.

----

To test whether Zipf’s Law holds for a collection of classic novels available from [Project Gutenberg](https://www.gutenberg.org/), we wrote software that counts and analyses the word frequency distribution in any arbitrary body of text.

----

![](https://i.imgur.com/BXPs6z7.png)

Word count distribution for *Dracula* ($\alpha = 1.1$)

---

## Overview

----

1. Organise small and medium-sized data science projects
2. Use the Unix shell to efficiently manage your data and code
3. Write Python programs that can be used on the command line
4. Use Git and GitHub to track and share your work

----

5. Work productively in a small team where everyone is welcome
6. Use Make to automate complex workflows
7. Enable users to configure your software without modifying it directly
8. Test your software and know which parts have not yet been tested
9. Find, handle, and fix errors in your code

----

10. Publish your code and research in open and reproducible ways
11. Create Python packages that can be installed in standard ways

(We assume you're already using Python for data analysis.)

---

## 1. Get organised

----

```text
pyzipf/
├── .gitignore
├── CITATION.md
├── CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE.md
├── README.md
├── Makefile
├── bin (or pyzipf)
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
```

Software: Bash shell, Git, text editor, Python (via Anaconda), GNU Make.

---

## 2. Unix Shell

---

## 3. Command line programs

----

The Jupyter Notebook, PyCharm, and other graphical interfaces are great for prototyping code and exploring data, but eventually we may need to apply our code to thousands of data files, run it with many different parameters, or combine it with other programs as part of a data analysis pipeline.

----

The easiest way to do this is often to turn our code into a standalone program that can be run in the Unix shell just like other command-line tools.

---

## 4. Git and GitHub

----

Version control works by storing a master copy of your code in a repository, which you can’t edit directly.

Instead, you check out a working copy of the code, edit that code, then commit changes back to the repository.

In this way, version control records a complete revision history (i.e., of every commit), so that you can retrieve and compare previous versions at any time.

----

![](https://i.imgur.com/jnEJxVY.png)

----

The basics:
```bash
$ git init

$ git add
$ git commit
$ git push
$ git pull

$ git status
$ git diff
```

----

More advanced topics:
- Branching
- Conflicts
- Branch-per-feature workflows
- [Pull requests](https://github.com/merely-useful/py-rse/pull/567)

----

![](https://i.imgur.com/Rv1dG8b.png)

---

## 5. Working in teams

The success of a software project depends on more than just writing nice code.

----

- Inclusivity
- Code of conduct
- Licenses (for software, data and reports)
- Issue tracking
- Prioritising
- Meetings / decision making / handling conflict
- Bug reports

---

## 6. Workflow automation

----

It’s easy to run one program to process a single data file, but what happens when our analysis depends on many files, or when we need to re-do the analysis every time new data arrives?

What should we do if the analysis has several steps that we have to do in a particular order?

----

If we try to keep track of this ourselves, we will inevitably forget some crucial steps and it will be hard for other people to pick up our work.

Instead, we should use a **build manager** to keep track of what depends on what and run our analysis programs automatically.

---

## 7. Configuring programs

As our programs or workflows become more complex, we may want to use up to four layers of configuration.

----

1. A system-wide configuration file for general settings
2. A user-specific configuration file for personal preferences
3. A job-specific file with settings for a particular run
4. Command-line options to change things that commonly change

---

## 8. Testing

----

### pytest

- Tests are put in files whose names begin with test_
- Each test is a function whose name also begins with test_
- These functions use assert to check results

----

- Floating point numbers ([pytest.approx](https://docs.pytest.org/en/6.2.x/reference.html#pytest-approx))
- Integration testing
- Regression testing
- Test coverage
- Continuous integration ([GitHub Actions](https://github.com/features/actions))
- How much testing is enough?

---

## 9. Handling errors

----

```python
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='logging.log')

logging.debug('This is for debugging.')
logging.info('This is just for information.')
logging.warning('This is a warning.')
logging.error('Something went wrong.')
logging.critical('Something went seriously wrong.')
```

---

## 10. Provenance tracking

1. Analysis code
2. Software environment 
3. Processing steps

----

Khan A & Virtanen S, 2020. Zipf's Law in classic english texts. *Journal of Important Research*, 27, 134-139

[README](https://github.com/amira-khan/zipf/blob/master/KhanVirtanen2020.md)
[Release](https://github.com/amira-khan/zipf/releases/tag/KhanVirtanen2020)
[Zenodo integration](https://guides.github.com/activities/citable-code/)

---

## 11. Packaging

via `setuptools`

----

```text
pkg_name
├── pkg_name
│   ├── module1.py
│   └── module2.py
├── README.md
└── setup.py
```

----

### Installation

----

### Distribution

```bash
$ python setup.py sdist
$ twine upload --repository pypi dist/*
```

https://pypi.org/project/pyzipf/

----

### Documentation

```bash
$ pip install sphinx
$ mkdir docs
$ cd docs
$ sphinx-quickstart
$ make html
```

https://github.com/amira-khan/zipf/tree/master/docs
https://pyzipf.readthedocs.io/en/latest/

----

### Publication

Consider a dedicated research software journal such as the [Journal of Open Research Software](https://openresearchsoftware.metajnl.com/) or the [Journal of Open Source Software](https://joss.theoj.org/).

---

## What's next?

12 quick tips for software design
https://github.com/gvwilson/12-design#readme

---

## Questions?

Book: [https://merely-useful.tech/py-rse/](https://merely-useful.tech/py-rse/)

Slides: [https://hackmd.io/@damienirving](https://hackmd.io/@damienirving)

---
