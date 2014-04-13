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
from maze_generator_abstract_base import MazeGeneratorAbstractBase
from maze_abstract_base import MazeAbstractBase
from random import randrange, choice


class ChillMazeGenerator(MazeGeneratorAbstractBase):
    maze = MazeAbstractBase

    def __init__(self, maze):
        self.maze = maze

    def generate_perfect_maze(self):
        tile_stack = []
        total_tiles = self.maze.get_width() * self.maze.get_height()
        current_tile = self.maze.get_tile_at(randrange(self.maze.get_width()),
                                             randrange(self.maze.get_height()))
        visited_tiles = 1

        while visited_tiles < total_tiles:
            neighbors_with_all_walls_up = self._find_neighbors_with_walls_up(
                current_tile)
            if len(neighbors_with_all_walls_up) > 0:
                neighbor = choice(neighbors_with_all_walls_up)
                self.maze.connect_tiles(current_tile, neighbor)
                tile_stack.append(neighbor)
                visited_tiles += 1
            else:
                current_tile = tile_stack.pop()

    def _find_neighbors_with_walls_up(self, tile):
        """Return all tiles that are neighbors of the provided tiles and
            have all their wiles up
            Params:
                tile: TileAbstractBase
            Return:
                list of TileAbstractBase
        """
        neighbors_with_all_walls_up = []
        neighbors = self.maze.get_tile_neighbors(tile)

        for neighbor in neighbors:
            if neighbor.are_all_walls_up():
                neighbors_with_all_walls_up.append(neighbor)

        return neighbors_with_all_walls_up