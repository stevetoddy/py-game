from lib2to3.pgen2.token import COLONEQUAL
import crawler
import random
import time


name = (input(f'Hello Contestant! What is your name? '))
player = crawler.Character(name)
print(f'Welcome {player.name}, let begin!\nYou enter the first room.')

# FIRST ROOM 
door_number = random.randint(1,20)
while True:
    print(door_number)
    try:
        ans = int(input('There are 20 doors with the numbers 1 to 20 painted above each. Which door do you want to go through? Pick a number between 1 and 20 to choose. '))
        if ans == door_number:
            player.turn_tracker += 1
            print("\nYou push against the door and it slowly gives way, you have found the correct door!\n")
            break
        elif ans in range(1,20) and ans != door_number:
            print(player.dead_end(),'\n')
            continue
        else:
            print(player.make_sense(),'\n- Enter a number between 1 and 20\n')
            continue
    except ValueError:
        print(player.make_sense(),"\n- Enter a number between 1 and 20\n")
        continue

print(f"Well done {player.name}! It only took you {player.turn_tracker} (sensible) guesses to find the right door!")
time.sleep(1.5)
if player.gibberish > 0:
    print(f"\nI won't make a big deal of the {player.gibberish} nonsensical statements you uttered, but next time keep them to yourself please.")
time.sleep(1.5)

# SECOND ROOM
print(f"\nOK then, that was pretty easy right {player.name}? Well this next room is even easier! \nAll you have to do is get an item from the Item Merchant over there, go and see what he has!")
time.sleep(2)
print(f"You trundle over to the Item Merchant and greet them, 'Hello Item Merchant! I am {player.name}, guesser of doors and future item haver!'\n")
time.sleep(1)
print(f"Hello {player.name}, that is an odd way to introduce yourself. I am the Item Merchant and as you might have guessed, I have items. You may pick one to take with you on your adventures\n")
while True:
    try:    
        ans = str(input("Please choose between a 'sausage', a 'key' or a 'disguise'? ").lower().strip())
        if ans == 'sausage':
            print(f"I had a feeling you would pick the sausage {player.name}, you have a hungry look about you. Please, before throwing it down your gullet, maybe hold onto it for a just a little while. You never know when you'll need a tasty treat!")
            player.add_item('sausage')
            break
        elif ans == 'key':
            print(f"Take this heavy key {player.name}, I'm not sure what door it unlocks but I'm sure you'll figure it out.")
            player.add_item('key')
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
            print(player.make_sense(),"\n- Please choose between a 'sausage', a 'key' or a 'disguise'\n")
            continue
    except ValueError:
        print(player.make_sense(),"\n- Please choose between a 'sausage', a 'key' or a 'disguise'\n")
        continue        
print(player.bag)

# if len(crawler.Bag.bag) > 1:
#     ans = str(input(f'Now your bag is bulging with a {crawler.Bag.bag[0]}, a {crawler.Bag.bag[1]} and a {crawler.Bag.bag[2]}, choose between right, left or forward? (r/l/f) ').lower().strip())
# else:
#     ans = str(input(f'Now your carrying a {crawler.Bag.bag[0]} in your bag, choose between right, left or forward? (r/l/f) ').lower().strip())
# while True:
#     if ans == 'l':
#         print('Dead End')
#         exit()
#     elif ans == 'r':
#         print('dead end')
#         exit()
#     elif ans == 'f':
#         print('Right way')
#         break
#     else:
#         print('That doesn\'t make sense..')
#         continue

# x = random.randint(1,100)
# if x <= 30:
#     print('You see something moving in the darkness...\n')
#     ans = str(input(f'As it moves into the light you can see it\'s a hungry dog... Do you run, play dead, or give him your {crawler.Bag.bag[0]}? (run, play, sausage)').lower().strip())
# elif x > 30 and x < 70:
#     print('Face door')
# elif x == 100:
#     print('SECRET')
# else:
#     print('Face Riddle')
    