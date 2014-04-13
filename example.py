from chill_maze import ChillMaze
from maze_printer_text import MazePrinterText
from chill_maze_generator import ChillMazeGenerator


def main():
    maze = ChillMaze(9, 9)
    generator = ChillMazeGenerator(maze)
    generator.generate_perfect_maze()

    printer = MazePrinterText(generator.maze)
    printer.print_maze()

if __name__ == "__main__":
    main()