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