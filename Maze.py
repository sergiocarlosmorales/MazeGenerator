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
            raise ValueError("Invalid wall location provided:{}"
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


class ChillMaze:
    _width = None
    _height = None
    _maze = []

    def __init__(self, width, height):
        """Initialization logic for the maze
            Params:
                width: numeric value for the grid width of the maze
                height: numeric value for the gird height of the maze
            Raises:
                ValueError: If width or height cannot be numerically
                            interpreted and are not greater than zero
        """
        try:
            width = int(width)
            height = int(height)

            if width < 1 or height < 1:
                raise ValueError

        except (TypeError, ValueError):
            raise ValueError("Width and Height must be greater than zero:"
                             "{},{} provided".format(width, height))

        # Initialize data
        self._width = width
        self._height = height
        self._maze = []

        # Time to actually initialize the tiles
        # Lets go through each row
        for row_number in range(height):
            # Then create all columns
            column = []
            for column_number in range(width):
                tile = ChillMazeTile()
                column.append(tile)
            self._maze.append(column)

        # Sanity check
        if (len(self._maze) != self.get_height() or
                len(self._maze[0]) != self.get_width()):
                    raise AssertionError("Dimensions are not matching up!\n"
                                         "Actual Width: {actual_width}\n"
                                         "Actual Height: {actual_height}\n"
                                         "Intended Width: {intended_width}\n"
                                         "Intended Height: {intended_height}\n"
                                         .format(
                                         actual_width=len(self._maze[0]),
                                         actual_height=len(self._maze),
                                         intended_width=width,
                                         intended_height=height
                                         ))

    def has_been_generated(self):
        """Determine whether or not this maze has been generated and has tiles
            Returns: bool
        """
        if len(self._maze) > 0 and len(self._maze[0]) > 0:
            return True
        else:
            return False

    def get_width(self):
        """Get the width of this maze
            Return: Numeric value of the width
        """
        return self._width

    def get_height(self):
        """Get the height of this maze
            Return: Numeric value of the height
        """
        return self._height
