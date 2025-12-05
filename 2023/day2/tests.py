from unittest import TestCase
from . import today, Picked, Game

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

class TodayTest(TestCase):
    def test_picked(self):
        p = Picked.from_entry(" 5 blue, 4 red, 13 green")
        self.assertEqual(p, Picked(blue=5, red=4, green=13))
        self.assertTrue(p.possible(5, 4, 13))
        self.assertFalse(p.possible(5, 3, 13))
        self.assertFalse(p.possible(5, 4, 12))
        self.assertFalse(p.possible(4, 4, 13))
        p = Picked.from_entry(" 10 blue")
        self.assertEqual(p, Picked(blue=10, red=0, green=0))
        p = Picked.from_entry(" 4 green, 20 blue")
        self.assertEqual(p, Picked(blue=20, red=0, green=4))

    def test_game(self):
        g = Game.from_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(g, Game(id=1, picks=[
            Picked(blue=3, red=4),
            Picked(red=1, green=2, blue=6),
            Picked(green=2),
        ]))
        self.assertTrue(g.possible(6, 4, 2))
        self.assertFalse(g.possible(5, 4, 2))
        self.assertFalse(g.possible(6, 3, 2))
        self.assertFalse(g.possible(6, 4, 1))

        g = Game.from_line("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(g, Game(id=4, picks=[
            Picked(green=1, red=3, blue=6),
            Picked(green=3, red=6),
            Picked(green=3, blue=15, red=14),
        ]))
    
    def test_power(self):
        g = Game.from_line("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green")
        self.assertEqual(g.power(), 48)
        g = Game.from_line("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue")
        self.assertEqual(g.power(), 12)
        g = Game.from_line("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red")
        self.assertEqual(g.power(), 1560)
        g = Game.from_line("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red")
        self.assertEqual(g.power(), 630)
        g = Game.from_line("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
        self.assertEqual(g.power(), 36)


    def test_data(self):
        self.assertEqual(today(test_data), 2286)
