import art
from rich import print
import crawler
import random
import time


# HEADING 
art.tprint("ESCAPE  ROOM","tarty1-large")
print(f"[bold magenta]By Stevan Todorovic[/bold magenta]")

crawler.TextPause.enter_continue()

#NAME INPUT
name = (input(f"Hello Contestant! Just before we start, what is your name? "))
player = crawler.Character(name)
print(f"\nWelcome {player.name}!\nYou are about to enter the worlds smallest [bold green]ESCAPE ROOM![/bold green].")
print("Let's begin!")

crawler.TextPause.enter_continue()

# FIRST ROOM
print("You enter the first room to find yourself confront with 20 numbered doors, they all look the same.")
print("A notice on the wall advises you, [yellow]'This room is EASY, just find the unlocked door to proceed!'[/yellow]")

crawler.TextPause.enter_continue()

door_number = random.randint(1,20)
while True:
    print(door_number)
    try:
        ans = int(input("Which door do you want to try? Pick a number between 1 and 20 to choose. "))
        if ans == door_number:
            player.turn_tracker += 1
            print("\nYou push against the door and it slowly gives way, you have found the correct door!\n")
            break
        elif ans in range(1,20) and ans != door_number:
            print(player.dead_end(),'\n')
            continue
        else:
            print(player.make_sense(),"\n-- Enter a number between 1 and 20\n")
            continue
    except ValueError:
        print(player.make_sense(),"\n-- Enter a number between 1 and 20\n")
        continue

print(f"Well done {player.name}! It only took you {player.turn_tracker} (sensible) guesses to find the right door!")

if player.gibberish > 0:
    print(f"\nI won't make a big deal of the {player.gibberish} nonsensical statements you uttered, but next time keep them to yourself please.")


# SECOND ROOM
print(f"\nOK then, that was pretty easy right {player.name}? Well this next room is even easier! \nAll you have to do is get an item from the Item Merchant over there, go and see what he has!\n")

print(f"You trundle over to the Item Merchant and greet them \n'Hello Item Merchant! I am {player.name}, guesser of doors and future item haver!'\n")

print(f"Hello {player.name}, that is an odd way to introduce yourself. I am the Item Merchant and as you might have guessed, I have items. You may pick one to take with you on your adventures\n")
while True:
    try:    
        ans = str(input("Please choose between a 'sausage', a 'key' or a 'disguise'? ").lower().strip())
        if ans == 'sausage':
            print(f"I had a feeling you would pick the sausage {player.name}, you have a hungry look about you. Please, before throwing it down your gullet, maybe hold onto it for a just a little while. You never know when you'll need a tasty treat!")
            player.add_item('sausage')
            break
        elif ans == 'key':
            time.sleep(1)
            print(f"Take this heavy key {player.name}, I'm not sure what door it unlocks but I'm sure you'll figure it out.\n")
            player.add_item('key')
            time.sleep(3)
            break
        elif ans == 'disguise':
            print(f"Here is a very sneaky disguise {player.name}, it will increase your chance of going unnoticed in crowded situations.")
            player.add_item('disguise')
            break
        elif 'please' in ans and 'sausage' in ans or 'key' in ans or 'disguise' in ans:
            print(f"You are a very polite person {player.name}! I have a soft spot in my heart for polite people. Please take all of my items and this special Gold Star!")
            player.add_item('sausage')
            player.add_item('key')
            player.add_item('disguise')
            player.add_item('Gold Star: Manners')
            break
        else:
            print(player.make_sense(),"\n-- Please choose between a 'sausage', a 'key' or a 'disguise'\n")
            continue
    except ValueError:
        print(player.make_sense(),"\n-- Please choose between a 'sausage', a 'key' or a 'disguise'\n")
        continue        
print(player.bag)

# THIRD ROOM
print("Enter a room with a portal hanging in the air and a sign pointing in it's direction. The sign say 'Step through the portal to find the exit!'\n")
enter = input("Do you enter the portal (y/n)? ").lower().strip()
while True:
    try:
        if enter == 'y':
            print("You step through the portal.... \n")
            break
        elif enter == 'n':
            print("You take one look at this dodgy portal business and decide this is not for you. you turn to leave but slip on a loose pebble, stumbling backwards through the portal.... \n")
            break
    except ValueError:
        print(player.make_sense(),"\n-- Please choose between 'y' for Yes or 'n' for NO\n")
        continue

print("Suddenly, you find yourself falling through the air, the ground rushing towards you!\nYou hit the ground with a thud.\n")

final_roll = random.randint(1,3)
luck = 42

# LOCKED DOOR
if final_roll == 1:
    player.ending = "LOCKED DOOR"
    print("You find yourself in a small room, with nothing but a locked door in front of you. This seems to be a bit of a theme here...\n")
    time.sleep(2)
    if 'key' in player.bag:
        print("You remember the key in your bag!")
        if random.randint(41,42) == luck:
            print("You're key unlocks the door! You win!")
            player.win = True
        else:
            print("The key breaks off in the door and the lock remains firmly in place. How unfortunate to be so unlucky in such a place!\n")
            print("The door is locked tight and the portal is no where to be seen. Better get comfortable, it seems this little room will be you home for a while.\n")
    else:
        if random.randint(1,42) == luck:
            print("Through sheer determination and grit, you have willed the locked door open.. How? You are not sure..")
            player.win = True
            player.lucky = True
        else:
            print("The door is locked tight and the portal is no where to be seen. Better get comfortable, it seems this little room will be you home for a while.")

# CANNIBALS
elif final_roll == 2:
    player.ending = "CANNIBALS"
    print("You raise you head to find yourself in a dark corner of a crowded room. Crowded with CANNIBALS! \n")
    time.sleep(2)
    if 'disguise' in player.bag:
        print("You remember the disguise in your bag!")
        if random.randint(41,42) == luck:
            print("You're able to slip past the cannibals and make it outside! You win!")
            player.win = True
        else:
            print("The disguise doesn't work and you are caught! How unfortunate to be so unlucky in such a place!\n")
            print("The cannibals throw you in a pot and start talking excitedly about herbs and spices.\n")
    else:
        if random.randint(1,42) == luck:
            print("The cannibals seem distracted for some reason and you can slip past.. What has distracted them? You are not sure..")
            player.win = True
            player.lucky = True
        else:
            print("The cannibals spot you immediately and start to salivating like Pavlov's dogs. As an avid cook, you can't help but be happy that you'll make one last crowd pleasing meal!")

# CERBERUS
else:
    player.ending = "CERBERUS"
    print("A mighty roar rips through the air, and before you can gather think, you find yourself face to face to face to face with the 3 headed beast of legend, Cerberus!\n")
    time.sleep(2)
    if 'sausage' in player.bag:
        print("You remember the sausage in your bag!")
        if random.randint(41,42) == luck:
            print("You gingerly offer the sausage to the closest head. As you hand trembles, the grotesque monster sniffs the sausage and lets out a gleeful squeal!\n")
            print("Turns out Cerberus loves snags and if now your friend. You win!\n")
            player.win = True
        else:
            print("You gingerly offer the sausage to the closest head. As you hand trembles, the grotesque monster sniffs the sausage and lets out an angry growl.\n")
            print("You hadn't noticed but it turns out it was a lamb and rosemary sausage, and Cerberus hates lamb even more than he hates rosemary. You are eaten.\n")
    else:
        if random.randint(1,42) == luck:
            print("Cerberus notices your kind eyes and becomes enthralled with you. You are able to walk past it without issue. You win!\n")
            player.win = True
            player.lucky = True
        else:
            print("Without a moments pause, the closest of Cerberus's terrible heads snaps towards in your direction and takes a mouthful of you.\n")
            print("Unfortunately it included some important parts that make up 'you', and you fall over dead.")

# CREDITS
player.win_lose()

if player.win == True:
    player.credits_win()
else:
    player.credits_lose()