from tkinter import *
from tkinter import messagebox
import os

DATA_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
        save_task_list()
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteTask():
    lb.delete(ANCHOR)
    save_task_list()

def save_task_list():
    tasks = lb.get(0, END)
    save_tasks(tasks)

    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To_Do_List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)


task_list = load_tasks()

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)



ws.mainloop()
