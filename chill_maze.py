from maze_abstract_base import MazeAbstractBase
from chill_tile import ChillTile


class ChillMaze(MazeAbstractBase):

    def __init__(self, width, height, tile_class=ChillTile):
        """Initialization logic for the maze
            Params:
                width: numeric value for the grid width of the maze
                height: numeric value for the gird height of the maze
            Raises:
                ValueError: If width or height cannot be numerically
                            interpreted and are not greater than zero
        """
        super().__init__(width, height, tile_class)
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
        self._tile_class = tile_class
        self._maze = []
        self._neighborhood = {}

        # Time to actually initialize the tiles
        # Lets go through each row
        for row_number in range(height):
            # Then create all columns
            column = []
            for column_number in range(width):
                tile = self._tile_class()
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

        self._set_tile_neighbors_relationship()

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

    def get_tiles_in_row(self, index):
        """Return all tiles on a specific row (horizontal dimension)
            !!!Remember that tile indexing is 0,0 at the top left corner!!!
            Params:
                index: integer
            Returns:
                List of tiles (TileAbstractBase)
            Raises:
                IndexError: If supplied index is invalid
        """
        try:
            tiles = self._maze[index]
            return tiles
        except IndexError:
            raise IndexError("Invalid value, {} not a valid index for a row"
                             .format(index))

    def get_tiles_in_column(self, index):
        """Return all tiles from a specific column (vertical dimension)
            Params:
                index integer
            Returns:
                List of tiles (TileAbstractBase)
            Raises:
                IndexError: If supplied index is invalid
        """
        try:
            tiles = []
            for row in self._maze:
                tiles.append(row[index])
            return tiles
        except IndexError:
            raise IndexError("Invalid value, {} not a valid index for a column"
                             .format(index))

    def get_tile_at(self, horizontal_index, vertical_index):
        """Return the tile at a specific location (x,y)
            Params:
                horizontal_index numeric index for the horizontal axis
                vertical_index numeric index for the vertical axis
            Returns:
                A TileAbstractBase
            Raises:
                Index error if any of the provided indexes is not valid
        """
        row = self.get_tiles_in_row(vertical_index)
        try:
            tile = row[horizontal_index]
        except IndexError:
            raise IndexError("Invalid position: {horizontal},{vertical}"
                             .format(horizontal=horizontal_index,
                                     vertical=vertical_index))
        return tile

    def _set_tile_neighbors_relationship(self):
        """Initialize data to determine tile neighbors

        This sets the data so we later can determine the neighbor of a tile
        It iterates over every tile and then saves data in an internal dict

        If a tile is at the border of a maze, it sets None as its neighbor
        """
        for vertical_index in range(self.get_height()):
            for horizontal_index in range(self.get_width()):
                current_tile = self.get_tile_at(horizontal_index,
                                                vertical_index)

                # North neighbor
                north_neighbor = None
                if vertical_index > 0:
                    north_neighbor = self.get_tile_at(horizontal_index,
                                                      vertical_index-1)

                # East neighbor
                east_neighbor = None
                if horizontal_index < self.get_width()-1:
                    east_neighbor = self.get_tile_at(horizontal_index+1,
                                                     vertical_index)

                # South neighbor
                south_neighbor = None
                if vertical_index < self.get_height()-1:
                    south_neighbor = self.get_tile_at(horizontal_index,
                                                      vertical_index+1)

                # West neighbor
                west_neighbor = None
                if horizontal_index > 0:
                    west_neighbor = self.get_tile_at(horizontal_index-1,
                                                     vertical_index)

                self._save_tile_neighbors_relationship(current_tile,
                                                       north_neighbor,
                                                       east_neighbor,
                                                       south_neighbor,
                                                       west_neighbor)

    def _save_tile_neighbors_relationship(self, reference_tile,
                                          north_neighbor,
                                          east_neighbor,
                                          south_neighbor,
                                          west_neighbor):
        """Save in our internal dictionary a tile neighbors
            Each entry in our dictionary is in the form:
            {tile: [north_tile, east_tile, south_tile, west_tile]}

            Params:
                reference_tile: TileAbstractBase for which we are saving the
                               the actual neighbor data
                north_neighbor: TileAbstractBase located at the north
                east_neighbor: TileAbstractBase located at the east
                south_neighbor: TileAbstractBase located at the south
                west_neighbor: TileAbstractBase located at the west

        """
        self._neighborhood[reference_tile] = [north_neighbor,
                                              east_neighbor,
                                              south_neighbor,
                                              west_neighbor]

    def _get_tile_neighbor(self, tile, neighbor_position):
        """Internal function to retrieve a tile neighbor
            Params:
                tile: TileAbstractBase for which we want to get the neighbor
                neighbor_position: str containing the location of the neighbor
            Returns:
                TileAbstractBase
            Raises:
                KeyError: If neighbor position provided is invalid
        """
        relationship_index = None
        if neighbor_position.capitalize() == "North":
            relationship_index = 0
        elif neighbor_position.capitalize() == "East":
            relationship_index = 1
        elif neighbor_position.capitalize() == "South":
            relationship_index = 2
        elif neighbor_position.capitalize() == "West":
            relationship_index = 3

        #Check we have a valid position to search for
        if relationship_index is None:
            raise ValueError("{} is not a valid neighbor position"
                             .format(neighbor_position))
        try:
            return self._neighborhood[tile][relationship_index]
        except KeyError:
            raise ValueError("No neighbor data found for tile")

    def get_tile_north_neighbor(self, tile):
        """Return the north neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase
        """
        return self._get_tile_neighbor(tile, "North")

    def get_tile_east_neighbor(self, tile):
        """Return the east neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase
        """
        return self._get_tile_neighbor(tile, "East")

    def get_tile_south_neighbor(self, tile):
        """Return the south neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase
        """
        return self._get_tile_neighbor(tile, "South")

    def get_tile_west_neighbor(self, tile):
        """Return the west neighbor of a tile
            Params:
                tile: TileAbstractBase
            Returns:
                TileAbstractBase
        """
        return self._get_tile_neighbor(tile, "West")

    def connect_tiles(self, tile_1, tile_2):
        """Connect two neighbor tiles (knocks appropriate walls)
            Params:
                tile_1: TileAbstractBase
                tile_2: TileAbstractBase
            Raises:
                ValueError if tiles are not neighbors
        """
        if self.get_tile_north_neighbor(tile_1) == tile_2:
            # tile_2 is north of tile_1, knock tile_2 south wall
            # and tile_1 north wall
            tile_1.knock_wall("North")
            tile_2.knock_wall("South")
        elif self.get_tile_east_neighbor(tile_1) == tile_2:
            # tile_2 is east of tile_1, knock tile_2 west wall
            # and tile_1 east wall
            tile_1.knock_wall("East")
            tile_2.knock_wall("West")
        elif self.get_tile_south_neighbor(tile_1) == tile_2:
            # tile_2 is south of tile_1, knock tile_2 north wall
            # and tile_1 south wall
            tile_1.knock_wall("South")
            tile_2.knock_wall("North")
        elif self.get_tile_west_neighbor(tile_1) == tile_2:
            # tile_2 is west of tile_1, knock tile_2 east wall
            # and tile_1 west wall
            tile_1.knock_wall("West")
            tile_2.knock_wall("East")
        else:
            raise ValueError("Tiles are not neighbors")