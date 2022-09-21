#!/bin/bash

# create venv
virtualenv .T1A3venv
source .T1A3venv/bin/activate 

# INSTALL required PACKAGES from requirements.txt file
pip install -r requirements.txt 

# EXECUTE APP
# First argument can be entered and will be used as players name, if 
# no argument is passed player will be prompted to enter their name
# in game.
python3 main.py $1

