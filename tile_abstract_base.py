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
        """
        return

    @abc.abstractmethod
    def raise_wall(self, location):
        """Rase the wall on a given location
            Params:
                location: str containing the location of the wall to raise
        """
        return

    @abc.abstractmethod
    def is_wall_up(self, location):
        """Determine if a wall is up or not at a given location
            Params:
                location: str containing the location of the wall to raise
            Returns:
                bool
        """
        return