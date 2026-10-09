from tkinter import *

w = Tk()
w.title("Event Handler")
w.geometry('150x150')

def kp(e):
    """Print the character associated to the key pressed"""
    print(e.char)

w.bind("<Key>", kp)

def c(e):
    print("\nButton clicked.")

b = Button(text="Click me", fg="white", bg="lightblue")
b.pack()
b.bind("<Button-1>", c)

w.mainloop()