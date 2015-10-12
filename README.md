# neuro
Styring af indkaldelser af medicinkontrol

# create local repository
git init
git add .
git commit -m 'Initial'

# create a new repo on github

# connect to github
git remote add origin https://github.com/smerser/neuro.git

# sync with remote if anything there
git pull https://github.com/smerser/neuro.git

# sync
git push -u origin master
git status

# In .gitignore add
neuro/settings.py

# Don't update settings.py
git update-index --assume-unchanged neuro/settings.py
git commit -a -m 'Ignore changes to settings.py'
