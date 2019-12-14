#! /bin/sh

echo " Make requirements.txt"
python3 -m pip freeze > requirements.txt

echo " Push to heroku"
git add requirements.txt
git commit -m "Update dependency"

