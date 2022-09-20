import crawler
player = crawler.Character(name="test_player")

# class TestDeadEnd:
#     def test_valid(self):
#         assert player.dead_end() == "** [blue]This door won't open[/blue] **"

options = ["** [blue]This door won't open[/blue] **", "** [blue]This door is locked, you give it a knock... No answer.[/blue] **", "** [blue]This door is locked tight[/blue] **", "** [blue]This door won't budge[/blue] **", "** [blue]AGH! This door is just painted on! Beautiful brushwork though.[/blue] **", "** [blue]This door won't budge.. but wait, there's a cluetacked to the door:[/blue] \"The Item Merchant is very generous if you're polite! Thank you for listening\" **"]

class TestDeadEnd:
    def test_valid(self):
        assert player.dead_end() in options