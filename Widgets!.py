from tkinter import *
from datetime import date

root = Tk()
root.title("Widgets!")
root.geometry("400x300")

l = Label(text="Widgeeeeetsss!!", fg="white", bg="lightblue", height=1, width=300)
nl = Label(text="Name???", bg="cyan")
e = Entry()

def display():
    n = e.get()
    global m
    m = ":D \n Da date today iz:- "
    g = "Hola "+n+"!"+"\n"
    tb.insert(END, g)
    tb.insert(END, m)
    tb.insert(END, date.today())

tb = Text(height=3)
b = Button(text="Click!", command=display, height=1, fg="white", bg="lightblue")

l.pack()
nl.pack()
e.pack()
b.pack()
tb.pack()
root.mainloop()