# INSTALL INSTRUCTIONS

This is an Escape Room Game terminal application to be played in the Linux terminal, that runs on Python3. 

If you are unfamiliar with the terminal, please refer to the relevant documentation below:

- [Mac](https://support.apple.com/en-au/guide/terminal/welcome/mac)
- [Linux](https://help.ubuntu.com/community/UsingTheTerminal)
- [Windows](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2&viewFallbackFrom=powershell-7.1)

You will need Python3 installed to run this application. If you are unfamiliar with Python, please refer to the documentation below. 

- [How to install Python](http://wsvincent.com/install-python/)

Open a terminal and navigate into a directory you would like the application to be.

Use the code snippet below in your terminal to retrieve the application directory from my git repository.

```
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