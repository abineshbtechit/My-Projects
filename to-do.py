import tkinter as tk
from tkinter import messagebox
import json, os

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f)

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        update_list()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty", "Enter a task")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        save_tasks(tasks)
        update_list()
    except:
        messagebox.showwarning("Select", "Select a task to delete")

def update_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, t)

app = tk.Tk()
app.title("To-Do List")

tasks = load_tasks()

entry = tk.Entry(app, width=30)
entry.pack(pady=10)

btn_add = tk.Button(app, text="Add Task", command=add_task)
btn_add.pack()

btn_delete = tk.Button(app, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)

listbox = tk.Listbox(app, width=45, height=10)
listbox.pack(pady=10)

update_list()
app.mainloop()

