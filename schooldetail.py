import tkinter as tk
root=tk.Tk()
root.geometry("600x600")
root.title("My love for doremon")
mainframe=tk.LabelFrame(root)
label=tk.LabelFrame(root,height=5,text="Love")
label1=tk.LabelFrame(mainframe,height=4)
label2=tk.LabelFrame(mainframe,height=4)
label.grid(row=0,column=1)
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
name_label=tk.Entry(label,font=("Akaash",30))
ok_lable=tk.Label(label1,text="label1")
ok_lable.grid(row=2,column=0)
name_label.grid(row=3,column=0)
dropbox_label=tk.Button(label,text="click")
dropbox_label.grid(row=0,column=0)
mainframe.grid(row=4,column=0)
for widget in mainframe.winfo_children():
    widget.grid_configure(padx=10,pady=10)
root.mainloop()