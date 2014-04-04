import unittest
from maze import ChillMazeTile, ChillMaze


class TileTests(unittest.TestCase):
    def test_tile_instantiates(self):
        ChillMazeTile()

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
            tile.knock_wall("Tacos")


class MazeTests(unittest.TestCase):
    def test_maze_instantiates(self):
        ChillMaze(3, 3)

    def test_error_for_non_numeric_initialization(self):
        with self.assertRaises(ValueError):
            ChillMaze("pizza", "is awesome")

    def test_error_for_negative_values_initialization(self):
        with self.assertRaises(ValueError):
            ChillMaze(-1, -3)
        with self.assertRaises(ValueError):
            ChillMaze(1, -3)
        with self.assertRaises(ValueError):
            ChillMaze(-1, 5)

    def test_error_for_zero_dimension_maze(self):
        with self.assertRaises(ValueError):
            ChillMaze(0, 0)
        with self.assertRaises(ValueError):
            ChillMaze(3, 0)
        with self.assertRaises(ValueError):
            ChillMaze(0, 3)

    def test_maze_initializes_generated(self):
        maze = ChillMaze(3, 4)
        self.assertTrue(maze.has_been_generated())

    def test_maze_returns_correct_dimensions(self):
        intended_width = 3
        intended_height = 5
        maze = ChillMaze(intended_width, intended_height)
        self.assertTrue(maze.get_width() == intended_width)
        self.assertTrue(maze.get_height() == intended_height)

        intended_width = 4
        intended_height = 2
        maze = ChillMaze(intended_width, intended_height)
        self.assertTrue(maze.get_width() == intended_width)
        self.assertTrue(maze.get_height() == intended_height)

    def test_getting_row_size_equals_width(self):
        intended_height = 3
        intended_width = 5

        maze = ChillMaze(intended_width, intended_height)
        self.assertEqual(intended_width, len(maze.get_row_tiles(0)))

    def test_getting_column_size_equals_height(self):
        intended_height = 3
        intended_width = 5

        maze = ChillMaze(intended_width, intended_height)
        self.assertEqual(intended_height, len(maze.get_column_tiles(0)))

    def test_error_on_invalid_indexes(self):
        intended_height = 3
        intended_width = 5

        maze = ChillMaze(intended_width, intended_height)

        with self.assertRaises(IndexError):
            # They are 0 indexed, so this value is one over the actual height
            maze.get_row_tiles(intended_height)

        with self.assertRaises(IndexError):
            maze.get_column_tiles(intended_width)

    def test_error_on_invalid_tile_index(self):
        intended_height = 3
        intended_width = 5

        with self.assertRaises(IndexError):
            maze = ChillMaze(intended_width, intended_height)
            maze.get_tile_at(intended_width, intended_height)

    def test_tile_retrieval_with_valid_indexes(self):
        intended_height = 3
        intended_width = 5

        maze = ChillMaze(intended_width, intended_height)
        maze.get_tile_at(intended_width-1, intended_height-1)

    @unittest.skip("Pending print method for easier debugging")
    def test_tile_mapping(self):
        # Generate a Maze
        intended_height = 3
        intended_width = 5
        maze = ChillMaze(intended_width, intended_height)

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


def main():
    unittest.main()

if __name__ == '__main__':
    main()
