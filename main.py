import crawler


# bag = []
ans = str(input("Will you play? (y/n) ").lower().strip())
name = None
if ans == 'y':
    name = input(f'Great! What is your name? ')
    print(f'Welcome {name}, let begin')
    player = crawler.Character(f'{name}')
    ans = str(input(f'So {name}, you can go left, right or forward? (l/r/f) ').lower()) 
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
        elif ans == 'all please':
            crawler.Bag().add('sausage')
            crawler.Bag().add('key')
            crawler.Bag().add('clue')
        else:
            crawler.Bag().add('clue')
    print(crawler.Bag.bag)
    print(crawler.Character, crawler.Bag.bag)
else:
    print("That's too bad, maybe next time.")
    exit()
if len(crawler.Bag.bag) > 1:
    ans = str(input(f'Now your bag is bulging with a {crawler.Bag.bag[0]}, a {crawler.Bag.bag[1]} and a {crawler.Bag.bag[2]}, choose between right, left or forward? (r/l/f) ').lower().strip())
else:
ans = str(input(f'Now your bag is bulging with a {crawler.Bag.bag[0]}, choose between right, left or forward? (r/l/f) ').lower().strip())
if ans == 'l':
    print('Dead End')
elif ans == 'r':
    print('dead end')
else:
    print('Right way')
    ans = str(input(f'You come across a hungry dog... Do you run, play dead, or give him your {crawler.Bag.bag[0]}? (run, play, sausage)').lower().strip())