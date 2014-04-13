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
import abc
from tile_abstract_base import TileAbstractBase


class MazeAbstractBase:
    __metaclass__ = abc.ABCMeta

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
    def get_tile_neighbors(self, tile):
        """Return all neighbors for a tile
            This will not always return 4 tiles, a tile may not have a neighbor
            and will not be included in the return list
            Params:
                tile: TileAbstractBase
            Returns:
                List of TileAbstractBase
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