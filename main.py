from visualization import Visualization
from astar import AStar
from tkinter import *
from config import *
from time import time


class Main:

    def __init__(self):
        # Initialize master GUI
        self.master = Tk()
        self.master.title("A* Search Algorithm")

        # Initialize canvas
        self.visualization = Visualization(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

        # Initialize A*
        self.astar = AStar(DEFAULT_MAP)

        print("GUI done loading... beginning main loop...")

        # Main loop
        while True:
            self.visualization.tick()

            self.master.update_idletasks()
            self.master.update()


if __name__ == "__main__":
    Main()
