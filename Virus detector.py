from tkinter import *
from tkinter import messagebox

w = Tk()
w.title("Virus detector")
w.geometry('200x200')

def mb():
    messagebox.showwarning("VIRUS DETECTED")

b = Button(text="Scan for a virus", fg="lightgray", bg="darkgray", command=mb)
b.place(x=50, y=80)

w.mainloop()