import unittest
from tile_tests import TileTests
from maze_tests import MazeTests
from chill_tile import ChillTile
from chill_maze import ChillMaze


def run_tests_wrapper(test_case):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner(verbosity=1).run(suite)


def run_tile_tests():
    tile_classes = [ChillTile]
    for tile_class in tile_classes:
        TileTests.tile_class = tile_class
        run_tests_wrapper(TileTests)


def run_maze_tests():
    maze_classes = [ChillMaze]
    for maze_class in maze_classes:
        MazeTests.maze_class = maze_class
        run_tests_wrapper(MazeTests)


if __name__ == '__main__':
    run_tile_tests()
    run_maze_tests()