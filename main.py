import crawler
import random


name = (input(f'Hello Contestant! What is your name? '))
player = crawler.Character(name)
print(f'Welcome {player.name}, let begin!\nYou enter the first room.')

# FIRST ROOM 
door_number = random.randint(1,9)
while True:
    print(door_number)
    try:
        ans = int(input('There are 8 doors with the numbers 1 to 8 painted above each. Which door do you want to go through? Pick a number between 1 and 8 to choose. '))
        if ans == door_number:
            print("Right way")
            break
        elif ans in range(1,9) and ans != door_number:
            print(player.dead_end(),'\n')
            continue
        else:
            print(player.make_sense(),'\n')
            continue
    except ValueError:
        print(player.make_sense(),"\n- Enter a number between 1 and 8\n")
        continue


    ans = str(input('Choice between a sausage, a key or a clue? (s/k/c) ' ).lower().strip())
    if ans == 's':
        crawler.Bag().add_item('sausage')
    elif ans == 'k':
        crawler.Bag().add_item('key')
    elif ans == 'c':
        crawler.Bag().add_item('clue')
    elif ans == 'all please':
        crawler.Bag().add_item('sausage')
        crawler.Bag().add_item('key')
        crawler.Bag().add_item('clue')
    else:
        print('That doesn\'t make sense...')

else:
    print('That\'s too bad, maybe next time.')
    exit()
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
    