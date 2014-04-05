import abc


class MazePrinterAbstractBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def print_maze(self, maze):
        """Print the maze, d'oh!
            Params:
                maze object that must conform to MazeAbstractBase
        """
        return