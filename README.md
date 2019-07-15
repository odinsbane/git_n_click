# git_n_click
A short introduction to using git, along with some example code that uses the python library click.

# starting a git project

There are two ways to start working on a git project in version control:
Clone an existing project or Create a new one. 

## creating a new repository.

A repository starts as a directory. So for this example Ill create a 
directory 'repo' and change into it.

    pwd

```console
/Users/username/Desktop/repo
```
    
Then I can create/ initialize the repository.

    git init
```console
Initialized empty Git repository in /Users/username/Desktop/repo/.git/
```    
We can check the status.

    git status

```console
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```
Using a `.gitignore` file allows us to ignore files that we don't want to
track. For example .pyc files that are generated. Since we're using 
python github has some pre-assembled .gitignore files. 
[.gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore).

We save that to a file named `.gitingore` in our repo.

    git status

```console
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	.gitignore
nothing added to commit but untracked files present (use "git add" to track)
```

So git recognizes the file, but it hasn't been added.

    git add .gitingore
    git status

```console
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#	new file:   .gitignore
#
```

Lastly we want to commit are changes.

    git commit -m "added .gitignore file"
    
```console
[master (root-commit) b48ac47] added .gitignore file
 1 file changed, 124 insertions(+)
 create mode 100644 .gitignore
```

Now we have a git repository and we're ready to start tracking our changes.

## Cloning an existing repository.

The other way to create a repository is to clone an existing one. For 
example, if you want to clone this one.

    git clone https://github.com/odinsbane/git_n_click.git
    
Now there will be a folder git_n_click, inside of that folder are the 
files managed by git's version control.

# Managing source code.

The next step is to add some source code to the repository. It is good
practice to keep your source files in their own folder.

    mkdir src
    touch click_example.py
    git status
    
```console
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#	src/
```

It doesn't see the .py file because we haven't added the source folder.

```console
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#	new file:   src/click_example.py
```
    
# Using click.

In the file `click_example.py` is a python script that can be run and
it will print the command line options supplied.

# Using a Virtual Environment.

The next section will outline how to create a virtual environment, and
use it to run our script.

For starters ssh to the other computer in the lab. Once at the login, 
change to the 'Desktop' folder. First we'll create a virtual environment.

```console
    python3 -m "gc-env"
```

After the command has finished there should be a new directory called
`gc-env`. Inside of this directory is our virtual environment. We can
install libraries and not affect the systemwide python. 

There are two ways to use the environment. The first way is to directly
reference the commands. 

```console

./gc-env/bin/pip install --upgrade pip

```

This command will upgrade the pip in are virtual environment. The second
way to use the virtual environment is to activate it.

```console
source ./gc-env/bin/activate
```

Afterwards the prompt should have changed.

```console

which pip

```

Should return, 

>~/Desktop/gc-env/bin/pip

Now to install a `click` to our virtual environment we just run pip again.

```console

pip install click

```

The virtual environment now has click installed (barring any errors).

Then again we can clone this repository, and run our script:

```console
git clone https://github.com/odinsbane/git_n_click.git
python git_n_click/src/click_example.py
```

This should run the program.

#Methods to run our program.

Right now, we have a respository with our source code, and a virtual
environment that we can use to run our code.


## Full path

The previous example we specified the full path to the example code. 
This might not be practical for two reasons. The first reason is obvious
because it gets cumbersome to type `full/path/to/src/code.py`. The 
second reason becomes apparent when we are using modules and packages.

I have created, `example_pkg/pkg_example.py`
If we change directory to `src` we can import either of these scripts 
from the interpretter.

```console
python
>>>import click_example
>>>import pkg_example
```

We cannot run package example though

```console
python example_pkg/pkg_example.py
```

The the error output:

```console
Traceback (most recent call last):
  File "example_pkg/pkg_example.py", line 5, in <module>
    import click_example
ModuleNotFoundError: No module named 'click_example'

```

The reason this doesn't work is because, we need src to be on our `sys.path`


## Path and Python path (not recommended)

The next way to run the program, is to set environment variables. First 
one is call `PATH`, when you run a program, the directories on the path 
will be checked first.

```console

export PATH=/home/username/Desktop/git_n_click/src:$PATH
click_examlpe.py A
```
So now click_example.py is run from anywhere (of course username has to
be the appropriate username. Still we cannot run the pkg_example.py 
it is not on the sys.path.

python will check the environment variable `PYTHONPATH` for paths to add
to our sys.path.

```console
export PYTHONPATH=/home/username/Desktop/git_n_click/src:$PYTHONPATH

```

Now, our paths should be setup ok but 'pkg_example.py' is not in a directory
on our path. We can run it another way.

```console
python -m example_pkg.pkg_example
```

We can do this because it is on the sys.path, and it has a main() function.


## Install to our virtual environment.

The last method is somewhat important. When you write programs that will
be distributed and used they will most likely get installed into a 
virtual environment. 

The way I that I do this is to use a `setup.py` file. One is included.

Go to the source directory and run

```console
pip install .
```

Now we should be able to run our programs.

```consol
click_example
pkg_example
python -m example_pkg.pkg_example
```

