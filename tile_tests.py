import unittest
from tile_abstract_base import TileAbstractBase


class TileTests(unittest.TestCase):
    tile_class = TileAbstractBase

    def test_all_walls_are_up_after_creation(self):
        tile = self.tile_class()
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_a_wall_causes_all_walls_check_to_be_false(self):
        tile = self.tile_class()
        tile.knock_wall("South")
        self.assertFalse(tile.are_all_walls_up())

    def test_raising_a_wall_after_knocked_makes_all_walls_check_true(self):
        tile = self.tile_class()
        tile.knock_wall("North")
        tile.raise_wall("North")
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_non_existent_wall_raises_value_error(self):
        tile = self.tile_class()
        with self.assertRaises(ValueError):
            tile.knock_wall("Tacos")

    def test_knocking_a_wall_actually_knocks_it(self):
        wall_position = "North"
        tile = self.tile_class()
        tile.knock_wall(wall_position)
        self.assertFalse(tile.is_wall_up(wall_position))

    def test_rebuilding_a_wall_actually_rebuilds_it(self):
        wall_position = "South"
        tile = self.tile_class()
        tile.knock_wall(wall_position)
        tile.raise_wall(wall_position)
        self.assertTrue(tile.is_wall_up(wall_position))

    def test_retrieving_non_existent_wall_status_raises_error(self):
        tile = self.tile_class()
        with self.assertRaises(ValueError):
            tile.is_wall_up("Waffles")