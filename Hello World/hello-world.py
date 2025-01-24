from tkinter import *
from tkinter import ttk
root = Tk()
root.title("msg to ms. chavez")
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="hey guys!").grid(column=0, row=0)
ttk.Label(frm, text="i hate ms chavez so much, the english teacher though").grid(column=0, row=2)
ttk.Button(frm, text="fuck her man", command=root.destroy).grid(column=0, row=3)
root.mainloop()
