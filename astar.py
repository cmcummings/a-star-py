# astar.py



get_distance_to_end = lambda node, end: abs(end[0] - node.x) + abs(end[1] - node.y)

class AStar:
    """The A* search Algorithm."""

    # Level map node constants
    EMPTY = 0
    WALL = 1
    START = 2
    END = 3

    def __init__(self, level_map):
        self.level_map = level_map
        # Find the start/end nodes
        self.start, self.end = self.read_level_map(self.level_map)

        print("Start node found:", self.start)
        print("End node found:", self.end)

        # Initialize start node
        self.start_node = Node(self.start[0], self.start[1])
        self.start_node.g = 0
        self.start_node.h = get_distance_to_end(self.start_node, self.end)

        # Initialize the open/closed lists
        self.open = self.get_nodes_around(self.start)
        self.closed = [self.start_node]

        self.advance()


    def read_level_map(self, level_map):
        """Reads a 2D array and returns the start and end nodes.
           Raises an error if there are no start or end nodes."""
        start = None
        end = None
        
        # Find the start/end nodes
        for y, row in enumerate(level_map):
            for x, node in enumerate(row):
                if node == self.START:
                    if start is None:
                        start = (x, y)
                    else:
                        raise InvalidStartError("There are multiple start nodes on the map.")
                elif node == self.END:
                    if end is None:
                        end = (x, y)
                    else:
                        raise InvalidEndError("There are multiple end nodes on the map.")
        
        # Check if there any start/end nodes were found.
        if start is None:
            raise InvalidStartError("There is no start node on the map.")
        if end is None:
            raise InvalidEndError("There is no end node on the map.")

        return start, end

    def advance(self):
        """Advances the search."""
        # Get the node on the open list which has the lowest score (S).
        S = self.open[0]
        for node in self.open:
            if node.f < S.f:
                S = node
        # Remove S from the open list and add it to the closed list
        self.open.remove(S)
        self.closed.append(S)
        # For each node T in S’s walkable adjacent tiles: 
        for T in self.get_nodes_around(S):
            T_node = Node(T[0], T[1], parent=S)
            g, h = self.calculate_score(T_node)
            T_node.update_score(g, h)
            # - If T is in the closed list: 
            #       Ignore it.
            if T_node in self.closed:
                continue
            
            in_open = False
            for node in self.open:
                if node.pos() == T_node.pos()
                    in_open = True
            # - If T is not in the open list: 
            #       Add it and compute its score.
            if not in_open:
                self.open.append(T)
            # - If T is already in the open list: 
            #       Check if the F score is lower when we use the 
            #       current generated path to get there. 
            #       If it is, update its score and update its parent as well.
            else:
                T_old = self.open


    def get_nodes_around(self, node):
        """Returns a list of coordinates around (up, down, left, right) a node."""
        x, y = node.x, node.y
        coords = []

        # Up
        if y-1 > 0 and self.level_map[y-1][x] is not self.WALL:
            coords.append((x, y-1))
        # Down
        if y+1 < len(self.level_map) and self.level_map[y+1][x] is not self.WALL:
            coords.append((x, y+1))
        # Left
        if x-1 > 0 and self.level_map[y][x-1] is not self.WALL:
            coords.append((x-1, y))
        # Right
        if x+1 < len(self.level_map[0]) and self.level_map[y][x+1] is not self.WALL:
            coords.append((x+1, y))

        return coords

    def calculate_score(self, node):
        """Calculates and returns G, H for a node."""
        # Calculate G: the movement cost from the start node to the current node
        g = node.parent.g + 1

        # Calculate H: the estimated movement cost from the current node to the end node
        # Manhattan distance method: # of horizontal + # of vertical squares to reach the end
        h = get_distance_to_end(node, self.end)

        return g, h


class Node:
    """A node on the map"""

    def __init__(self, x, y, parent=None):
        self.x, self.y = x, y
        self.f, self.g, self.h = 0, 0, 0
        self.parent = parent

    def update_score(self, g, h):
        self.f, self.g, self.h = g+h, g, h

    def pos(self):
        return (self.x, self.y)

    def __str__(self):
        return "Node(" + x + ", " + y + "): F=" + self.f + " G=" + self.g + " H=" + self.h


class InvalidStartError(Exception):
    pass

class InvalidEndError(Exception):
    pass