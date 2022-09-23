import time
import clearing
from rich import print  # THIS IMPORT WILL OVERRIDE THE BUILTIN PRINT FUNCTION

class TextPause:
    """
    PRESS ENTER TO CONTINUE STORY BREAK
    """
    @staticmethod
    def enter_continue():
        """
        PRESS ENTER TO CONTINUE STORY BREAK
        """
        time.sleep(1.5)
        print("\n\n[bold red]{PRESS ENTER TO CONTINUE}[/bold red]\n\n")
        input()
        clearing.clear()
