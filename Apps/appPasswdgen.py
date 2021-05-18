# Password Generator

import random 
from tkinter import Tk, Menu, IntVar, Label, Entry, Button, Radiobutton
from tkinter.ttk import Combobox
  
# Various functions to be used within this program
def low(): 
    entry.delete(0, 'end') 
  
    # Get the length of passowrd 
    length = var1.get() 
  
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()"
    password = "" 
  
    # if strength selected is low 
    if var.get() == 1: 
        for i in range(0, length): 
            password = password + random.choice(lower) 
        return password 
  
    # if strength selected is medium 
    elif var.get() == 0: 
        for i in range(0, length): 
            password = password + random.choice(upper) 
        return password 
  
    # if strength selected is strong 
    elif var.get() == 3: 
        for i in range(0, length): 
            password = password + random.choice(digits) 
        return password 
    else: 
        print("Please choose an option") 
  
  
# Function for generation of password 
def generate():
    try:
        password1 = low() 
        entry.insert(10, password1)
    except:
        entry.insert(10, 'Error')
  
# Main Function 
  
# create GUI window 
root = Tk()
root.resizable(height = False, width = False)
var = IntVar() 
var1 = IntVar() 
defaultFont = ("Segoe UI Light", 14)

# Title of your GUI window 
root.title("Password Generator") 
  
# create label and entry to show 
# password generated 
Random_password = Label(root, text="Password: ", font = defaultFont) 
Random_password.grid(row=0) 
entry = Entry(root, font = defaultFont, width = 40) 
entry.grid(row=0, column=1) 
  
# create label for length of password 
c_label = Label(root, text="Length: ", font = defaultFont) 
c_label.grid(row=1, sticky = 'w') 
  
# button to generate the password
generate_button = Button(root, text="Generate", command=generate, font = defaultFont) 
generate_button.grid(row=0, column=3)

# Radio Buttons for deciding the 
# strength of password 
# Default strength is Medium 
radio_low = Radiobutton(root, text="Low", variable=var, value=1, font = defaultFont) 
radio_low.grid(row=1, column=2, sticky='E') 
radio_middle = Radiobutton(root, text="Medium", variable=var, value=0, font = defaultFont) 
radio_middle.grid(row=1, column=3, sticky='E') 
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3, font = defaultFont) 
radio_strong.grid(row=1, column=4, sticky='E') 
combo = Combobox(root, textvariable=var1, width = 19, font = defaultFont) 
  
# Combo Box for length of your password 
combo['values'] = [i for i in range(8, 33)]
combo.current(0) 
combo.bind('<<ComboboxSelected>>') 
combo.grid(column=1, row=1, sticky = 'w') 

# Menu Bar
menubar = Menu(root)
menubar.add_cascade(label = "Exit", command = root.destroy)
root.config(menu = menubar)

root.mainloop() 
