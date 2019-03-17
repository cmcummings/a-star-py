# control_panel.py
from tkinter import Frame, Button

class ControlPanel(Frame):

    def __init__(self, master, **options):
        Frame.__init__(self, master, **options)
        self.grid(row=0, column=1)
        self.config(padx=5, pady=5)

        self.b_advance = Button(self, text="Advance", command=master.advance)
        self.b_advance.pack(padx=5, pady=5, side='top')

        