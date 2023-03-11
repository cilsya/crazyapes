### Setup

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

- Export Conda Environment

```python
conda env export > environment.yml
```

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