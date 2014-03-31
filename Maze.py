class ChillMazeTile:
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
        if location.capitalize() == "Top":
            self._wall_top = new_value
        elif location.capitalize() == "Bottom":
            self._wall_bottom = new_value
        elif location.capitalize() == "Left":
            self._wall_left = new_value
        elif location.capitalize() == "Top":
            self._wall_top = new_value
        else:
            raise ValueError("Invalid wall location provided:{}"
                             .format(location))

    def knock_wall(self, location):
        return self._set_wall(location, False)

    def raise_wall(self, location):
        return self._set_wall(location, True)


class ChillMaze:
    _width = 0
    _height = 0
    _generated = False

    def __init__(self, width, height):
        if width < 1 or height < 1:
            raise ValueError("Width and Height must be greater than zero:"
                             "{},{} provided".format(width, height))

        self._width = width
        self._height = height
        self._generated = False

    def generate(self):
        pass
