from maze_abstract_base import MazeAbstractBase
import abc


class MazeGeneratorAbstractBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, maze):
        """Initializer
            Params:
                maze: MazeAbstractBase
        """
        return

    @abc.abstractmethod
    def generate_perfect_maze(self):
        """Main function to generate a perfect maze
            Returns: MazeAbstractBase
        """
        return