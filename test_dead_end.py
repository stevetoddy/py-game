import crawler
player = crawler.Character(name="test_player")

class TestDeadEnd:
    def test_valid(self):
        assert player.dead_end() == "** [blue]This door won't open[/blue] **" or "** [blue]This door is locked, you give it a knock... No answer.[/blue] **" or "** [blue]This door is locked tight[/blue] **" or "** [blue]This door won't budge[/blue] **" or "** [blue]AGH! This door is just painted on! Beautiful brushwork though.[/blue] **" or "** [blue]This door won't budge.. but wait, there's a clue tacked to the door:[/blue] \"The Item Merchant is very generous if you're polite! Thank you for listening\" **"


