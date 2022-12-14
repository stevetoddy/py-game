import crawler

# pylint: disable=line-too-long

player = crawler.Character(name="test_player")

# List of responses for the dead end responses test
options_dead_end = [
    "[blue]** This door won't open **[/blue]",
    "[blue]** This door is locked, you give it a knock... No answer. **[/blue]",
    "[blue]** This door is locked tight **[/blue]", "[blue]** This door won't budge **[/blue]",
    "[blue]** AGH! This door is just painted on! Beautiful brushwork though. **[/blue]",
    "[blue]** This door won't budge.. but wait, there's a clue tacked to the door: **[/blue] \"The Item Merchant is very generous if you're polite! Thank you for listening\""
    ]

# List of responses for the make sense responses test
options_make_sense = [
    "[yellow]** That doesn't make sense.. **[/yellow]",
    "[yellow]** Please stop with the gibberish! **[/yellow]",
    "[yellow]** You must think before you speak **[/yellow]",
    "[yellow]** It seems like you know what you're doing, but this doesn't make sense.. **[/yellow]",
    "[yellow]** Please consider using your head.. **[/yellow]",
    "[yellow]** If you don't start making sense, I will be forced to have you institutionalised! **[/yellow]"
    ]



class TestResponses:
    ''''
    CLASS FOR RESPONSE GENERATORS TESTS
    '''
    # Test to show dead_end() method works as intended. List 'options_dead_end' is populated
    # with all possible results from dead_end() and when method is called, the result is checked
    # against this list
    def test_dead_end(self):
        ''''
        TEST FOR DEAD END RESPONSE
        '''
        assert player.dead_end() in options_dead_end

    # Test to show make_sense() method works as intended. List 'options_make_sense' is populated
    # with all possible results from make_sense() and when method is called, the result is checked
    # against this list
    def test_make_sense(self):
        ''''
        TEST FOR NONSENSE RESPONSE
        '''
        assert player.make_sense() in options_make_sense



# Test to show add_item() method works as intended. Passing a test item
# to add_item and checking if the item was added to the list bag in the player instance.
class TestBagAdd:
    ''''
    CLASS FOR ADD TEST
    '''
    def test_add_item(self):
        '''
        ADD ITEM TEST
        '''
        player.add_item("TEST_ITEM")
        assert "TEST_ITEM" in player.bag
