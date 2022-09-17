
import random
import art
from rich import print


class Character:
    def __init__(self, name):
        self.name = name
        self.turn_tracker = 0
        self.gibberish = 0
        self.bag = []
        self.win = False
        self.ending = " "
        self.lucky = False

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

        if x <= 60:
            self.gibberish += 1
            return "** That doesn't make sense.. **"
        elif x > 60 and x <= 70:
            self.gibberish += 1
            return "** Please stop with the gibberish! **"
        elif x > 70 and x <= 80:
            self.gibberish += 1
            return "** You must think before you speak **"
        elif x > 80 and x <= 90:
            self.gibberish += 1
            return "** It seems like you know what you're doing, but this doesn't make sense.. **"
        elif x > 90 and x < 95:
            self.gibberish += 1        
            return "** Please consider using your head.. **"
        elif x >= 95:
            self.gibberish += 1        
            return "** If you don't start making sense, I will be forced to have you institutionalised! **"

    def win_lose(self):
        if self.win == True:
            art.tprint("CONGRATULATIONS","tarty1-large")
            art.tprint(f"{self.name}","tarty1-large")
            print(f"You made it {self.name}! You made it through unscathed!\n")
        else:
            art.tprint("BAD LUCK","smpoison-large")
            art.tprint(f"{self.name}","smpoison-large")
            if self.ending == "LOCKED DOOR":
                print("              _______________")
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
                print("\n[red]You have died miserably staring at the locked door. Better luck next time.[/red]\n")
            elif self.ending == "CANNIBALS":
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
                print("\n[red]You have died a delicious death! Better luck next time.[/red]\n")
            elif self.ending == "CERBERUS":
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
                print("\n[red]You now lack the required body parts to keep living! Better luck next time.[/red]\n")

    def credits_win(self):
        print("\n")
        print("*************************************************************************************************************************")
        print("          _______________ ")
        print("         |@@@@|     |####| ")
        print("         |@@@@|     |####|                                  ")
        print(f"         |@@@@|     |####|      It took you {self.turn_tracker} guesses to get through the first room")
        print("         \@@@@|     |####/                                       ")
        print("          \@@@|     |###/       ITEMS FOUND                                 ")
        print(f"           `@@|_____|##'        {' - '.join(self.bag)} ")
        print("                (O)                                              ")
        print("             .-'''''-.          WAS IT LUCK?                                ")
        print(f"           .'  * * *  `.        - {self.lucky}                                 ")
        print("          :  *       *  :                                        ")
        print("         : ~    YOU    ~ :      ENDING                                 ")
        print(f"         : ~    WON    ~ :      - {self.ending}")
        print("          :  *       *  : ")
        print(f"           `.  * * *  .'         You made {self.gibberish} unintelligible remarks along your journey")
        print("             `-.....-' ")
        print("\n")
        print("*************************************************************************************************************************")
        print("\n")
        print("\n")

    def credits_lose(self):
        print("\n")
        print("*************************************************************************************************************************")
        print("        _                   _ ")
        print("      _( )                 ( )_ ")
        print("     (_, |      __ __      | ,_) ")
        print(f"         \'\    /  ^  \    /'/        It took you {self.turn_tracker} guesses to get through the first room")   
        print("          '\'\,/\      \,/'/' ")
        print("           '\| []   [] |/'           ITEMS FOUND")
        print(f"             (_  /^\  _)             {' - '.join(self.bag)} ")
        print("               \  ~  / ")
        print("               /HHHHH\               ENDING")
        print(f"             /'/(^^^)\'\              - {self.ending}")
        print("         _,/'/'  ^^^  '\'\,_ ")
        print(f"        (_, |           | ,_)        You made {self.gibberish} unintelligible remarks along your journey")
        print("          (_)           (_) ")
        print("\n")
        print("*************************************************************************************************************************")
        print("\n")
        print("\n")


class TextPause:
    def enter_continue():
        print("\n\n[bold red]{PRESS ENTER TO CONTINUE}[/bold red]\n\n")
        input()