class ChillMazeTile:
    _wallTop = True
    _wallBottom = True
    _wallRight = True
    _wallLeft = True

    def are_all_walls_up(self):
        return self._wallBottom and self._wallLeft and \
            self._wallRight and self._wallTop

    def knock_wall(self, location):
        if location.capitalize() == "Top":
            self._wallTop = False
        elif location.capitalize() == "Bottom":
            self._wallBottom = False
        elif location.capitalize() == "Left":
            self._wallLeft = False
        elif location.capitalize() == "Top":
            self._wallTop = False
        else:
            raise ValueError("Invalid wall location provided: {}"
                             .format(location))


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