"""
    This is the class that contains all of the tkinter menu operations
"""

from tkinter import *
from tkinter import ttk

class MenuInterface:


    # The main window that ecapsulates the buttons and boxes
    root = Tk(className=' Budget Calculator')
    text_box_frame = ttk.Frame(root, padding=50)
    new_expenditure_window = None
    # This variable is used to indicate which row the next text box should be placed on
    next_row = 8

    # Dictionary for hexidecimal colors to make color picking easier
    colors = {
        "turq" : "#00cc99"
    }

    def __init__(self):

        # Create a default style for the frames
        s1 = ttk.Style()
        s1.configure('TFrame', background=self.colors["turq"])


        # Set the root size, color, and name
        Label(self.root, text="Budget Calculator", foreground="black")
        self.root.geometry("500x500")
        self.root.configure(background=self.colors["turq"])


        # Add button to allow user to add extra monthly expenditures
        # First line just adds some padding
        Label(self.text_box_frame, text="", background=self.colors["turq"]).grid(column=0, row=0)
        new_tb_button = Button(self.text_box_frame, text="Add New Expenditure", command=self.new_tb_name_select_window).grid(column=0, row=1)


        # Add common text boxes that the user will need
        self.text_box_frame.grid(column=3, row=3)
        self.add_text_box("Yearly Salary", self.text_box_frame, 0, 3)
        self.add_text_box("Monthy Food Expense", self.text_box_frame, 0, 5)
        self.add_text_box("Monthly Allowance", self.text_box_frame, 0, 7)



    """
        This function adds text boxes which the user will input various monthly expenditures
        and these values will be used to calculate remaining money 
    """
    def add_text_box(self, label, frame, c, r):

        text_box = Text(
            frame,
            height=1,
            width=20
        )

        label = ttk.Label(frame, text=label, foreground="black", background=self.colors["turq"], wraplength=150).grid(column=c, row=r)

        text_box.grid(column=c, row=r+1)
        text_box.insert(INSERT, "")
        text_box.config(state='normal')



    def new_tb_name_select_window(self):

        # Spawn new tk window
        winPtr = Toplevel(self.root)
        self.new_expenditure_window = TopLevelWindow(winPtr, "200x100", self.colors["turq"])

        # Add label for the text box
        label = ttk.Label(self.new_expenditure_window.win, text="Enter Expenditure Name", foreground="black", background=self.colors["turq"])
        label.grid(column=0,row=0)

        #Add text box to window
        new_field_name = StringVar()
        text_box = Entry(self.new_expenditure_window.win, textvariable=new_field_name)
        text_box.grid(column=0, row=1)
        self.new_expenditure_window.add_text_box("New Expenditure", new_field_name)

        # Add enter button
        btn = Button(self.new_expenditure_window.win, text="Enter", command=self.get_text_box_entry, padx=20)
        btn.grid(column=0,row=2)


    """
        This wont take parameters so you need to write a class for the pop up window so you can store the parameters
    """

    def get_text_box_entry(self):
        entry = self.new_expenditure_window.tbs["New Expenditure"].get()
        print(entry)
        self.next_row = self.next_row+2
        self.new_expenditure_window.win.destroy()
        self.new_expenditure_window = None
        self.add_text_box(entry, self.text_box_frame, 0, self.next_row)

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

