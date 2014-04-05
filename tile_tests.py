import unittest
from tile_abstract_base import TileAbstractBase


class TileTests(unittest.TestCase):
    tile_class = TileAbstractBase

    def test_all_walls_are_up_after_creation(self):
        tile = self.tile_class()
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_a_wall_causes_all_walls_check_to_be_false(self):
        tile = self.tile_class()
        tile.knock_wall("Bottom")
        self.assertFalse(tile.are_all_walls_up())

    def test_raising_a_wall_after_knocked_makes_all_walls_check_true(self):
        tile = self.tile_class()
        tile.knock_wall("Top")
        tile.raise_wall("Top")
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_non_existent_wall_raises_value_error(self):
        tile = self.tile_class()
        with self.assertRaises(ValueError):
            tile.knock_wall("Tacos")