import unittest

from rolling_dice.die import Die


class DieTestCase(unittest.TestCase):
    def test_num_side(self):
        die = Die(10)
        self.assertEqual(10, die.num_sides)


if __name__ == "__main__":
    unittest.main()
