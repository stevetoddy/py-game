class Character:
    def __init__(self, name, health = 3, attack = 1):
        self.name = name
        self.health = health
        self.attack = attack
        # self.bag = Items(None, None, None)


class Bag:
    bag = []

    def add(self, item):
        self.add = self.bag.append(item)