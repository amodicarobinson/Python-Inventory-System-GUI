# Create Menu bar in python GUI
import tkinter as tk
from tkinter import Label, ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
from typing import Text
import csv
from csv import *

win = tk.Tk()
win.title("Python GUI Test With Tkinter")
win.geometry("500x500")
win.config(background="white")
main_lst=[]
# Exit Action
def _quit():
    win.quit()
    win.destroy()
    exit()

# Function for opening the file explorer
def _file():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title= "Select a File",
                                          filetypes=(("Text Files",
                                                      ".txt*"),
                                                     ("All Files",
                                                      "*.*")))
    file_explorer.config(text="File Open:"+filename)
    
    
def add():
    lst=[initials.get(),date.get(),cname.get(),uname.get(),sn.get(),stock.get()]
    main_lst.append(lst)
    messagebox.showinfo("Information","Saved successfully")

def save():
    with open("inventory.csv", "w") as file:
        Writer = writer(file)
        Writer = writerow(["Initials","Date","Computer Name","Name", "S/N", "Stock"])
        Writer.writerows(main_lst)
        messagebox.showinfo("Information","Saved successfully")
        
def clear():
    initials.delete()
    date.delete()
    cname.delete
# File explorer Window
file_explorer = Label(win,
                      text="File Explorer",
                      width=100, height=10,
                      fg="blue")
# Create Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# File Menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Open", command=_file)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Help Menu
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
helpMenu.add_cascade(label="Help", menu=helpMenu)

# Calling Main
win.mainloop()