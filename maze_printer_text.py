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
                    row_print_data += self.wall_character

                if tile.is_wall_up("North"):
                    row_print_data += self.wall_character
                else:
                    row_print_data += self.empty_character

                row_print_data += self.wall_character

            row_print_data += self.new_line

        # level 2
        for horizontal_index, tile in enumerate(tiles):
            if horizontal_index == 0:
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
                row_print_data += self.wall_character

            if tile.is_wall_up("South"):
                row_print_data += self.wall_character
            else:
                row_print_data += self.empty_character

            row_print_data += self.wall_character

        return row_print_data
