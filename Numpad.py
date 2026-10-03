from tkinter import *

root = Tk()
root.title("NumPad")
root.geometry('250x250')
num = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['+', 0, '-'], ['=', '^', '*']]

for i in range(4):
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        f = Frame(master=root, relief=SUNKEN, borderwidth=1)
        f.grid(column=j, row=i)
        l = Label(master=f, text=num[i][j], bg="lightblue", fg="white")
        l.pack(padx=3, pady=3)

root.mainloop()