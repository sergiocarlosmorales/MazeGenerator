from maze_printer_abstract_base import MazePrinterAbstractBase
from maze_abstract_base import MazeAbstractBase


class MazePrinterText(MazePrinterAbstractBase):
    wall_character = "*"
    empty_character = " "
    new_line = "\n"
    maze = MazeAbstractBase

    def __init__(self, maze):
        self.maze = maze
        pass

    def print_maze(self):
        """Do the main work of printing a maze
        """
        for vertical_index in range(self.maze.get_height()):
            tiles = self.maze.get_tiles_in_row(vertical_index)
            tiles_print_data = self._get_row_print_data(tiles, vertical_index)
            print(tiles_print_data)

    def _get_row_print_data(self, tiles, vertical_index):
        row_print_data = ""

        # level 1 (only appears on first (0) row)
        if vertical_index == 0:
            for horizontal_index, tile in enumerate(tiles):
                # west wall only appears on first (0) column
                if horizontal_index == 0:
                    should_display_west_wall = True
                else:
                    should_display_west_wall = False

                if tile.is_wall_up("North") and should_display_west_wall and \
                        tile.is_wall_up("West"):
                            row_print_data += self.wall_character
                else:
                    if should_display_west_wall:
                        row_print_data += self.empty_character

                if tile.is_wall_up("North"):
                    row_print_data += self.wall_character
                else:
                    row_print_data += self.empty_character

                if tile.is_wall_up("East"):
                    row_print_data += self.wall_character
                else:
                    row_print_data += self.empty_character

            row_print_data += self.new_line

        # level 2
        for horizontal_index, tile in enumerate(tiles):
            if horizontal_index == 0:
                should_display_west_wall = True
            else:
                should_display_west_wall = False

            if should_display_west_wall:
                if tile.is_wall_up("West"):
                    row_print_data += self.wall_character
                else:
                    row_print_data += self.empty_character

            row_print_data += self.empty_character

            if tile.is_wall_up("East"):
                row_print_data += self.wall_character
            else:
                row_print_data += self.empty_character

        row_print_data += self.new_line

        # level 3
        for horizontal_index, tile in enumerate(tiles):
            if horizontal_index == 0:
                should_display_west_wall = True
            else:
                should_display_west_wall = False

            if should_display_west_wall:
                if tile.is_wall_up("West") and tile.is_wall_up("South"):
                    row_print_data += self.wall_character
                else:
                    row_print_data += self.empty_character

            if tile.is_wall_up("South"):
                row_print_data += self.wall_character
            else:
                row_print_data += self.empty_character

            if tile.is_wall_up("East"):
                row_print_data += self.wall_character
            else:
                row_print_data += self.empty_character

        return row_print_data
