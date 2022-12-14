# Create Menu bar in python GUI
import csv as csv
import tkinter as tk
from tkinter import END, Button, Entry, Label, Toplevel, ttk
from tkinter import Menu
from tkinter import filedialog
from tkinter import messagebox
from typing import Text
from csv import *
from datetime import date

win = tk.Tk()
win.title("Python Inventory GUI")
win.geometry("750x500")
win.config(background="white")
main_lst=[]

today = date.today()

# Exit Action
def _quit():
    win.quit()
    win.destroy()
    exit()

class NewWindow(Toplevel):
    
    def __init__(self, master = None):
        
        super().__init__(master= master)
        self.title("Inventory")
        self.geometry("550x250")
        self.resizable(height=False, width=False)
        
        text = tk.Text(self, height=12)
        text.grid(column=0, row=0, sticky='nsew')
        
        def open_text_file():
            # file type
            filetypes = (
                ('CSV files', '*.csv'),
                ('text files', '*.txt'),
                ('All files', '*.*')
            )
            # show the open file dialog
            f = filedialog.askopenfile(filetypes=filetypes)
            # read the text file and show its content on the Text
            text.insert('1.0', f.readlines())
            
        # open file button
        open_button = Button(
            self,
            text='Open a File',
            command= open_text_file
        )
        
        open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)
        
        
        
    
        
                

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
    lst=[initials.get(),today,cname.get(),uname.get(),"CND1193"+sn.get(),stock.get()]
    main_lst.append(lst)
    messagebox.showinfo("Information","Saved successfully")

def save():
    with open("inventory.csv", "w") as file:
        Writer = writer(file)
        Writer.writerow(["Initials","Date","Computer Name","Name", "S/N", "Stock"])
        Writer.writerows(main_lst)
        messagebox.showinfo("Information","Saved successfully")
        
def clear():
    initials.delete(0,END)
    # date.delete(0,END)
    cname.delete(0,END)
    uname.delete(0,END)
    sn.delete(0,END)
    stock.delete(0,END)
    


# Labels
label1 = Label(win, text="Initals: ",padx=20, pady=10)
# label2 = Label(win, text="Date: ",padx=20, pady=10)
label3 = Label(win, text="Computer Name: ",padx=20, pady=10)
label4 = Label(win, text="User Name: ",padx=20, pady=10)
label5 = Label(win, text="S/N: ",padx=20, pady=10)
label6 = Label(win, text="Stock: ",padx=20, pady=10)

# Entry Fields
initials = Entry(win,width=30,borderwidth=3)
# date = Entry(win,width=30,borderwidth=3)
cname = Entry(win,width=30,borderwidth=3)
uname = Entry(win,width=30,borderwidth=3)
sn = Entry(win,width=30,borderwidth=3)
stock = Entry(win,width=30,borderwidth=3)

# Buttons 
save = Button(win,text="Save", padx=20, pady=10,command=save)
add = Button(win,text="Add", padx=20, pady=10,command=add)
clear = Button(win,text="Clear", padx=10, pady=10,command=clear)
OpenWindow = Button(win,text="Check Inventory", padx=10, pady=10)
exitB = Button(win, text="Exit", padx=10, pady=10, command=_quit )

OpenWindow.bind("<Button>",
                lambda e: NewWindow(win))

label1.grid(row=0, column=1) 
#label2.grid(row=1, column=1)
label3.grid(row=2, column=1)
label4.grid(row=3, column=1)
label5.grid(row=4, column=1)
label6.grid(row=5, column=1)

label1.config(bg="white")
#label2.config(bg="white")
label3.config(bg="white")
label4.config(bg="white")
label5.config(bg="white")
label6.config(bg="white")

initials.grid(row=0,column=2)
#date.grid(row=1,column=2)
cname.grid(row=2,column=2)
uname.grid(row=3,column=2)
sn.grid(row=4,column=2)
stock.grid(row=5,column=2)

save.grid(row=7,column=2, columnspan=2, pady=20)
add.grid(row=6,column=2, columnspan=2, pady=20)
clear.grid(row=8,column=2, columnspan=2, pady=20)
OpenWindow.grid(row=6, column=4, padx=50)
exitB.grid(row=7, column=4, padx=50)

save.config(bg="black", fg="white")
add.config(bg="black", fg="white")
clear.config(bg="black", fg="white")
OpenWindow.config(bg="red", fg="white")
exitB.config(bg="red",fg="white")


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
print(main_lst)