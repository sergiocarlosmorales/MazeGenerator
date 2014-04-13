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
        print("Running tile tests for: {}\n".format(tile_class.__name__))
        run_tests_wrapper(TileTests)


def run_maze_tests():
    """Run maze tests for all maze classes
    """
    maze_classes = [ChillMaze]
    for maze_class in maze_classes:
        MazeTests.maze_class = maze_class
        print("Running maze tests for: {}\n".format(maze_class.__name__))
        run_tests_wrapper(MazeTests)


if __name__ == '__main__':
    run_tile_tests()
    run_maze_tests()