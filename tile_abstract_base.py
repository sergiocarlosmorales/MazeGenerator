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


class TileAbstractBase:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def are_all_walls_up(self):
        """Determine whether or not: all walls are up
            Params:
                none
            Returns:
                bool
        """
        return

    @abc.abstractmethod
    def knock_wall(self, location):
        """Knock the wall on a given location
            Params:
                location: str containing the location of the wall to knock
            Raises:
                ValueError if location param is not a valid location for a wall
        """
        return

    @abc.abstractmethod
    def raise_wall(self, location):
        """Raise the wall on a given location
            Params:
                location: str containing the location of the wall to raise
            Raises:
                ValueError if location param is not a valid location for a wall
        """
        return

    @abc.abstractmethod
    def is_wall_up(self, location):
        """Determine if a wall is up or not at a given location
            Params:
                location: str containing the location of the wall to raise
            Returns:
                bool
            Raises:
                ValueError if location param is not a valid location for a wall
        """
        return