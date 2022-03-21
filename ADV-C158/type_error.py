#data type error
from tkinter import *
root=Tk()
root.title("Addition")
root.geometry("600x400")
input_box = Entry(root)
input_box.pack()

def addition():
    number = 5
    get_input = input_box.get()
    try:
        print(number + get_input)
    except(TypeError):
	    messagebox.showinfo("Error", "Cannot add two different data types: integer and string") 
    
button = Button(root , text= "addition", command = addition)
button.pack()
root.mainloop()