# The MIT License (MIT)
#
# Copyright (c) 2014 Sergio Carlos Morales Angeles
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import unittest
from maze_abstract_base import MazeAbstractBase


class MazeTests(unittest.TestCase):
    maze_class = MazeAbstractBase

    def test_error_for_non_numeric_initialization(self):
        with self.assertRaises(ValueError):
            self.maze_class("pizza", "is awesome")

    def test_error_for_negative_values_initialization(self):
        with self.assertRaises(ValueError):
            self.maze_class(-1, -3)
        with self.assertRaises(ValueError):
            self.maze_class(1, -3)
        with self.assertRaises(ValueError):
            self.maze_class(-1, 5)

    def test_error_for_zero_dimension_maze(self):
        with self.assertRaises(ValueError):
            self.maze_class(0, 0)
        with self.assertRaises(ValueError):
            self.maze_class(3, 0)
        with self.assertRaises(ValueError):
            self.maze_class(0, 3)

    def test_maze_initializes_generated(self):
        maze = self.maze_class(3, 4)
        self.assertTrue(maze.has_been_generated())

    def test_maze_returns_correct_dimensions(self):
        intended_width = 3
        intended_height = 5
        maze = self.maze_class(intended_width, intended_height)
        self.assertTrue(maze.get_width() == intended_width)
        self.assertTrue(maze.get_height() == intended_height)

        intended_width = 4
        intended_height = 2
        maze = self.maze_class(intended_width, intended_height)
        self.assertTrue(maze.get_width() == intended_width)
        self.assertTrue(maze.get_height() == intended_height)

    def test_getting_row_size_equals_width(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)
        self.assertEqual(intended_width, len(maze.get_tiles_in_row(0)))

    def test_getting_column_size_equals_height(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)
        self.assertEqual(intended_height, len(maze.get_tiles_in_column(0)))

    def test_error_on_invalid_indexes(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)

        with self.assertRaises(IndexError):
            # They are 0 indexed, so this value is one over the actual height
            maze.get_tiles_in_row(intended_height)

        with self.assertRaises(IndexError):
            maze.get_tiles_in_column(intended_width)

    def test_error_on_invalid_tile_index(self):
        intended_height = 3
        intended_width = 5

        with self.assertRaises(IndexError):
            maze = self.maze_class(intended_width, intended_height)
            maze.get_tile_at(intended_width, intended_height)

    def test_tile_retrieval_with_valid_indexes(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)
        maze.get_tile_at(intended_width-1, intended_height-1)

    def test_tile_mapping(self):
        maze = self.maze_class(5, 5)

        for horizontal_index in range(maze.get_width()):
            for vertical_index in range(maze.get_height()):
                reference_tile = maze.get_tile_at(horizontal_index,
                                                  vertical_index)
                #lets get the tile via row
                row = maze.get_tiles_in_row(vertical_index)
                self.assertEqual(reference_tile, row[horizontal_index])

                #lets get the tile via column
                column = maze.get_tiles_in_column(horizontal_index)
                self.assertEqual(reference_tile, column[vertical_index])

    def test_neighborhood_mapping(self):
        maze = self.maze_class(3, 3)

        # Lets use the center tile as reference
        center_tile = maze.get_tile_at(1, 1)

        self.assertEqual(maze.get_tile_north_neighbor(center_tile),
                         maze.get_tile_at(1, 0))
        self.assertEqual(maze.get_tile_east_neighbor(center_tile),
                         maze.get_tile_at(2, 1))
        self.assertEqual(maze.get_tile_south_neighbor(center_tile),
                         maze.get_tile_at(1, 2))
        self.assertEqual(maze.get_tile_west_neighbor(center_tile),
                         maze.get_tile_at(0, 1))

    def test_maze_corner_tiles_neighbors(self):
        maze = self.maze_class(3, 3)
        top_left_tile = maze.get_tile_at(0, 0)
        top_right_tile = maze.get_tile_at(2, 0)
        bottom_right_tile = maze.get_tile_at(2, 2)

        # Top left tile
        self.assertEqual(maze.get_tile_north_neighbor(top_left_tile),
                         None)
        self.assertEqual(maze.get_tile_west_neighbor(top_left_tile),
                         None)

        # Top right tile
        self.assertEqual(maze.get_tile_north_neighbor(top_right_tile),
                         None)
        self.assertEqual(maze.get_tile_east_neighbor(top_right_tile),
                         None)

        # Bottom right tile
        self.assertEqual(maze.get_tile_east_neighbor(bottom_right_tile),
                         None)
        self.assertEqual(maze.get_tile_south_neighbor(bottom_right_tile),
                         None)

    def test_tiles_connection(self):
        maze = self.maze_class(3, 3)
        center_tile = maze.get_tile_at(1, 1)

        # Connect center tile with its north neighbor
        self.assertFalse(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_north_neighbor(center_tile)
            )
        )
        maze.connect_tiles(center_tile,
                           maze.get_tile_north_neighbor(center_tile))
        self.assertTrue(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_north_neighbor(center_tile)
            )
        )

        # Connect center tile with its east neighbor
        self.assertFalse(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_east_neighbor(center_tile)
            )
        )
        maze.connect_tiles(center_tile,
                           maze.get_tile_east_neighbor(center_tile))
        self.assertTrue(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_east_neighbor(center_tile)
            )
        )

        # Connect center tile with its south neighbor
        self.assertFalse(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_south_neighbor(center_tile)
            )
        )
        maze.connect_tiles(center_tile,
                           maze.get_tile_south_neighbor(center_tile))
        self.assertTrue(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_south_neighbor(center_tile)
            )
        )

        # Connect center tile with its west neighbor
        self.assertFalse(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_west_neighbor(center_tile)
            )
        )
        maze.connect_tiles(center_tile,
                           maze.get_tile_west_neighbor(center_tile))
        self.assertTrue(
            maze.are_tiles_connected(
                center_tile,
                maze.get_tile_west_neighbor(center_tile)
            )
        )

    def test_separate_tiles_cant_be_connected(self):
        maze = self.maze_class(3, 3)
        upper_left_tile = maze.get_tile_at(0, 0)
        lower_right_tile = maze.get_tile_at(2, 2)

        # Test with varying tile order just to be sure it does not
        # affect our result
        with self.assertRaises(ValueError):
            maze.connect_tiles(upper_left_tile,
                               lower_right_tile)
        with self.assertRaises(ValueError):
            maze.connect_tiles(lower_right_tile,
                               upper_left_tile)

        self.assertFalse(maze.are_tiles_connected(upper_left_tile,
                                                  lower_right_tile))
        self.assertFalse(maze.are_tiles_connected(lower_right_tile,
                                                  upper_left_tile))

    def test_get_neighbors_for_center_tile(self):
        maze = self.maze_class(3, 3)
        center_tile = maze.get_tile_at(1, 1)
        center_tile_neighbors = maze.get_tile_neighbors(center_tile)
        # north, east, south, west
        self.assertEqual(4, len(center_tile_neighbors))
        # north
        self.assertTrue(maze.get_tile_at(1, 0) in center_tile_neighbors)
        # east
        self.assertTrue(maze.get_tile_at(2, 1) in center_tile_neighbors)
        # south
        self.assertTrue(maze.get_tile_at(1, 2) in center_tile_neighbors)
        # west
        self.assertTrue(maze.get_tile_at(0, 1) in center_tile_neighbors)

    def test_get_neighbors_for_corner_tile(self):
        maze = self.maze_class(3, 3)
        corner_tile = maze.get_tile_at(0, 0)
        corner_tile_neighbors = maze.get_tile_neighbors(corner_tile)
        # east and south
        self.assertEqual(2, len(corner_tile_neighbors))
        # east
        self.assertTrue(maze.get_tile_at(1, 0) in corner_tile_neighbors)
        # south
        self.assertTrue(maze.get_tile_at(0, 1) in corner_tile_neighbors)
