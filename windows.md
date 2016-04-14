## Terminal emulator

The best one is [Git for Windows](https://git-for-windows.github.io/), otherwise known as Git Bash or MSysGit.

MSys is an environment for Windows offering a Unix-type shell. 
Since Git requires such an environment to run on Windows, 
they are packaged together and named MSysGit.

MSysGit tries to make Windows paths look more like Unix paths 
by allowing us to use a forward slash instead of a backslash as a separator.
It also allows us to refer to the C drive as `/c` instead of as `C:`.
Paths are still case insensitive, though, 
which means that if you try to put files called backup.txt (in all lower case) 
and Backup.txt (with a capital 'B') into the same directory, 
the second will overwrite the first.

MSysGit also doesn't come with `man` (the command for showing the manual for a given program), 
although this tends not be be a problem since the `--help` flag does much the same thing in most cases.
