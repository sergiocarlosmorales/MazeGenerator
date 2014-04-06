from tile_abstract_base import TileAbstractBase


class ChillTile(TileAbstractBase):
    # Flags to indicate if a given wall is up
    _wall_north = None
    _wall_south = None
    _wall_east = None
    _wall_west = None

    def __init__(self):
        """
        Initializer of a tile
        """
        # Build all walls
        self._set_wall("North", True)
        self._set_wall("East", True)
        self._set_wall("South", True)
        self._set_wall("West", True)

    def are_all_walls_up(self):
        """Determine whether or not: all walls are up
            Params:
                none
            Returns:
                bool
        """
        return self._wall_south and self._wall_west and \
            self._wall_east and self._wall_north

    def _set_wall(self, location, new_value):
        """Set a wall to a specified value
            Params:
                location: str to determine which wall to modify
                new_value: value to be assigned to the wall
            Raises:
                ValueError if location param is not a valid location for a wall
        """
        if location.capitalize() == "North":
            self._wall_north = new_value
        elif location.capitalize() == "South":
            self._wall_south = new_value
        elif location.capitalize() == "West":
            self._wall_west = new_value
        elif location.capitalize() == "East":
            self._wall_east = new_value
        else:
            raise ValueError("Invalid wall location provided: {}"
                             .format(location))

    def knock_wall(self, location):
        """Knock the wall on a given location
            Params:
                location: str containing the location of the wall to knock
        """
        return self._set_wall(location, False)

    def raise_wall(self, location):
        """Rase the wall on a given location
            Params:
                location: str containing the location of the wall to raise
        """
        return self._set_wall(location, True)

    def is_wall_up(self, location):
        if location.capitalize() == "North":
            return self._wall_north
        elif location.capitalize() == "South":
            return self._wall_south
        elif location.capitalize() == "West":
            return self._wall_west
        elif location.capitalize() == "East":
            return self._wall_east
        else:
            raise ValueError("Invalid wall location provided: {}"
                             .format(location))