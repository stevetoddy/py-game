# README
## INSTALLATION INSTRUCTIONS

This is an Escape Room Game terminal application to be played in the Linux terminal, that runs on Python3.  

If you are unfamiliar with the terminal, please refer to the relevant documentation below:

- [Mac](https://support.apple.com/en-au/guide/terminal/welcome/mac)
- [Linux](https://help.ubuntu.com/community/UsingTheTerminal)
- [Windows](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2&viewFallbackFrom=powershell-7.1)

You will need Python3 installed to run this application. If you are unfamiliar with Python, please refer to the documentation below.  

- [How to install Python](http://wsvincent.com/install-python/)

Open a terminal and navigate into a directory you would like the application to be.

Please check you have virtualenv installed, this will be required if you do not want the python packages this application requires to be installed globally on your system.  

If you are unsure if you have virtualenv installed, please refer to the documentation below.

[Virtual Environment Installation](https://www.pythonforbeginners.com/basics/how-to-use-python-virtualenv)

One you have confirmed you have virtualenv installed, use the code snippet below in your terminal to retrieve the application directory from my git repository.

```https://pypi.org/project/clearing/
git clone https://github.com/stevetoddy/py-game.git
```

Navigate into the ‘py-game’ directory.  

Now you can run the application.  
The following instructions will create a virtual environment and install the Python packages the application requires to run:  

```
source escape_room.sh
```

If you would like, you can select you in game name before launching the application using the snippet below:

```
source escape_room.sh name
```

Replacing name with the name you would like in game.

For example:  

```
source escape_room.sh Steve
```

Use this command anytime you would like to play the game, with or without you name.  
You will have the chance to enter your name after launching the application if you do not provide it.  
Just make sure you are in the ‘py-game’ directory that you received from my Git repository.

Once you are finished with the game, you should deactivate the virtual environment we set up for it.  
This is done by entering ‘deactivate’ into your terminal, as shown below.

```
deactivate
```

Enjoy the game!

---

## DEPENDENCIES REQUIRED

- Windows, macOS, Ubuntu or another modern OS
- Python 3.7 or later
- Virtualenv 20.0 or later

---

## SYSTEM REQUIREMENTS

- If you are able to run a modern OS, you will be able to run this terminal application.  

---

## STYLE GUIDE

- [PEP 8](https://peps.python.org/pep-0008/)

---

## FEATURES

- You may enter you name when launching the application by placing you name after the command shown earlier to run. This is detailed in the above section titled Installation Instructions.  

- The first room will have you try and guess the correct door to go through. The correct door is randomly generated each new game. If the player chooses the incorrect door they will get a randomly generated message telling them the bad news. If the player enters a door number out of the range of the set amount of doors, they will receive a randomly selected message advising them they need to enter a number in the correct range and some flavour text telling them to make sense. There is a secret message that has a low chance of displaying when the player selects a wrong door.  

- The two response generators both work in a similar fashion. One is to give a response when the player selects the wrong door in the first room. There are 5 possible responses, with the most generic one having a higher chance of being displayed than the others. There is one message that has a low chance of being displayed and has a clue for the player about the next room. The second response generator will return a line asking the player to 'please make sense', in a few different ways. Again, the most generic responses have a higher chance of being displayed. Every time either of these messages are displayed, they are noted in the player instance so we can give the player a readout of the amount of guesses taken to get through the first room, and also how many time the application asked the player to 'make sense'.

- In the second room you meet the Item Merchant, they have 3 items you can choose from and each will help you get past a different ending encounter, which I will cover in more detail in the next feature below. The Item Merchant has a secret too, if you ask nicely for an item, they will give you all of the item and the secret Gold Star.  

- The final room will have you face one of three possible endings, a locked door, a room full of cannibals or a monster. These encounters are randomly chosen, all with even weighting. If you picked the key in the previous room, you will have a one in two chance of getting past the locked door, but if you didn't choose the key, you will have a one in forty-two chance of getting past the locked door. If you do not get past the encounter, you lose the game. If you chose the sausage, you will have the increase against the monster. If you pick the disguise, you will have the increased chance against the room of cannibals. After you either win or lose, you will be show a win or lose statement that relates to the encounter you faced.  

- Upon winning oir losing, the player will be given either the winners stats board or the loser stats board. Both display the same stats but the winners board have a medal that says you won, the losers board has a skull and cross bones in the medals place. Both boards display how many guesses it took the player to get through the first room, which items they chose, if they found the gold star, which ending they encountered and how many nonsense statements they made throughout the run.  

- I have a screen clearing, text break that breaks up the story. It has an inbuilt clearing function that clears the terminal screen, a sleep timer to give the application a cadence and a 'hit enter to continue' function. 

---

## TESTS

### 1st Test – Test dead_end()  
This test is to show my dead_end() method works as intended. The dead_end() method was created to give a random response to the player while guessing doors in the first room. If the player guesses the wrong door, in the acceptable range (1-20) the dead_end() method will give the player back a randomly picked response from a list of five possible responses.  

I have created a list called 'options_dead_end' and it is is populated with all possible results from dead_end(). When method is called, the result is checked against this list and will pass if the returned result is in the list ‘options_dead_end’.

### 2nd Test – Test make_sense()  
This test is to show my make_sense() method works as intended. The make_sense() method was created to give a random response to the player whenever they enter an input that is not expected by the program and is not within an acceptable range. If the player enters an input that is not recognised the method make_sense() will return one of five possible statements, picked at random.  

I have created a list called 'options_make_sense' and it is is populated with all possible results from make_sense(). When the method is called, the result is checked against this list and will pass if the returned result is in the list ‘options_make_sense’.

### 3rd Test – Test add_item()  
This test is to show my add_item() method works as intended. In this test I give the method add_items() an 'item' called "TEST_ITEM" and then assert that "TEST_ITEM" was added to the list called 'bag' in the player instance.  

---

## LINK TO GITHUB REPOSITORY

- [Github Repository](https://github.com/stevetoddy/py-game/tree/main)

---

## LINK TO TRELLO BOARD 

- [Terminal Application Trello Board](https://trello.com/c/UwDrglhj/22-documentation)

---  

## IMPLEMENTATION PLAN

I have my Trello board as my main point of design implementation, and I will give an overview of the design implementation here.  

## Brainstorming  

Initially the idea was to create a dungeon crawler with many items that would effect the outcome of certain encounters. After attempting to start this idea, I noticed that moving in and out of areas was not possible in the time frame given and my skill to that point. I reused some ideas and settled on the escape room idea, having a series of puzzle like rooms. I kept an element of the items idea with the Item Merchant and the third room, where items effect the outcome of the encounter. 

## Initial To Do List

All checklists and detailed design plans related to the implementation plan are located on the Trello board [here](https://trello.com/c/UwDrglhj/22-documentation).

- Start Trello board
- Write out this implementation plan
- Start Github repository
- Write bones of idea into code to make sure it is viable
- Flesh out code with a bit of story
- Work on first feature, response generators
- Look for modules to make the application look nicer
- Implement modules to make application look nicer in the form of a starting splash screen, highlighted colour text for emphasis, pictures of end encounters, pictures of winning and losing
- Make a text break so the user can 'press enter to continue'
- Screen clearing option
- Time delay options to give the application pacing
- Flesh out main puzzles
  - First room
  - Second room
  - Third room
  - Ending board (win and lose) with run stats
- Write tests for features
- Bash script with command line args
  - launch virtual environment
  - install required python packages
  - launch game
  - give user option to give their name as a command line argument
- Make walkthrough video 
  - needs slide deck 
  - talk about features in game and code
  - show a run through of game if time 
  - upload and link
- QA testing throughout the application before submission

---

## REFERENCES

Ascii Art was sourced from the following resources:  
Unknown Artist - https://ascii.co.uk/art/skulls  
Joan G. Stark - https://www.asciiart.eu/miscellaneous/awards  
Joan G. Stark - https://ascii.co.uk/art/cauldron  
b'ger - https://ascii.co.uk/art/cerberus  
ejm - https://ascii.co.uk/art/doors  

Python packages were sourced from the following resources:  
clearing - https://pypi.org/project/clearing/  
rich - https://pypi.org/project/rich/  
art - https://pypi.org/project/art/  

All other packages are builtin or created by Stevan Todorovic. 