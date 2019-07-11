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
change to the 'Desktop' folder. 

