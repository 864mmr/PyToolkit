from tkinter import Tk, Label, Menu, Menubutton, messagebox
from os import listdir, system, getcwd, chdir

root = Tk()
root.title("pyToolkit")
root.resizable(height = False, width = False)
root.geometry("300x100")
defaultFont = ("Segoe UI Light", 12)

#status bar
status = Label(root, text = "By 864mmr", anchor = 'w', font = defaultFont)
status.pack(side = 'bottom', fill = 'x')

#menu bar
m = Menu(root)
root.config(menu = m)
m.add_cascade(label = "About", command = lambda : messagebox.showinfo('About', 'pyToolkit: A simple set of tools'))
m.add_cascade(label = "Exit", command = root.destroy)

#drop-down menu
m2 = Menubutton(root, text="<< Select App >>", font = defaultFont,
                width = 200, height = 100, bd = 5, relief = 'ridge')
m2.menu  = Menu(m2, tearoff = 0)
m2["menu"] = m2.menu

# Accesses the Apps folder and loads available apps
mydir = getcwd()
mydir_new = chdir(mydir+"\\Tools")
for file in listdir():
    f = open(file, 'r')
    m2.menu.add_command(label = f.readline()[2:], command = lambda c = file: system(c))
    f.close()
m2.pack()
root.mainloop()
