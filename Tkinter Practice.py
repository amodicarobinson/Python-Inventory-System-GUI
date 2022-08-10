# Create Menu bar in python GUI
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

win = tk.Tk()
win.title("Python GUI Test With Tkinter")

# Exit Action
def _quit():
    win.quit()
    win.destroy()
    exit()

# Create Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# File Menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Help Menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
helpMenu.add_cascade(label="Help", menu=helpMenu)

# Calling Main
win.mainloop()