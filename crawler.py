import random
from rich import print
import time
import clearing
import art


class Character:
    """PLAYER CLASS"""
    def __init__(self, name):
        self.name = name
        self.turn_tracker = 0
        self.gibberish = 0
        self.bag = []
        self.win = False
        self.ending = " "
        self.gold_star = False

    def add_item(self, item):
        """ADD ITEMS TO PLAYER BAG"""
        self.item = self.bag.append(item)

    def dead_end(self):
        """PICKING WRONG DOOR STATEMENT"""
        pick_door = random.randint(1,101)
        if pick_door <= 20:
            self.turn_tracker += 1
            return "[blue]** This door won't open **[/blue]"
        if 20 < pick_door <= 40:
            self.turn_tracker += 1
            return "[blue]** This door is locked, you give it a knock... No answer. **[/blue]"
        if 40 < pick_door <= 60:
            self.turn_tracker += 1
            return "[blue]** This door is locked tight **[/blue]"
        if 60 < pick_door <= 80:
            self.turn_tracker += 1
            return "[blue]** This door won't budge **[/blue]"
        if 80 < pick_door < 95:
            self.turn_tracker += 1
            return "[blue]** AGH! This door is just painted on! Beautiful brushwork though. **[/blue]"
        if pick_door >= 95:
            self.turn_tracker += 1
            return "[blue]** This door won't budge.. but wait, there's a clue tacked to the door: **[/blue] \"The Item Merchant is very generous if you're polite! Thank you for listening\""

    def make_sense(self):
        """USER ENTERING A WRONG VALUE OR TYPE STATEMENT"""
        wrong_statement = random.randint(1,101)

        if wrong_statement <= 60:
            self.gibberish += 1
            return "[yellow]** That doesn't make sense.. **[/yellow]"
        if 60 < wrong_statement <= 70:
            self.gibberish += 1
            return "[yellow]** Please stop with the gibberish! **[/yellow]"
        if 70 < wrong_statement <= 80:
            self.gibberish += 1
            return "[yellow]** You must think before you speak **[/yellow]"
        if 80 < wrong_statement <= 90:
            self.gibberish += 1
            return "[yellow]** It seems like you know what you're doing, but this doesn't make sense.. **[/yellow]"
        if 90 < wrong_statement < 95:
            self.gibberish += 1        
            return "[yellow]** Please consider using your head.. **[/yellow]"
        if wrong_statement >= 95:
            self.gibberish += 1        
            return "[yellow]** If you don't start making sense, I will be forced to have you institutionalised! **[/yellow]"

    def win_lose(self):
        """WIN/LOSE STATEMENTS WITH PICTURES"""
        if self.win is True:
            art.tprint("\n\nCONGRATULATIONS","tarty1-large")
            art.tprint(f"{self.name}","tarty1-large")
            print("\n[bold yellow]You made it through unscathed![/bold yellow]\n")
        else:
            art.tprint(f"\n\nBAD LUCK {self.name}","smpoison-large")
            if self.ending == "LOCKED DOOR":
                print("\n[red]You have died miserably staring at the locked door. Better luck next time.[/red]\n")
            elif self.ending == "CANNIBALS":
                print("\n[red]You have died a delicious death! Better luck next time.[/red]\n")
            elif self.ending == "CERBERUS":
                print("\n[red]You now lack the required body parts to keep living! Better luck next time.[/red]\n")

    def credits_win(self):
        """WIN STATE"""
        print("\n\n")
        print("*************************************************************************************************************************")
        print("          _______________ ")
        print("         |@@@@|     |####| ")
        print("         |@@@@|     |####|                                  ")
        print(f"         |@@@@|     |####|      It took you {self.turn_tracker} guesses to get through the first room")
        print("         \@@@@|     |####/                                       ")
        print("          \@@@|     |###/       ITEMS COLLECTED                                 ")
        print(f"           `@@|_____|##'        {' - '.join(self.bag)} ")
        print("                (O)                                              ")
        print("             .-'''''-.          GOLD STAR FOUND?                                ")
        print(f"           .'  * * *  `.        - {self.gold_star}   ")
        print("          :  *       *  :                                        ")
        print("         : ~    YOU    ~ :      ENDING                                 ")
        print(f"         : ~    WON    ~ :      - {self.ending}")
        print("          :  *       *  : ")
        print(f"           `.  * * *  .'        You made {self.gibberish} unintelligible remarks along your journey")
        print("             `-.....-' ")
        print("\n")
        print("*************************************************************************************************************************")
        print("\n")
        print("\n")

    def credits_lose(self):
        """LOSE STATE"""
        print("\n\n")
        print("*************************************************************************************************************************")
        print("        _                   _ ")
        print(f"      _( )                 ( )_        It took you {self.turn_tracker} guesses to get through the first room")
        print("     (_, |      __ __      | ,_) ")
        print("         \'\    /  ^  \    /'/         ITEMS FOUND")
        print(f"          '\'\,/\      \,/'/'          {' - '.join(self.bag)}")
        print("           '\| []   [] |/'            ")
        print("             (_  /^\  _)               GOLD STAR FOUND?")
        print(f"               \  ~  /                 - {self.gold_star}")
        print("               /HHHHH\               ")
        print("             /'/(^^^)\'\               ENDING ")
        print(f"         _,/'/'  ^^^  '\'\,_           - {self.ending}")
        print("        (_, |           | ,_) ")
        print(f"          (_)           (_)            You made {self.gibberish} unintelligible remarks along your journey")
        print("\n")
        print("*************************************************************************************************************************")
        print("\n")
        print("\n")


class TextPause:
    """PRESS ENTER TO CONTINUE STORY BREAK"""
    @staticmethod
    def enter_continue():
        """PRESS ENTER TO CONTINUE STORY BREAK"""
        time.sleep(1.5)
        print("\n\n[bold red]{PRESS ENTER TO CONTINUE}[/bold red]\n\n")
        input()
        clearing.clear()
