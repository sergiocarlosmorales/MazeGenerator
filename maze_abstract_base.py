import abc
from tile_abstract_base import TileAbstractBase


class MazeAbstractBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __init__(self, width, height, tile_class=TileAbstractBase):
        """Initialization logic for the maze
            Params:
                width: numeric value for the grid width of the maze
                height: numeric value for the gird height of the maze
                tile_class: class to be used for tiles, one must be provided
                            by default
            Raises:
                ValueError: If width or height cannot be numerically
                            interpreted and are not greater than zero
        """
        return

    @abc.abstractmethod
    def has_been_generated(self):
        """Determine whether or not this maze has been generated and has tiles
            Returns: bool
        """
        return

    @abc.abstractmethod
    def get_width(self):
        """Get the width of this maze
            Return: Numeric value of the width
        """
        return

    @abc.abstractmethod
    def get_height(self):
        """Get the height of this maze
            Return: Numeric value of the height
        """
        return

    @abc.abstractmethod
    def get_tiles_in_row(self, index):
        """Return all tiles on a specific row (horizontal dimension)
            Params:
                index: integer
            Returns:
                List of tiles
            Raises:
                IndexError: If supplied index is invalid
        """
        return

    @abc.abstractmethod
    def get_tiles_in_column(self, index):
        """Return all tiles from a specific column (vertical dimension)
            Params:
                index integer
            Returns:
                List of tiles
            Raises:
                IndexError: If supplied index is invalid
        """
        return

    @abc.abstractmethod
    def get_tile_at(self, horizontal_index, vertical_index):
        """Return the tile at a specific location
            Params:
                horizontal_index numeric index for the horizontal axis
                vertical_index numeric index for the vertical axis
            Returns:
                A tile TileAbstractBase
            Raises:
                Index error if any of the provided indexes is not valid
        """
        return

    @abc.abstractmethod
    def get_tile_north_neighbor(self, tile):
        """Return the north neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase|None
        """
        return

    @abc.abstractmethod
    def get_tile_east_neighbor(self, tile):
        """Return the east neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase|None
        """
        return

    @abc.abstractmethod
    def get_tile_south_neighbor(self, tile):
        """Return the south neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase|None
        """
        return

    @abc.abstractmethod
    def get_tile_west_neighbor(self, tile):
        """Return the west neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase|None
        """
        return

    @abc.abstractmethod
    def connect_tiles(self, tile_1, tile_2):
        """Connect two neighbor tiles (knocks appropriate walls)
            Params:
                tile_1: TileAbstractBase
                tile_2: TileAbstractBase
            Raises:
                ValueError if tiles are not neighbors
        """
        return

    @abc.abstractmethod
    def are_tiles_connected(self, tile_1, tile_2):
        """Determine whether two tiles are connected
            Params:
                tile_1: TileAbstractBase
                tile_2: TileAbstractBase
            Returns:
                Bool
        """
        return