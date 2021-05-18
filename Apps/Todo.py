# To-Do List Maker

from tkinter import Tk, Menu, Label, Entry, Button, Listbox
import tkinter.messagebox as tkm
from tkinter.simpledialog import askstring

# main window

root= Tk()
root.title("To-do")
root.resizable(height = False, width = False)
defaultFont = ("Segoe UI Light", 14)

# functions creation

def update_listbox():
    num=1
    clear_listbox()
    for task in tasks:
        lb_tasks.insert('end','%i) %s' % (num,task))
        num+=1

def clear_listbox():
    lb_tasks.delete(0,'end')

def add_task():
    task= txt_input.get()
    if task!='':
        tasks.append(task)
        update_listbox()
    txt_input.delete(0, 'end')

    
def delete():
    task = lb_tasks.get('active')[3:]
    if task in tasks:
        tasks.remove(task)
    update_listbox()

def deleteall():
    j=tkm.askyesno("Confirm: Delete All","Do you really want to delete all?")
    if j==True:
        global tasks
        tasks=[]
        update_listbox()

def export():
    s=askstring('Enter Title','Enter a title for the tasks list export: ')
    f=open(s+'.txt','w+')
    f.write(s+': \n')
    num=1
    for i in tasks:
        f.write(str(num)+') '+i+'\n')
        num+=1
    j=tkm.askyesno("Export Complete","Export complete\n Do you want to clear the current tasks?")
    if j==True:
        deleteall()
        
tasks=[]

# display elements

lbl_title = Label(root, text='To-do List Maker',font = defaultFont)
lbl_title.grid(row=0,column=0,columnspan=2)

txt_input = Entry(root, width=15, font = defaultFont)
txt_input.grid(row=1,column=1)

btn_add_task = Button(root, text='Add task', command=add_task, font = defaultFont)
btn_add_task.grid(row=1,column=0)

btn_delete = Button(root, text='Delete',  command=delete, font = defaultFont)
btn_delete.grid(row=2,column=0)

btn_delete_all = Button(root, text='Delete all', command=deleteall, font = defaultFont)
btn_delete_all.grid(row=3,column=0)

btn_export = Button(root, text='Export', command=export, font = defaultFont)
btn_export.grid(row=4,column=0)

lb_tasks = Listbox(root, font = defaultFont)
lb_tasks.grid(row=2,column=1,rowspan=6)

# Menu Bar
menubar = Menu(root)
menubar.add_cascade(label = "Exit", command = root.destroy)
root.config(menu = menubar)

root.mainloop()
