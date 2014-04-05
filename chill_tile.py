from tile_abstract_base import TileAbstractBase


class ChillTile(TileAbstractBase):
    # Flags to indicate if a given wall is up
    _wall_top = None
    _wall_bottom = None
    _wall_right = None
    _wall_left = None

    def __init__(self):
        """
        Initializer of a tile
        """
        # Build all walls
        self._set_wall("Top", True)
        self._set_wall("Right", True)
        self._set_wall("Bottom", True)
        self._set_wall("Left", True)

    def are_all_walls_up(self):
        """Determine whether or not: all walls are up
            Params:
                none
            Returns:
                bool
        """
        return self._wall_bottom and self._wall_left and \
            self._wall_right and self._wall_top

    def _set_wall(self, location, new_value):
        """Set a wall to a specified value
            Params:
                location: str to determine which wall to modify
                new_value: value to be assigned to the wall
            Raises:
                ValueError if location param is not a valid location for a wall
        """
        if location.capitalize() == "Top":
            self._wall_top = new_value
        elif location.capitalize() == "Bottom":
            self._wall_bottom = new_value
        elif location.capitalize() == "Left":
            self._wall_left = new_value
        elif location.capitalize() == "Right":
            self._wall_right = new_value
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
        if location.capitalize() == "Top":
            return self._wall_top
        elif location.capitalize() == "Bottom":
            return self._wall_bottom
        elif location.capitalize() == "Left":
            return self._wall_left
        elif location.capitalize() == "Right":
            return self._wall_right
        else:
            raise ValueError("Invalid wall location provided: {}"
                             .format(location))