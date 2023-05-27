import tkinter as tk

# Define functions for calculator operations
def add():
    result = float(num1.get()) + float(num2.get())
    answer.config(text=result)

def subtract():
    result = float(num1.get()) - float(num2.get())
    answer.config(text=result)

def multiply():
    result = float(num1.get()) * float(num2.get())
    answer.config(text=result)

def divide():
    result = float(num1.get()) / float(num2.get())
    answer.config(text=result)

# Create the GUI
root = tk.Tk()
root.title("Calculator")

# Create input fields and labels
num1_label = tk.Label(root, text="Number 1")
num1_label.grid(row=0, column=0)
num1 = tk.Entry(root)
num1.grid(row=0, column=1)

num2_label = tk.Label(root, text="Number 2")
num2_label.grid(row=1, column=0)
num2 = tk.Entry(root)
num2.grid(row=1, column=1)

# Create operation buttons
add_button = tk.Button(root, text="+", command=add)
add_button.grid(row=2, column=0)

subtract_button = tk.Button(root, text="-", command=subtract)
subtract_button.grid(row=2, column=1)

multiply_button = tk.Button(root, text="*", command=multiply)
multiply_button.grid(row=3, column=0)

divide_button = tk.Button(root, text="/", command=divide)
divide_button.grid(row=3, column=1)

# Create a label to display the result
answer_label = tk.Label(root, text="Answer:")
answer_label.grid(row=4, column=0)
answer = tk.Label(root, text="")
answer.grid(row=4, column=1)

root.mainloop()