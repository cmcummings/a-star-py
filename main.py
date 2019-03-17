from visualization import Visualization
from control_panel import ControlPanel
from astar import AStar
from tkinter import *
from config import *
from time import time

class Main(Tk):

    def __init__(self):
        Tk.__init__(self)
        # Initialize master GUI
        self.title("A* Search Algorithm")
        self.geometry("{}x{}".format(WIDTH, HEIGHT))
        self.resizable(0, 0)

        # Initialize A*
        self.astar = AStar(DEFAULT_MAP)

        # Initialize canvas
        self.visualization = Visualization(self, self.astar.get_node_map(), width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

        # Initialize control panel
        self.control_panel = ControlPanel(self)

        # For testing purposes:
        # while self.astar.end_path is None:
        #     self.astar.advance()

        # path = self.astar.get_final_path()
        # for node in path:
        #     print(node)

        # print(self.astar.get_node_map())

        # Main loop
        while True:
            self.visualization.tick()

            self.update_idletasks()
            self.update()
    
    def advance(self):
        """Advances the algorithm and updates the visualization."""
        msg = self.astar.advance()
        if msg == "NO_PATH":
            pass
        elif msg == "SOLVED":
            self.visualization.node_map = self.astar.get_node_map_path()
        else:
            self.visualization.node_map = self.astar.get_node_map()


if __name__ == "__main__":
    Main()
