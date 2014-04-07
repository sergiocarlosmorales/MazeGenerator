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