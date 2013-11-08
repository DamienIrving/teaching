## Why learn the shell?

### A practical example

Nelle Nemo, a marine biologist, has just returned from a six-month survey of the North 
Pacific Gyre, where she has been sampling gelatinous marine life in the Great Pacific 
Garbage Patch. She has 1520 samples in all, and now needs to:

1. Run each sample through an assay machine that will measure the relative abundance of 
   300 different proteins. The machine's output for a single sample is a file with one 
   line for each protein.
2. Calculate statistics for each of the proteins separately using a program her supervisor
   wrote called `goostat`.
3. Compare the statistics for each protein with corresponding statistics for each other 
   protein using a program one of the other graduate students wrote called `goodiff`.
4. Write up. Her supervisor would really like her to do this by the end of the month so 
   that her paper can appear in an upcoming special issue of Aquatic Goo Letters.

It takes about half an hour for the assay machine to process each sample. The good news 
is, it only takes two minutes to set each one up. Since her lab has eight assay machines 
that she can use in parallel, this step will "only" take about two weeks.

The bad news is, if she has to run `goostat` and `goodiff` by hand, she'll have to enter 
filenames and click "OK" roughly 3002 times (300 runs of `goostat`, plus 300×299 runs of 
`goodiff`). At 30 seconds each, that will 750 hours, or 18 weeks. Not only would she miss 
her paper deadline, the chances of her getting all 90,000 commands right are approximately 
zero.

This is where the command shell comes in. Nelle can use it to automate the repetitive 
steps in her processing pipeline, so that her computer can work 24 hours a day while she 
writes her paper. As a bonus, once she has put a processing pipeline together, she will 
be able to use it again whenever she collects more data.

### A more comprehensive justification

That's a pretty compelling example, however an experienced programmer might argue that you 
could also automate Nelle's analysis by writing an appropriate Python script. A more complete 
justification for learning the shell would therefore be that *so much else depends on it*. 
Installing software (like Python), configuring your default text editor, and controlling 
remote machines (e.g. printers) frequently assume a basic familiarity with the shell. Many 
tools also use its terminology (for example, the %ls and %cd magic commands in IPython).
You also can't use a cloud (or other high performance) computing facility without a working 
knowledge of the shell. The bottom line is, to be a competent software carpenter, 
you can't get by without it.

## What is the shell?

Probably the most confronting thing for first time users of the shell is that it is accessed
via a command-line user interface (CLUI), as opposed to a more familiar graphical user 
interface (GUI). At the heart of a CLUI is the read-evaluate-print loop, or REPL: when the 
user types a command, the computer reads it, executes it, and prints its output. 

This description makes it sound as though the user sends commands directly to the 
computer, and the computer sends output directly to the user. In fact, there is usually a 
program in between called a command shell. What the user types goes into the shell; it 
figures out what commands to run and orders the computer to execute them. 

FIGURE: Relationship between user, shell and computer.

A shell is a program like any other. What's special about it is that its job is to run 
other programs, rather than to do calculations itself. The most popular Unix shell is 
Bash, the Bourne Again SHell (so-called because it's derived from a shell written by 
Stephen Bourne — this is what passes for wit among programmers). Bash is the default shell
on most modern implementations of Unix (e.g. Ubuntu, Mac OS X), and in most packages that 
provide Unix-like tools for Windows, such as GitBash. 

Commands in Bash (or any other shell) are typically terse (often only a couple of 
characters long), their names are frequently cryptic, and their output is lines of text 
rather than something visual like a graph. In a sense, this makes interacting with the 
shell feel more like "real" programming than anything else you do on a computer.

## Getting around 

The part of the operating system responsible for managing files and directories is called 
the file system. It organizes our data into files, which hold information, and directories
(also called "folders"), which hold files or other directories. Most of us would be 
familiar with browsing the file system via GUIs like Windows Explorer or Finder.

In the bash shell, there are several commands for creating, inspecting, renaming, and 
deleting files and directories. 

To begin, let's find out where we are by running a command called `pwd` (which stands for 
"print working directory"). At any moment, our current working directory is our current 
default directory, i.e., the directory that the computer assumes we want to run commands 
in unless we explicitly specify something else. Here, the computer's response is 
`/Users/dbirving`, which is my home directory: 

```
$ pwd
/Users/dbirving
$
```

To understand what a "home directory" is, let's have a look at how the file system as a 
whole is typically organized:  

![A typical file system](filesystem.png)
A typical file system.

At the top is the root directory that holds everything else the computer is storing. We 
refer to it using a slash character `/` on its own; this is the leading slash in 
`/Users/dbirving`. Inside that directory (or underneath it, if you're drawing a tree) are 
several other directories. The names of these will be slightly different from computer to 
computer, but typically consist of directories like `bin` or `usr` (which is where some 
built-in programs are stored), `users` (where users' personal directories are located), 
`tmp` (for temporary files that don't need to be stored long-term), and so on. For 
instance, we can see that Python is stored in the `usr` directory:

```
$ which python
/usr/bin/anaconda/bin/python
$
``` 

Notice that there are two meanings for the `/` character. When it appears at the front of a 
file or directory name, it refers to the root directory. When it appears inside a name, 
it's just a separator. 

Now that we understand the layout of the file system, we can use the `ls` and `cd` 
commands to view the contents of directories and move about.

INTRODUCE: `ls -G -F -a -l -t`, `cd`, `cd ..`, relative versus absolute paths


### Why does my Windows shell look different?


