from tkinter import *
from datetime import date

root = Tk()
root.title("Check In")
root.geometry('400x300')

l = Label(text="Workshop Check In", fg="white", bg="lightgreen")
ln = Label(text="Name", fg="white", bg="lightgreen")
ne = Entry()    

def display():
    n = ne.get()
    g = f"Welcome {n}! You have checked in."
    m = "\n Date: "+ str(date.today())
    tb.insert(END, g)
    tb.insert(END, m)

tb = Text(height=3)
b = Button(text="Check In", command=display, fg="white", bg="green")

l.pack()
ln.pack()
ne.pack()
b.pack()
tb.pack()

root.mainloop()