import abc


class MazePrinterAbstractBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def print_maze(self):
        """Print the maze, d'oh!
            Params:
                maze object that must conform to MazeAbstractBase
        """
        return