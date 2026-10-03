from tkinter import *

root = Tk()
root.title("Log in")
root.geometry('400x350')
f = Frame(master=root, height=200, width=360, bg="gray")

l1 = Label(text="Name", fg="white", bg="lightgray", width=12)
l2 = Label(text="Email", fg="white", bg="lightgray", width=12)
l3 = Label(text="Password", fg="white", bg="lightgray", width=12)

ne = Entry(f)
ee = Entry(f)
pe = Entry(f, show="*")

def display():
    n = ne.get()
    e = ee.get()
    p = pe.get()
    g = f"Hello {n}."
    m = "\nUr account creation was successful.\nEmail: "+e+" \nPassword: "+p
    tb.insert(END, g)
    tb.insert(END, m)

tb = Text(bg="white", fg="black")
b = Button(text="Create", bg="black", command=display, fg="white")

f.place(x=20, y=0)
l1.place(x=20, y=20)
ne.place(x=150, y=20)
l2.place(x=20, y=80)
ee.place(x=150, y=80)
l3.place(x=20, y=140)
pe.place(x=150, y=140)
b.place(x=130, y=210)
tb.place(y=250)

root.mainloop()