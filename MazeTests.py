import unittest
from Maze import ChillMazeTile


class TileTests(unittest.TestCase):
    def test_tile_instantiates(self):
        tile = ChillMazeTile()

    def test_all_walls_are_up_after_creation(self):
        tile = ChillMazeTile()
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_a_wall_causes_all_walls_check_to_be_false(self):
        tile = ChillMazeTile()
        tile.knock_wall("Bottom")
        self.assertFalse(tile.are_all_walls_up())

    def test_raising_a_wall_after_knocked_makes_all_walls_check_true(self):
        tile = ChillMazeTile()
        tile.knock_wall("Top")
        tile.raise_wall("Top")
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_non_existent_wall_raises_value_error(self):
        tile = ChillMazeTile()
        with self.assertRaises(ValueError):
            tile.knock_wall("Inexistent")

def main():
    unittest.main()

if __name__ == '__main__':
    main()
