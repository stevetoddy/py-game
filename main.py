from lib2to3.pgen2.token import COLONEQUAL
import crawler
import random


name = (input(f'Hello Contestant! What is your name? '))
player = crawler.Character(name)
print(f'Welcome {player.name}, let begin!\nYou enter the first room.')

# # FIRST ROOM 
# door_number = random.randint(1,21)
# while True:
#     print(door_number)
#     try:
#         ans = int(input('There are 20 doors with the numbers 1 to 20 painted above each. Which door do you want to go through? Pick a number between 1 and 20 to choose. '))
#         if ans == door_number:
#             player.turn_tracker += 1
#             print("Right way")
#             break
#         elif ans in range(1,21) and ans != door_number:
#             print(player.dead_end(),'\n')
#             continue
#         else:
#             print(player.make_sense(),'\n- Enter a number between 1 and 20\n')
#             continue
#     except ValueError:
#         print(player.make_sense(),"\n- Enter a number between 1 and 20\n")
#         continue

# print(f"Well done {player.name}! It only took you {player.turn_tracker} (sensible) guesses to find the right door!")

# SECOND ROOM
print(f"That was pretty easy right {player.name}? Well this next room is even easier! All you have to do is get an item from the Item Merchant over there, go say hello!")

while True:
    try:    
        ans = str(input("Choose between a 'sausage', a 'key' or a 'disguise'? ").lower().strip())
        if ans == 'sausage':
            player.add_item('sausage')
            break
        elif ans == 'key':
            player.add_item('key')
            break
        elif ans == 'disguise':
            player.add_item('disguise')
            break
        # elif 'please' in ans and 'thank' not in ans and 'sausage' in ans or 'key' in ans or 'disguise' in ans :
        #     print(f"You are very polite {player.name}! Please take all of my items!")
        #     player.add_item('sausage')
        #     player.add_item('key')
        #     player.add_item('disguise')
        #     break
        elif 'please' in ans and 'sausage' in ans or 'key' in ans or 'disguise' in ans:
            print(f"You are the most polite person I have ever met {player.name}! Please take all of my items and this special Gold Star!")
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
    