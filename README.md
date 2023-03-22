### Setup

#### From scratch

- Create conda environment

```system
conda create --name gamemon python=3.6

```

- Activate conda environment

```system
conda activate gamemon
```

- Install pywin32
	- __NOTE:__ [For installation on Linux](https://www.geeksforgeeks.org/how-to-install-pywin32-on-linux/)

```system
conda install -c anaconda pywin32
```

- Install wxpython

```system
conda install -c conda-forge wxpython
```

- Install flake8 for linting

```system
conda install flake8
```

- Also install `importlib-metadata` manually if you are getting `ModuleNotFoundError: No module named 'importlib_metadata'` errors when trying to run `flake8 .`

```system
conda install importlib-metadata
```

- Install `nose2` for unit testing

```system
pip install nose2
```

- Export Conda Environment

```python
conda env export > environment.yml
```

#### Create Environment from `.yml` file on (This was made on Windows Platform)

- Load Conda Environment

```python
conda env create -f environment.yml
```

### Conda Commands

- [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)

# Git Commands

- [General GitHub Setup](https://support.codebasehq.com/articles/repositories/pushing-to-a-repository)

#### Get and Set Username and Email

- To know username for __EVERY__ repository

```system
git config --global user.name
```


- To know email

```system
git config --global user.email
```

- To set username for __EVERY__ repository

```system
git config --global user.name "Mona Lisa"
```

- To know email for __EVERY__ repository

```system
git config --global user.email "youremail@yourdomain.com"
```

- To get remote repository

```system
git remote -v
```

- To set remote repository

```system
git remote add origin ssh://login@IP/path/to/repository
```

- Set origin

```system
git remote set-url origin https://github.com/user/another-repo
```

- Rename branch 

```system
git branch -m old-name new-name
```

- For example

```system
git branch -m master main
```

- To push to repo

```system
git push <remote> <branch>
```

- So, for example

```system
git push origin main
```

- By default, Git chooses origin for the remote and your current branch as the branch to push.

```system
git push
```

- You might have to save upstream branch

```system
git push --set-upstream origin main
```

- To create a new branch

```system
git branch dev
```

- To switch to a branch

```system
git switch dev
```

- Or force push to override the repo. [Force "git push" to overwrite remote files](https://stackoverflow.com/questions/10510462/force-git-push-to-overwrite-remote-files)

```system
git push -f <remote> <branch>
```

- [If a folder is not being tracked but it is not in gitignore](https://stackoverflow.com/questions/49547886/git-not-tracking-folder-and-files)
    - Removing `gitlink`

example:

```system
git rm --cached apps/kv
# no trailing slash!
```

- [How to Clone or Download a Specific Branch from Github](https://www.howtogeek.com/devops/how-to-clone-or-download-a-specific-branch-from-github/)
    - The first will clone the entire repo, and checkout the dev branch. The second, using the --single-branch flag, will only fetch updates that pertain to the branch being downloaded. This can be faster if you have a lot of files on other branches you don’t care about.

```system
git clone --branch dev https://github.com/username/Repo.git
git clone --branch dev --single-branch https://github.com/username/Repo.git
```

- [how to checkout a specific commit from git](https://stackoverflow.com/questions/50942519/how-to-checkout-a-specific-commit-from-git)

Check ID

```system
git log
```

If you really want to lose everything:

```system
git reset --hard 9ce920d
```

- [Visualizing branch topology in Git](https://stackoverflow.com/questions/1838873/visualizing-branch-topology-in-git)

```system
git log --graph
```

or

```system
gitk
```

- Both also accept --all, which will show all the branches instead of just the current one.

```system
git log --graph --decorate --oneline
```

- [Git Graph Visualizes Branches in VS Code for Free](https://ardalis.com/git-graph-visualizes-branches-in-vs-code-for-free/)
    - [Git Graph](https://marketplace.visualstudio.com/items?itemName=mhutchie.git-graph)
    - [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens)

- The git merge Command
    - https://www.delftstack.com/howto/git/git-merge-branch-into-another-branch/

    - Run the `git status` command. This will point the HEAD to the recipient branch.

    - Switch to the recipient branch using the git checkout <recipient branch>` command.

    - Update your master branch with the latest remote commits using the git fetch and git pull commands.
    Merge the branches by running the `git merge <your branch name here>` command.

### Run unit tests

- Quick answer for this code base
    - All the unit tests are in the unittests folder
```python
nose2 -v -s src/unittests
```

- Using [nose](https://nose.readthedocs.io/en/latest/) to run tests
- Tests are run using [unittest](https://docs.python.org/3/library/unittest.html)
- Test are made next to the code with `_test` prepended to the function name.
- When running `nose2` in the terminal, any file with the word `test` (i.e. `test_calculation.py`) will be checked for unit tests.
- To run nose2 (in general):

```system
nose2 -v
```

- Look at the `nose2_help.txt` file saved at the root for help on how to use nose2.

### Run linters

- To run flake8 on all files in subfolder

```system
flake8 .
```


```system
flake8 ./
```

- To run flake8 on all files on a file

```system
flake8 <filename.py>
```

- To output flake8 to a text file

```system
flake8 . > flake8_fixes.txt
```

## Setup Nose2 for unit test

- Can use `nose2.cfg` to configure (possibly ignore files to test) as illustrated in [this documentation.](https://docs.nose2.io/en/latest/usage.html#specifying-tests-to-run)

## Setup flake8 for linting in VSCode

- [Using Flake8 in VSCode](https://stackoverflow.com/questions/54160207/using-flake8-in-vscode)

- [Open settings.json in VS Code](https://stackoverflow.com/questions/65908987/vs-code-how-to-open-settings-json-file)

- To run Pylint

Example:
```system
pylint <filename.py>
```

```system
pylint rt_static.py
```

- [Linting Python in Visual Studio Code](https://code.visualstudio.com/docs/python/linting)

# Setup developer documentation

- [Auto-Generated Python Documentation with Sphinx (See comments for update fix](https://www.youtube.com/watch?v=b4iFyrLQQh4)

- [How to Document using Sphinx: Introduction](https://www.youtube.com/watch?v=_xDgNKc6-AI)
- [How to Document using Sphinx: Part 1—Setting up](https://www.youtube.com/watch?v=WcUhGT4rs5o)
- [How to Document using Sphinx: Part 2—Building and Changing Themes](https://www.youtube.com/watch?v=RvJ54ADcVno)
- [How to Document using Sphinx: Part 3—Formatting with reStructuredText](https://www.youtube.com/watch?v=DSIuLnoKLd8)
- [How to Document using Sphinx: Part 4—Using Git to push docs to GitHub](https://www.youtube.com/watch?v=CqR1b0Y-o5k)
- [Carol Willing - Practical Sphinx - PyCon 2018](https://www.youtube.com/watch?v=0ROZRNZkPS8)
- [Bryson Tyrrell - Your code should document itself! Embedding documentation into your Python projects](https://www.youtube.com/watch?v=JQ8RQru-Y9Y)

# Add column vertical ruler in VS Code
- [Vertical rulers in Visual Studio Code](https://stackoverflow.com/questions/29968499/vertical-rulers-in-visual-studio-code)

# Visual Studio Code open tab in new window
- [Visual Studio Code open tab in new window](https://stackoverflow.com/questions/43362133/visual-studio-code-open-tab-in-new-window)

- First press `Ctrl+K`,then release，then press `O` (the letter, not the
number)

# Epsilon with NumPy Arrays

- Probably want to use [this version from the NumPy documentation](https://numpy.org/doc/stable/reference/generated/numpy.allclose.html)

```python
numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)
```

- [Stackoverflow explanation](https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise)

```python
np.array_equal(A,B)  # test if same shape, same elements values
np.array_equiv(A,B)  # test if broadcastable shape, same elements values
np.allclose(A,B,...) # test if same shape, elements have close enough values
```