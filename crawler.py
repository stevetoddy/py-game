import random

class Character:
    def __init__(self, name):
        self.name = name
        self.turn_tracker = 0
        self.gibberish = 0
        self.bag = []

    def add_item(self, item):
        self.item = self.bag.append(item)


    def dead_end(self):
        x = random.randint(1,101)
        
        if x <= 20:
            self.turn_tracker += 1
            return "** This door won't open **"
        elif x > 20 and x <= 40:
            self.turn_tracker += 1
            return "** This door is locked, you give it a knock... No answer. **"
        elif x > 40 and x <= 60:
            self.turn_tracker += 1
            return "** This door is locked tight **"
        elif x > 60 and x <= 80:
            self.turn_tracker += 1
            return "** This door won't budge **"
        elif x > 80 and x < 95:
            self.turn_tracker += 1        
            return "** AGH! This door is just painted on! Beautiful brushwork though. **"
        elif x >= 95:
            self.turn_tracker += 1        
            return "** This door won't budge.. but wait, there's a clue tacked to the door: \"The Item Merchant is very generous if you're polite! Thank you for listening\" **"

    def make_sense(self):
        x = random.randint(1,101)

        if x <= 40:
            self.gibberish += 1
            return "** That doesn't make sense.. **"
        elif x > 40 and x <= 50:
            self.gibberish += 1
            return "** Please stop with the gibberish! **"
        elif x > 50 and x <= 60:
            self.gibberish += 1
            return "** You must think before you speak **"
        elif x > 60 and x <= 70:
            self.gibberish += 1
            return "** It seems like you know what you're doing, but this doesn't make sense.. **"
        elif x > 70 and x < 95:
            self.gibberish += 1        
            return "** Please consider using your head.. **"
        elif x >= 95:
            self.gibberish += 1        
            return "** If you don't start making sense, I will be forced to have you institutionalised! **"
    
