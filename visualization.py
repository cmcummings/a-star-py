# visualization.py
from tkinter import Canvas, ALL
from config import *
from time import time 


current_time_millis = lambda: int(round(time() * 1000))


class Visualization(Canvas):
    """The canvas on which a visualization of the A* Algorithm is drawn on."""

    def __init__(self, master, **options):
        # Initialize canvas
        Canvas.__init__(self, master, **options) # Initialize parent class
        self.grid(row=0, column=0)

        self.last_update = current_time_millis() # FPS

        # Control variables
        self.x_offset, self.y_offset = 0, 0
        self.scale = 1

        self.node_map = None

    def tick(self):
        if current_time_millis() - self.last_update >= 1000/CANVAS_FPS:
            self.logic()
            self.draw()
            self.last_update = current_time_millis()

    def logic(self):
        pass

    def draw(self):
        self.delete(ALL) # Delete all objects from the previous draw loop
        self.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="white", width=0) # Clear the screen

        # Draw the nodes
        node_width = 50 * self.scale
        for y, row in enumerate(self.node_map):
            for x, node in enumerate(row):
                self.create_rectangle(x*node_width+self.x_offset, y*node_width+self.y_offset, node_width, node_width, 
                                      fill='white', outline='black', width=1)
