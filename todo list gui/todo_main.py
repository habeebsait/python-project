from tkinter import *
from tkinter import messagebox

task = []
ORANGE = "#ffa31a"
GREY = "#d1d1e0"
completed = []
i=0


def add():
    global task

    t = task_entry.get()
    if t == "":
        messagebox.showinfo(title = "Warning!!", message= "Task cannot be empty")
    else:
        task.append(t)
    display()

def display():
    global i
    Lb.delete(0,END)
    for _ in task:
        Lb.insert(task.index(_),f"Task {task.index(_)}: {_}")
        task_entry.delete(0,END)


def delete():
    global task, completed
    
    chosen = Lb.curselection()
    if len(chosen) != 0:
        Lb.delete(chosen)
        c = task[chosen[0]]
        completed.append(c)
        Lb1.delete(0, END)
        for _ in completed:
            Lb1.insert(completed.index(_), f"Task {completed.index(_)}: {_}")

        task.remove(task[chosen[0]])
        print(task)

        display()
    else:
        messagebox.showinfo(title= "Error!", message= "Choose a task to mark as completed")


window = Tk()
window.title("Todo List")
window.config(bg = GREY, padx = 50, pady = 50)
window.minsize(600,900)

task_entry = Entry()
task_entry.focus()
task_entry.place(x=150,y=300)


task_label = Label(text = "Todo List", font = ("Arial", 24, "bold"), bg = ORANGE, highlightthickness=0)
task_label.place(x= 190,y=0)

completed_label = Label(text = "Completed Tasks", font =("Arial", 24, "bold"), bg = ORANGE, highlightthickness=0)
completed_label.place (x=140, y= 450)

Lb = Listbox(height = 12, width = 40)
Lb.place(x=60, y=80)

Lb1 = Listbox(height = 12, width = 40)
Lb1.place(x = 60, y = 500)

add_button = Button(text = "Add", command = add, padx=30, pady=30)
add_button.place(x=10, y=350)

delete_button = Button(text = "Task Completed",bg = "red", command = delete, padx = 30, pady=30)
delete_button.place(x=300, y=350)








window.mainloop()
