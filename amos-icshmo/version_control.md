# Version control

*For this lesson participants follow along command by command,
rather than observing and then completing challenges afterwards.*

A version control system stores a master copy of your code in a repository,
which you can't edit directly. 

Instead, you checkout a working copy of the code,
edit to your heart's content,
then commit changes back to the repository.

In this way,
the system records a complete revision history (i.e. of every commit),
so that you can retrieve and compare previous versions at any time.

This is useful for a whole range of reasons...


## Setup

When we use Git on a new computer for the first time,
we need to configure a few things. 

```
$ git config --global user.name "Your Name"
$ git config --global user.email "you@email.com"

```

This user name and email will be associated with your subsequent Git activity,
which means that any changes pushed to
[GitHub](http://github.com/),
[BitBucket](http://bitbucket.org/),
[GitLab](http://gitlab.com/) or
another Git host server later on in this lesson will include this information.

You only need to run these configuration commands once -
git will remember then for next time.


Then we tell Git to make `planets` a [repository]({{ page.root }}/reference/#repository)—a place where
Git can store versions of our files:

~~~
$ git init
~~~
{: .bash}

If we use `ls` to show the directory's contents,
it appears that nothing has changed:

~~~
$ ls
~~~
{: .bash}

But if we add the `-a` flag to show everything,
we can see that Git has created a hidden directory within `planets` called `.git`:

~~~
$ ls -a
~~~
{: .bash}

~~~
.	..	.git
~~~
{: .output}

Git stores information about the project in this special sub-directory.
If we ever delete it,
we will lose the project's history.

We can check that everything is set up correctly
by asking Git to tell us the status of our project:

~~~
$ git status
~~~
{: .bash}

If you are using a different version of git than I am, then then the exact
wording of the output might be slightly different.

~~~
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
~~~
{: .output}