from crawler import Character.dead_end

class TestDeadEnd:
    def test_valid(self):
        assert dead_end() in range(1-21)
