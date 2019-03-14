# astar.py





class AStar:
    """The A* search Algorithm."""

    # Level map point constants
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3

    def __init__(self, level_map):
        self.level_map = level_map
        # Find the start/end points
        self.start, self.end = self.read_level_map(self.level_map)

        print("Start point found:", self.start)
        print("End point found:", self.end)

        # Initialize the open/closed lists
        self.open = self.get_points_around(self.start)
        self.closed = [self.start]

        # Initialize the search_points list, which contains F and parent points
        self.search_points = []

        print(self.open)
        self.advance()


    def read_level_map(self, level_map):
        """Reads a 2D array and returns the start and end points.
           Raises an error if there are no start or end points."""
        start = None
        end = None
        
        # Find the start/end points
        for y, row in enumerate(level_map):
            for x, point in enumerate(row):
                if point == self.START:
                    if start is None:
                        start = (x, y)
                    else:
                        raise InvalidStartError("There are multiple start points on the map.")
                elif point == self.END:
                    if end is None:
                        end = (x, y)
                    else:
                        raise InvalidEndError("There are multiple end points on the map.")
        
        # Check if there any start/end points were found.
        if start is None:
            raise InvalidStartError("There is no start point on the map.")
        if end is None:
            raise InvalidEndError("There is no end point on the map.")

        return start, end

    def advance(self):
        """Advances the search."""
        # Get the point on the open list which has the lowest score.
        s = self.calculate_score((0, 0))

    def get_points_around(self, point):
        """Returns a list of points around (up, down, left, right) a Point."""
        x, y = point.x, point.y
        points = []

        # Up
        if y-1 > 0 and self.level_map[y-1][x] is not None:
            points.append((x, y-1))
        # Down
        if y+1 < len(self.level_map) and self.level_map[y+1][x] is not None:
            points.append((x, y+1))
        # Left
        if x-1 > 0 and self.level_map[y][x-1] is not None:
            points.append((x-1, y))
        # Right
        if x+1 < len(self.level_map[0]) and self.level_map[y][x+1] is not None:
            points.append((x+1, y))

        return points

    def calculate_score(self, point):
        """Calculates F for a point."""
        print(point)
        # Calculate G: the movement cost from the start point to the current point
        g = point.parent.g + 1

        # Calculate H: the estimated movement cost from the current point to the end point
        # Manhattan distance method: # of horizontal + # of vertical squares to reach the end
        h = abs(self.end[0] - point[0]) + abs(self.end[1] - point[1])

        return g + h


class Point:

    def __init__(self, x, y, g, h, parent=None):
        self.x, self.y = x, y
        self.f, self.g, self.h = g+h, g, h
        self.parent = parent

    def update_score(self, g, h):
        self.f, self.g, self.h = g+h, g, h


class InvalidStartError(Exception):
    pass

class InvalidEndError(Exception):
    pass