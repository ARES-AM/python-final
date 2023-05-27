import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.geometry("500x850")
root.title("DOREMON")
# styling
s=ttk.Style()
# make 2 colum and add label frame in 1st column
fra=tk.Frame(root).grid(row=0,column=0,padx=50,pady=7)
lbfram=tk.Label(fra,text="doremon",width=10).grid(row=0,column=1,sticky='NW')
LABELFR=tk.Label(fra,text='dor').grid(row=0,column=2,sticky='W')
root.mainloop()