import tkinter as tk
root=tk.Tk()
root.geometry("450x700")
root.title("Calculator")
display=tk.Entry(root,text="display",bd=5).grid(row=0,column=0)
numpad=tk.LabelFrame(root,text="this is keypad").grid(row=1,column=0)
root.mainloop()