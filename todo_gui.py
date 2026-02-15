import tkinter as tk
from tkinter import messagebox

tasks = []


# Add Task Function
def add_task():
    task = entry.get()

    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)


# Delete Task Function
def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
        tasks.pop(selected_task)

    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")


# Main Window
root = tk.Tk()
root.title("Varun's To-Do App 📝")
root.geometry("400x450")


# Heading
label = tk.Label(root, text="My To-Do List", font=("Arial", 18))
label.pack(pady=10)


# Entry Box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)


# Add Button
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), command=add_task)
add_button.pack(pady=5)


# Listbox
listbox = tk.Listbox(root, font=("Arial", 12), height=10)
listbox.pack(pady=10)


# Delete Button
delete_button = tk.Button(root, text="Delete Task", font=("Arial", 12), command=delete_task)
delete_button.pack(pady=5)


# Exit Button
exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit)
exit_button.pack(pady=10)


# Run the App
root.mainloop()
