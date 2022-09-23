import random
import time
from sys import argv
import clearing
import art
from rich import print  # THIS IMPORT WILL OVERRIDE THE BUILTIN PRINT FUNCTION
import pause_continue
import crawler


# TELLING PYLINT TO IGNORE LONG LINE AS THEY ARE ALL OUTPUT
# & TO IGNORE ANOMALOUS BACKSLASHES FROM THE ASCII ART
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=line-too-long

clearing.clear()

#HEADING
art.tprint("\n\nESCAPE  ROOM","tarty1-large")
print("[bold magenta]By Stevan Todorovic[/bold magenta]")

pause_continue.TextPause.enter_continue()

#NAME INPUT
if len(argv) <= 1:
    while True:
        NAME = (input("\n\nHello Contestant! Just before we start, what is your name? "))
        if NAME == "":
            print ("[red]Please enter your name[/red]")
            continue
        player = crawler.Character(NAME)
        print(f"\nWelcome {player.name}!\n\nYou are about to enter the worlds smallest [bold green]ESCAPE ROOM![/bold green].")
        break
else:   #IF NAME IS GIVEN AS ARGUMENT THEN GAME WILL SKIP ASKING THE PLAYER
    NAME = argv[1]
    player = crawler.Character(NAME)
    print(f"\n\nWelcome {player.name}!\n\nYou are about to enter the worlds smallest [bold green]ESCAPE ROOM![/bold green].")

print("\n[bold yellow]Let's begin![/bold yellow]")

pause_continue.TextPause.enter_continue()

#FIRST ROOM WELCOME
print("\n\nYou enter the first room to find yourself confront with 20 numbered doors, they all look the same.")
print("A notice on the wall advises you, [yellow]'This room is EASY, just find the unlocked door to proceed!'[/yellow]")

pause_continue.TextPause.enter_continue()

#FIRST ROOM GUESSING GAME
door_number = random.randint(1,20)
while True:
    try:
        ans = int(input("\n\nWhich door do you want to try? Pick a number between 1 and 20 to choose: "))
        if ans == door_number:
            player.turn_tracker += 1
            print("\n[bold green]You push against the door and it slowly gives way, you have found the correct door![/bold green]\n")
            time.sleep(1.5)
            break
        if ans in range(1,21) and ans != door_number:
            print(player.dead_end(),'\n')
            continue
        print(player.make_sense(),"\n[red]-- Enter a number between 1 and 20 --[/red]\n")
        continue

    except ValueError:
        print(player.make_sense(),"\n[red]-- You must pick a NUMBER between 1 and 20 --[/red]\n")
        continue

pause_continue.TextPause.enter_continue()

#FIRST ROOM COMPLETION SCREEN
print(f"\n\nWell done {player.name}! It only took you {player.turn_tracker} (sensible) guesses to find the right door!")

time.sleep(1)

if player.gibberish > 0:
    print(f"\nI won't make a big deal of the {player.gibberish} nonsensical statements you uttered, but next time keep them to yourself please.")

pause_continue.TextPause.enter_continue()

#SECOND ROOM WELCOME
print(f"\n\nOK then, that was pretty easy right {player.name}? Well this next room is even easier!")
print("All you have to do is get an item from the Item Merchant over there, go and see what he has!\n")

pause_continue.TextPause.enter_continue()

print(f"\n\nYou trundle over to the Item Merchant and greet them \n'Hello Item Merchant! I am {player.name}, guesser of doors and future item haver!'\n")

time.sleep(1.5)

print(f"'Hello {player.name}, those are some strange and presumptuous titles you have there.'")
print("\n'I am the Item Merchant and as you might have guessed, I have items. You may pick one to take with you on your adventures'\n")

pause_continue.TextPause.enter_continue()

#SECOND ROOM ITEM PICKER
while True:
    ANS = str(input("\n\nPlease choose between a 'sausage', a 'key' or a 'disguise'? ").lower().strip())
    if ANS == 'sausage':
        print(f"\n'I had a feeling you would pick the sausage {player.name}, you have a hungry look about you. Please, before throwing it down your gullet, maybe hold onto it for a just a little while. You never know when you will need a tasty treat!'")
        player.add_item('sausage')
        pause_continue.TextPause.enter_continue()
        break
    if ANS == 'key':
        print(f"\n'Take this heavy key {player.name}, I am not sure what door it unlocks but I am sure you will figure it out.'\n")
        player.add_item('key')
        pause_continue.TextPause.enter_continue()
        break
    if ANS == 'disguise':
        print(f"\n'Here is a very sneaky disguise {player.name}, it will increase your chance of going unnoticed in crowded situations.'")
        player.add_item('disguise')
        pause_continue.TextPause.enter_continue()
        break
    if 'please' in ANS and 'sausage' in ANS or 'key' in ANS or 'disguise' in ANS:
        print(f"\n'You are a very polite person {player.name}! I have a soft spot in my heart for polite people. Please take all of my items and this special [bold yellow]Gold Star![/bold yellow]'")
        player.add_item('sausage')
        player.add_item('key')
        player.add_item('disguise')
        player.add_item('Gold Star: Manners')
        pause_continue.TextPause.enter_continue()
        break
    print(player.make_sense(),"\n-- Please choose between a 'sausage', a 'key' or a 'disguise'\n")
    continue

#THIRD ROOM PORTAL CHOICE
print("\n\nYou leave the merchant and enter a room with a portal hanging in the air. A sign pointing in its direction says 'Step through the portal to find the exit!'\n")
while True:
    enter = input("Do you enter the portal (y/n)? ").lower().strip()
    if enter == 'y':
        print("You step through the portal.... \n")
        break
    if enter == 'n':
        print("You take one look at this dodgy portal business and decide this is not for you. You turn to leave but slip on a loose pebble, stumbling backwards.... \n")
        break
    if enter == "":
        print(player.make_sense())
        continue
    print(player.make_sense(),"\n-- Please choose between 'y' for Yes or 'n' for NO\n")
    continue

#PORTAL FALL
time.sleep(3)

print("Suddenly, you find yourself falling through the air, the ground rushing towards you!\n")

time.sleep(3)

print("You hit the ground with a thud.\n")

pause_continue.TextPause.enter_continue()


#FINAL ROOM DECIDER
final_roll = random.randint(1,3)
LUCK = 42

#LOCKED DOOR ENDING
if final_roll == 1:
    player.ending = "LOCKED DOOR"
    print("\n\nYou find yourself in a small room, with nothing but a locked door in front of you. This seems to be a bit of a theme here...\n")
    print("               _______________")
    print("              |  ___________  |")
    print("              | |  _ _ _ _  | |")
    print("              | | | | | | | | |")
    print("              | | |-+-+-+-| | |")
    print("              | | |-+-+-+-| | |")
    print("              | | |_|_|_|_| | |")
    print("              | |           | |")
    print("              | |         ()| |")
    print("              | |         ||| |")
    print("              | |         ()| |")
    print("              | |           | |")
    print("              | |           | |")
    print("              | |           | |")
    print("              |_|___________|_|")
    pause_continue.TextPause.enter_continue()

    #WITH ITEM
    if 'key' in player.bag:
        print("\n\nYou remember the key in your bag!")

        pause_continue.TextPause.enter_continue()

        #WITH ITEM WIN
        if random.randint(41,42) == LUCK:
            print("\n\nYou're key unlocks the door! You win!")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITH ITEM LOSE
        else:
            print("\n\nThe key breaks off in the door and the lock remains firmly in place. How unfortunate to be so unlucky in such a place!\n")
            time.sleep(1.5)
            print("\nThe door is locked tight and the portal is no where to be seen. Better get comfortable, it seems this little room will be you home for a while.")
            print("\n\n[bold red]HOW UNLUCKY![/bold red]")

            pause_continue.TextPause.enter_continue()

    #WITHOUT ITEM
    else:
        #WITHOUT ITEM WIN
        if random.randint(1,42) == LUCK:
            print("\n\nThrough sheer determination and grit, you have willed the locked door open.. How? You are not sure..")
            print("\n\n[bold green]HOW LUCKY![/bold green]")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITHOUT ITEM LOSE
        else:
            print("\n\nThe door is locked tight and the portal is no where to be seen. Better get comfortable, it seems this little room will be you home for a while.")

            pause_continue.TextPause.enter_continue()

# CANNIBALS ENDING
elif final_roll == 2:
    player.ending = "CANNIBALS"
    print("\n\nYou raise you head to find yourself in a dark corner of a crowded room. Crowded with CANNIBALS! \n")
    print("They are all looking longingly into an empty cauldron in the center of the room\n")
    print("                      ( ")
    print("                       )  ) ")
    print("                   ______(____")
    print("                  (___________) ")
    print("                   /         \ ")
    print("                  /           \ ")
    print("                 |             | ")
    print("             ____\             /____")
    print("            ()____'.__     __.'____() ")
    print("                 .'` .'```'. `-. ")
    print("                ().'`       `'.() ")

    pause_continue.TextPause.enter_continue()

    #WITH ITEM
    if 'disguise' in player.bag:
        print("\n\nYou remember the disguise in your bag!")

        pause_continue.TextPause.enter_continue()

        #WITH ITEM WIN
        if random.randint(41,42) == LUCK:
            print("\n\nYou are able to slip past the cannibals and make it outside! You win!")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITH ITEM LOSE
        else:
            print("\n\nThe disguise doesn't work and you are caught! How unfortunate to be so unlucky in such a place!\n")
            print("The cannibals throw you in a pot and start talking excitedly about herbs and spices.")
            print("\n\n[bold red]HOW UNLUCKY![/bold red]")

            pause_continue.TextPause.enter_continue()

    #WITHOUT ITEM
    else:
        #WITHOUT ITEM WIN
        if random.randint(1,42) == LUCK:
            print("\n\nThe cannibals seem distracted for some reason and you can slip past.. What has distracted them? You are not sure..")
            print("\n\n[bold green]HOW LUCKY![/bold green]")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITHOUT ITEM LOSE
        else:
            print("\n\nThe cannibals spot you immediately and start to salivating like Pavlov's dogs. As an avid cook, you can't help but be happy that you will make one last meal!")

            pause_continue.TextPause.enter_continue()

# CERBERUS ENDING
else:
    player.ending = "CERBERUS"
    print("\n\nA mighty roar rips through the air! Before you can think, you find yourself face to face to face to face with the three headed beast of legend, Cerberus!\n")
    print("                        /\_/\____, ")
    print("              ,___/\_/\ \  ~     / ")
    print("              \     ~  \ )   XXX ")
    print("                XXX     /    /\_/\___, ")
    print("                   \   /====/   ~    / ")
    print("                    )=/     \    XXX ")
    print("                   _|    / \ \_/ ")
    print("                ,-/   _  \_/   \ ")
    print("               / (   /____,__|  )")
    print("              (  |_ (    )  \) _|")
    print("             _/ _)   \   \__/   (_")
    print("            (,-(,(,(,/      \,),),)")

    pause_continue.TextPause.enter_continue()

    #WITH ITEM
    if 'sausage' in player.bag:
        print("\n\nYou remember the sausage in your bag!")

        pause_continue.TextPause.enter_continue()

        #WITH ITEM WIN
        if random.randint(41,42) == LUCK:
            print("\n\nYou gingerly offer the sausage to the closest head. As you hand trembles, the grotesque monster sniffs the sausage and lets out a gleeful squeal!\n")
            print("Turns out Cerberus loves snags and is now your friend. You win!\n")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITH ITEM LOSE
        else:
            print("\n\nYou gingerly offer the sausage to the closest head. As you hand trembles, the grotesque monster sniffs the sausage and lets out an angry growl.\n")
            print("You had not noticed but it turns out it was a lamb and rosemary sausage, and Cerberus hates lamb even more than he hates rosemary. You are eaten instead.")
            print("\n\n[bold red]HOW UNLUCKY![/bold red]")

            pause_continue.TextPause.enter_continue()

    #WITHOUT ITEM
    else:

        #WITHOUT ITEM WIN
        if random.randint(1,42) == LUCK:
            print("\n\nCerberus notices your kind eyes and becomes enthralled with you. You are able to walk past it without issue. You win!")
            print("\n\n[bold green]HOW LUCKY![/bold green]")
            player.win = True

            pause_continue.TextPause.enter_continue()

        #WITHOUT ITEM LOSE
        else:
            print("\n\nWithout a moments pause, the closest of Cerberus\'s terrible heads snaps in your direction and takes a mouthful of you.\n")
            print("Unfortunately it included some important parts that make up 'you', and you fall over dead.")

            pause_continue.TextPause.enter_continue()

# WIN OR LOSE CREDITS
player.win_lose()

pause_continue.TextPause.enter_continue()

#GOLD STAR CHECK
if "Gold Star: Manners" in player.bag:
    player.gold_star = True

#WIN OR LOSE CHECK
if player.win is True:
    player.credits_win()
else:
    player.credits_lose()
