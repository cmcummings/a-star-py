# visualization.py
from tkinter import Canvas, ALL
from config import *
from time import time 


current_time_millis = lambda: int(round(time() * 1000))


class Visualization(Canvas):
    """The canvas on which a visualization of the A* Algorithm is drawn on."""

    def __init__(self, master, **options):
        Canvas.__init__(self, master, **options) # Initialize parent class
        self.pack()

        self.last_update = current_time_millis()

        print("Canvas initialized...")

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