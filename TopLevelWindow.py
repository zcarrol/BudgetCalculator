from tkinter import *

class TopLevelWindow:

    def __init__(self, win, geometry, color):
        # Set up new top level window
        self.win = win
        self.win.grab_set()
        self.win.geometry(geometry)
        self.win.configure(background=color)
        # Dictionary of Name : Textbox pointer to make working with text boxes easier
        self.tbs = {}

    def add_text_box(self, name, tb):
        self.tbs[name] = tb