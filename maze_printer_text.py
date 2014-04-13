from maze_printer_abstract_base import MazePrinterAbstractBase
from maze_abstract_base import MazeAbstractBase
from chill_maze import ChillMaze


class ChillMazePrinterText(MazePrinterAbstractBase):
    debug_mode = True
    wall_character = "*"
    empty_character = " "
    new_line = "\n"
    maze = MazeAbstractBase

    def print_maze(self):
        for vertical_index in range(self.maze.get_height()):
            tiles = self.maze.get_tiles_in_row(vertical_index)
            tiles_print_data = self.get_row_print_data(tiles, vertical_index)
            print(tiles_print_data)

    def get_row_print_data(self, tiles, vertical_index):
        row_print_data = ""

        # level 1
        for horizontal_index, tile in enumerate(tiles):

            if vertical_index == 0:
                should_display_north_wall = True
            else:
                should_display_north_wall = False

            if horizontal_index == 0:
                should_display_west_wall = True
            else:
                should_display_west_wall = False

            # level 1
            if should_display_north_wall:
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


def main():
    maze = ChillMaze(3, 3)
    printer = ChillMazePrinterText()
    printer.maze = maze
    printer.print_maze()

if __name__ == '__main__':
    main()
