## Getting around

#### Summary

* The file system is responsible for managing information on disk.
* Information is stored in files, which are stored in directories (folders).
* Directories can also store other directories, which forms a directory tree.
* `/` on its own is the root directory of the whole filesystem.
* A relative path specifies a location starting from the current location.
* An absolute path specifies a location from the root of the filesystem.
* Directory names in a path are separated with `/` on Unix, but `\` on Windows.
* '..' means "the directory above the current one"; '.' on its own means "the current directory".
* Most file names are something.extension; the extension isn't required, and doesn't 
  guarantee anything, but is normally used to indicate the type of data in the file.
* `cd` path changes the current working directory.
* `ls path` prints a listing of a specific file or directory; `ls` on its own lists the 
  current working directory.
* `pwd` prints the user's current working directory
* Most commands take options (flags) which begin with a '-'


#### Challenges

Refer to the sketched file system when answering the following questions

![Example filesystem](filedir_challenge.png)  

1. If `pwd` displays `/users/thing`, what will `ls ../backup` display?  
    a. `../backup: No such file or directory`  
    b. `2012-12-01 2013-01-08 2013-01-27`  
    c. `2012-12-01/ 2013-01-08/ 2013-01-27/`  
    d. `original pnas_final pnas_sub`  

2. If `pwd` displays `/users/backup`, what command will display `original/ pnas_sub/ pnas_final/`?   
    a. `ls pwd`
    b. `ls -r -F`
    c. `ls -r -F /users/backup`
    d. Either b or c, but not a

3. What does the command `cd` without a directory name do?
    a. It has no effect  
    b. It changes the working directory to `/`  
    c. It changes the working directory to the user's home directory  
    d. It is an error  

4. We said earlier that spaces in path names have to be marked with a leading backslash 
   in order for the shell to interpret them properly. Why? What happens if we run a 
   command like `$ ls my\ thesis\ files` without the backslashes?


## Creating things

#### Summary

* Unix documentation uses '^A' to mean "control-A".
* The shell does not have a trash bin: once something is deleted, it's really gone.
* `mkdir path` creates a new directory.
* `cp old new` copies a file.
* `mv old new` moves (renames) a file or directory.
* `rm path` removes (deletes) a file.
* `rmdir path` removes (deletes) an empty directory.

#### Challenges

1. What is the output of the closing ls command in the sequence shown below?  

    $ pwd
    /home/thing/data
    $ ls
    proteins.dat
    $ mkdir recombine
    $ mv proteins.dat recombine
    $ cp recombine/proteins.dat ../proteins-saved.dat
    $ ls

2. Suppose that:  

    $ ls -F
    analyzed/  fructose.dat    raw/   sucrose.dat

What command(s) could you run so that the commands below will produce the output shown?

    $ ls
    analyzed   raw
    $ ls analyzed
    fructose.dat    sucrose.dat

3. What does `cp` do when given several filenames and a directory name, as in:  

    $ mkdir backup
    $ cp thesis/citations.txt thesis/quotations.txt backup

What does `cp` do when given three or more filenames, as in:

    $ ls -F
    intro.txt    methods.txt    survey.txt
    $ cp intro.txt methods.txt survey.txt

Why do you think cp's behavior is different from mv's?

4. The command `ls -R` lists the contents of directories recursively, i.e., lists their 
sub-directories, sub-sub-directories, and so on in alphabetical order at each level. The 
command ls -t lists things by time of last change, with most recently changed files or 
directories first. In what order does `ls -R -t` display things?



## Pipes and filters

#### Summary

* Use wildcards to match filenames.
* '*' is a wildcard pattern that matches zero or more characters in a pathname.
* '?' is a wildcard pattern that matches any single character.
* `command > file` redirects a command's output to a file.
* `first | second` is a pipeline: the output of the first command is used as the input to
  the second.
* The best way to use the shell is to use pipes to combine simple single-purpose programs 
  (filters).
* `cat` displays the contents of its inputs.
* `head` displays the first few lines of its input.
* `sort` sorts its inputs.
* `tail` displays the last few lines of its input.
* `wc` counts lines, words, and characters in its inputs.

#### Challenges


## Loops

#### Summary

* Use a for loop to repeat commands once for every thing in a list.
* Use `$name` to expand a variable (i.e., get its value).
* Do not use spaces, quotes, or wildcard characters such as '*' or '?' in filenames, as 
  it complicates variable expansion.
* Give files consistent names that are easy to match with wildcard patterns to make it 
  easy to select them for looping.
* Use the up-arrow key to scroll up through previous commands to edit and repeat them.
* Use `history` to display recent commands, and `!number` to repeat a command by number.

#### Challenges

## Shell scripts

#### Summary

* Save commands in files (usually called shell scripts) for re-use.
* Use `bash filename` to run saved commands.
* `$*` refers to all of a shell script's command-line parameters.
* `$1, $2, etc.,` refer to specified command-line parameters.
* Letting users decide what files to process is more flexible and more consistent with 
  built-in Unix commands.

#### Challenges


## Finding things

#### Summary

* Everything is stored as bytes, but the bytes in binary files do not represent characters.
* Use nested loops to run commands for every combination of two lists of things.
* Use `\` to break one logical line into several physical lines.
* Use parentheses `()` to keep things combined.
* Use `$(command)` to insert a command's output in place.
* `find` finds files with specific properties that match patterns.
* `grep` selects lines in files that match patterns.
* `man` command displays the manual page for a given command.

#### Challenges

 





