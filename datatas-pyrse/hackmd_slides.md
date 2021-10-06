
![](https://i.imgur.com/xDy67Hx.jpg)

[https://merely-useful.tech/py-rse/](https://merely-useful.tech/py-rse/)

---

## Data analysis project

----

**Zipf’s Law** states that the second most common word in a body of text appears half as often as the most common, the third most common appears a third as often, and so on.

----

To test whether Zipf’s Law holds for a collection of classic novels available from [Project Gutenberg](https://www.gutenberg.org/), we write software that counts and analyses the word frequency distribution in any arbitrary body of text.

----

![](https://i.imgur.com/BXPs6z7.png)

Word count distribution for *Dracula* ($\alpha = 1.1$)

---

## Overview

----

- Organise small and medium-sized data science projects.
- Use the Unix shell to efficiently manage your data and code.
- Write Python programs that can be used on the command line.
- Use Git and GitHub to track and share your work.

----

- Work productively in a small team where everyone is welcome.
- Use Make to automate complex workflows.
- Enable users to configure your software without modifying it directly.
- Test your software and know which parts have not yet been tested.
- Find, handle, and fix errors in your code.

----

- Publish your code and research in open and reproducible ways.
- Create Python packages that can be installed in standard ways.

(We assume you're already using Python for data analysis.)

---

## Project structure

----

```text
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
```

---

## Software installation

Bash shell, Git, text editor, Python 3 (via the Anaconda distribution), GNU Make.

---

## Unix Shell

---

## Command line programs

----

The Jupyter Notebook, PyCharm, and other graphical interfaces are great for prototyping code and exploring data, but eventually we may need to apply our code to thousands of data files, run it with many different parameters, or combine it with other programs as part of a data analysis pipeline.

----

The easiest way to do this is often to turn our code into a standalone program that can be run in the Unix shell just like other command-line tools.

---

## Git

----

Version control works by storing a master copy of your code in a repository, which you can’t edit directly. Instead, you check out a working copy of the code, edit that code, then commit changes back to the repository. In this way, version control records a complete revision history (i.e., of every commit), so that you can retrieve and compare previous versions at any time.

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
- Pull requests

---

## Working in teams

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

## Workflow automation

----

It’s easy to run one program to process a single data file, but what happens when our analysis depends on many files, or when we need to re-do the analysis every time new data arrives?

What should we do if the analysis has several steps that we have to do in a particular order?

----

If we try to keep track of this ourselves, we will inevitably forget some crucial steps and it will be hard for other people to pick up our work.

Instead, we should use a **build manager** to keep track of what depends on what and run our analysis programs automatically.

---

## Configuring programs

As our programs or workflows become more complex, we may want to use up to four layers of configuration.

----

1. A system-wide configuration file for general settings
2. A user-specific configuration file for personal preferences
3. A job-specific file with settings for a particular run
4. Command-line options to change things that commonly change

---

## Testing

----

### pytest

- Tests are put in files whose names begin with test_
- Each test is a function whose name also begins with test_
- These functions use assert to check results

----

- Floating point numbers
- Integration testing
- Regression testing
- Test coverage
- Continuous integration
- How much testing is enough?
 
 ---
