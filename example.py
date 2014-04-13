from chill_maze import ChillMaze
from maze_printer_text import MazePrinterText


def main():
    maze = ChillMaze(3, 3)
    tile1 = maze.get_tile_at(0, 0)
    tile2 = maze.get_tile_at(1, 0)
    maze.connect_tiles(tile1, tile2)
    printer = MazePrinterText(maze)
    printer.print_maze()

if __name__ == "__main__":
    main()