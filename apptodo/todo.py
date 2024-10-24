import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x400")

        # Task List
        self.tasks = []

        # GUI Elements
        self.task_label = tk.Label(self.root, text="Enter your task:", font=("Arial", 14))
        self.task_label.pack(pady=10)

        self.task_entry = tk.Entry(self.root, width=30, font=("Arial", 14))
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", width=15, font=("Arial", 12), command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, height=10, width=35, font=("Arial", 12))
        self.task_listbox.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Selected Task", width=20, font=("Arial", 12), command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", width=20, font=("Arial", 12), command=self.clear_tasks)
        self.clear_button.pack(pady=5)

    def add_task(self):
        """Add a new task to the list."""
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)  # Clear the input field
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def remove_task(self):
        """Remove the selected task."""
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_task_index]
            if messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete '{task}'?"):
                self.tasks.pop(selected_task_index)
                self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to remove.")

    def clear_tasks(self):
        """Clear all tasks."""
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()
            self.update_task_listbox()

    def update_task_listbox(self):
        """Update the listbox with the current task list."""
        self.task_listbox.delete(0, tk.END)  # Clear listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()