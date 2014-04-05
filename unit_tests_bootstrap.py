import unittest
# Test classes
from tile_tests import TileTests
from maze_tests import MazeTests
# Implementation classes
from chill_tile import ChillTile
from chill_maze import ChillMaze


def run_tests_wrapper(testcase, verbosity_level=1):
    """This will execute a test case
        Params:
            testcase The actual test case, unittest.TestCase
            verbosity_level Optional numeric to tune the level of output
    """
    suite = unittest.TestLoader().loadTestsFromTestCase(testcase)
    unittest.TextTestRunner(verbosity=verbosity_level).run(suite)


def run_tile_tests():
    """Run tile tests for all tile classes
    """
    tile_classes = [ChillTile]
    for tile_class in tile_classes:
        TileTests.tile_class = tile_class
        run_tests_wrapper(TileTests)


def run_maze_tests():
    """Run maze tests for all maze classes
    """
    maze_classes = [ChillMaze]
    for maze_class in maze_classes:
        MazeTests.maze_class = maze_class
        run_tests_wrapper(MazeTests)


if __name__ == '__main__':
    run_tile_tests()
    run_maze_tests()