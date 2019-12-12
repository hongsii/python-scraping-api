#! /bin/sh

echo " Make requirements.txt"
python -m pip freeze > requirements.txt

echo " Push to heroku"
git add requirements.txt
git commit -m "Update dependency"
git push heroku master

