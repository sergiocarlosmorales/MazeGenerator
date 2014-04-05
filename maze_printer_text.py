from maze_printer_abstract_base import MazePrinterAbstractBase
from maze_abstract_base import MazeAbstractBase


class ChillMazePrinterText(MazePrinterAbstractBase):
    debug_mode = True
    maze = MazeAbstractBase
    _top_wall_up_character = "."
    _top_wall_down_character = " "

    def print_maze(self):
        for vertical_index in self.maze.get_height():
            tiles = self.maze.get_tiles_in_row(vertical_index)
            print(self.get_row_print_data(tiles))
            pass

    def get_row_print_data(self, tiles):
        """Return the raw data representing the top of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                str
        """
        if len(tiles) < 1:
            return ""
        print_data = ""
        for tile in tiles:
            tile_data = self.get_top_tile_print_data(tile)
            print_data += tile_data

        return print_data

    def get_top_tile_print_data(self, tile):
        """Return the raw data representing the top of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                str
        """
        data = ""
        if self.debug_mode:
            pass
        return data