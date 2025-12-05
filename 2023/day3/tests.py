from unittest import TestCase, main
from . import today, parse_line, Number, unseen_numbers_around, today_1, adjacent_numbers

test_data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

class TodayTest(TestCase):
    def test_parse_line(self):
        l = parse_line("467..114..")
        self.assertEqual(l[0], Number(n=467))
        self.assertEqual(l[1], Number(n=467))
        self.assertEqual(l[2], Number(n=467))
        self.assertEqual(l[3], False)
        self.assertEqual(l[4], False)
        self.assertEqual(l[5], Number(n=114))
        self.assertEqual(l[6], Number(n=114))
        self.assertEqual(l[7], Number(n=114))
        self.assertEqual(l[8], False)
        self.assertEqual(l[9], False)

        l = parse_line(".467...114")
        self.assertEqual(l[1], Number(n=467))
        self.assertEqual(l[2], Number(n=467))
        self.assertEqual(l[3], Number(n=467))
        self.assertEqual(l[7], Number(n=114))
        self.assertEqual(l[8], Number(n=114))
        self.assertEqual(l[9], Number(n=114))

        l = parse_line("617*......")
        self.assertEqual(l[0], Number(n=617))
        self.assertEqual(l[1], Number(n=617))
        self.assertEqual(l[2], Number(n=617))
        self.assertTrue(l[3])
        self.assertFalse(l[4])

        l = parse_line("617*......", mode_bis=True)
        self.assertTrue(l[3])
        self.assertFalse(l[4])

        l = parse_line("617#......", mode_bis=True)
        self.assertFalse(l[3])
        self.assertFalse(l[4])

    def _gen_map(self):
        number_1 = Number(n=1)
        number_10 = Number(n=10)
        return [
            [number_10, number_10, False, False], # 0
            [False,     False,    True,   False], # 1
            [False,     False,  number_1, True],  # 2
        ]

    def test_unseen_numbers_around(self):
        self.assertEqual(unseen_numbers_around(self._gen_map(), 1, 1), 11)
        self.assertEqual(unseen_numbers_around(self._gen_map(), 1, 2), 11)
        self.assertEqual(unseen_numbers_around(self._gen_map(), 1, 0), 10)
        self.assertEqual(unseen_numbers_around(self._gen_map(), 0, 2), 10)
        self.assertEqual(unseen_numbers_around(self._gen_map(), 0, 3), 0)
        self.assertEqual(unseen_numbers_around(self._gen_map(), 2, 3), 1)

    def _gen_map_2(self):
        number_2 = Number(n=2)
        number_2_bis = Number(n=2)
        return [
            [False,       False, False, False], # 0
            [False,      True,    False,   False], # 1
            [number_2_bis, False,  number_2, True],  # 2
        ]

    def test_adjactent_numbers(self):
        self.assertListEqual(adjacent_numbers(self._gen_map_2(), 1, 1), [2, 2])


    def test_data(self):
        self.assertEqual(today_1(test_data), 4361)
        self.assertEqual(today(test_data), 467835)

if __name__ == '__main__':
    main()
