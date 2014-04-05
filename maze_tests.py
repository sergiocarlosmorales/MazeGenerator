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
        self.assertEqual(intended_width, len(maze.get_row_tiles(0)))

    def test_getting_column_size_equals_height(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)
        self.assertEqual(intended_height, len(maze.get_column_tiles(0)))

    def test_error_on_invalid_indexes(self):
        intended_height = 3
        intended_width = 5

        maze = self.maze_class(intended_width, intended_height)

        with self.assertRaises(IndexError):
            # They are 0 indexed, so this value is one over the actual height
            maze.get_row_tiles(intended_height)

        with self.assertRaises(IndexError):
            maze.get_column_tiles(intended_width)

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

    @unittest.skip("Pending print method for easier debugging")
    def test_tile_mapping(self):
        # Generate a Maze
        intended_height = 3
        intended_width = 5
        maze = self.maze_class(intended_width, intended_height)

        # Iterate through each horizontal dimension (rows)
        for horizontal_index in range(maze.get_width()):
            for vertical_index in range(maze.get_height()):
                reference_id = id(maze.get_tile_at(horizontal_index,
                                                   vertical_index))
                #lets get the object via row
                row = maze.get_row_tiles(vertical_index)
                tile = row[horizontal_index]
                self.assertEqual(reference_id,
                                 id(tile))