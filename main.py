import crawler
import random



ans = str(input('Will you play? (y/n) ').lower().strip())

if ans == 'y':
    player = crawler.Character(input(f'Great! What is your name? '))
    
    print(f'Welcome {player.name}, let begin')
    ans = str(input(f'So {player.name}, you can go left, right or forward? (l/r/f) ').lower().strip())
    if ans == 'l':
        print('DEAD END')
        exit()
    elif ans == 'r':
        print('DEAD END')
    else:
        print('Right way')
        ans = str(input('Choice between a sausage, a key or a clue? (s/k/c) ' ).lower().strip())
        if ans == 's':
            crawler.Bag().add('sausage')
        elif ans == 'k':
            crawler.Bag().add('key')
        elif ans == 'c':
            crawler.Bag().add('clue')
        elif ans == 'all please':
            crawler.Bag().add('sausage')
            crawler.Bag().add('key')
            crawler.Bag().add('clue')
        else:
            print('That doesn\'t make sense...')

else:
    print('That\'s too bad, maybe next time.')
    exit()
if len(crawler.Bag.bag) > 1:
    ans = str(input(f'Now your bag is bulging with a {crawler.Bag.bag[0]}, a {crawler.Bag.bag[1]} and a {crawler.Bag.bag[2]}, choose between right, left or forward? (r/l/f) ').lower().strip())
else:
    ans = str(input(f'Now your carrying a {crawler.Bag.bag[0]} in your bag, choose between right, left or forward? (r/l/f) ').lower().strip())
while True:
    if ans == 'l':
        print('Dead End')
        exit()
    elif ans == 'r':
        print('dead end')
        exit()
    elif ans == 'f':
        print('Right way')
        break
    else:
        print('That doesn\'t make sense..')
        continue

x = random.randint(1,100)
if x <= 30:
    print('You see something moving in the darkness...\n')
    ans = str(input(f'As it moves into the light you can see it\'s a hungry dog... Do you run, play dead, or give him your {crawler.Bag.bag[0]}? (run, play, sausage)').lower().strip())
elif x > 30 and x < 70:
    print('Face door')
elif x == 100:
    print('SECRET')
else:
    print('Face Riddle')
    