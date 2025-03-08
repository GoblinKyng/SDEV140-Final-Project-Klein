"""
ClockWise - A To-Do List Application
Author: Mark Klein
Date Written: 03/08/2025

Description:
This is a simple to-do list application built using Tkinter. 
It allows users to add tasks with a due date and category, 
mark tasks as completed, and display reminders for tasks due today.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
import os

#Function to validate the date input
def validateDate(dateString):
    """Validates if the input string is in the correct date format (YYYY-MM-DD)"""
    try:
        datetime.strptime(dateString, "%Y-%m-%d")  #Check if format is correct
        return True
    except ValueError:
        return False  


#Main Window Class 
class ClockWiseApp(tk.Tk):
    """The main application window for the ClockWise To-Do List"""

    def __init__(self):
        """Initializes the ClockWiseApp window, loads images, and sets up the UI components."""
        super().__init__()

        #Set the window title and size
        self.title("ClockWise - To-Do List")  #Application Title
        self.geometry("450x600")  #Sets Window size
        self.configure(bg="#e3f2fd")  #Set background color

        self.tasks = []  #List to store task 

        #Get the directory where the script is located
        scriptDir = os.path.dirname(os.path.abspath(__file__))  #Get script path

        #Load images using a full path
        logoPath = os.path.join(scriptDir, "logo.gif")  #Path for logo image
        addIconPath = os.path.join(scriptDir, "add_icon.gif")  #Path for add task icon

        #Resize images using subsample to reduce size
        self.logoImage = tk.PhotoImage(file=logoPath).subsample(15, 15)  #Load and resize logo
        self.addIcon = tk.PhotoImage(file=addIconPath).subsample(15, 15)  #Load and resize icon

        #Display logo at the top of the app
        self.logoLabel = tk.Label(self, image=self.logoImage, bg="#f4f4f4")
        self.logoLabel.pack(pady=10)  

        #Create the label for task list section
        self.label = tk.Label(self, text="Your Tasks:", font=("Arial", 16, "bold"), bg="#f4f4f4")
        self.label.pack(pady=5)

        #Listbox to display tasks
        self.taskListbox = tk.Listbox(self, width=50, height=10, font=("Arial", 12))
        self.taskListbox.pack(pady=10)

        #Buttons to interact with the task list
        self.addButton = tk.Button(self, text=" ➕Add Task", image=self.addIcon, compound="left",command=self.addTaskWindow, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
        self.addButton.pack(pady=5)

        self.completeButton = tk.Button(self, text="✔Complete Task", command=self.completeTask,bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
        self.completeButton.pack(pady=5)

        self.remindersButton = tk.Button(self, text="⏰Show Reminders", command=self.showReminders,bg="#FF9800", fg="white", font=("Arial", 12, "bold"))
        self.remindersButton.pack(pady=5)

        self.exitButton = tk.Button(self, text="Exit", command=self.quit, bg="#E91E63", fg="white", font=("Arial", 12, "bold"))
        self.exitButton.pack(pady=10)

    def addTaskWindow(self):
        """Opens the Add Task window where users can add a task."""
        addTaskWindow = AddTaskWindow(self)  
        self.wait_window(addTaskWindow)  #Pause until the window is closed

    def addTask(self, taskName, dueDate, category):
        """Adds a new task to the list"""
        task = {"name": taskName, "dueDate": dueDate, "category": category}  #Create task dictionary
        self.tasks.append(task)  #Add task to the list
        self.updateTaskListbox()  #Refresh task list box

    def completeTask(self):
        """Removes a task from the list box"""
        try:
            selectedTaskIndex = self.taskListbox.curselection()[0]  #Get task currently selected in list box
            completedTask = self.tasks.pop(selectedTaskIndex)  #Remove the task from the list
            self.updateTaskListbox()  #Refresh list box
            messagebox.showinfo("Task Completed", f"Task '{completedTask['name']}' is marked as completed!") #Informs user task has been completed in message box
        except IndexError:
            messagebox.showwarning("No Task Selected", "Please select a task to mark as completed.") #Displays error in message box when no task is selected 

    def showReminders(self):
        """Displays a reminder for tasks that are due today."""
        today = datetime.today().strftime("%Y-%m-%d")  #Get today's date
        reminders = [task for task in self.tasks if task["dueDate"] == today]  #Find tasks due today
        if reminders:
            reminderText = "\n".join([task["name"] for task in reminders])  #Present task due today in message box
            messagebox.showinfo("Today's Reminders", reminderText)
        else:
            messagebox.showinfo("No Reminders", "You have no tasks due today.") 

    def updateTaskListbox(self):
        """Updates the task list display in the listbox."""
        self.taskListbox.delete(0, tk.END)  #Clear existing listbox items
        for task in self.tasks:
            self.taskListbox.insert(tk.END, f"{task['name']} - {task['category']} - Due: {task['dueDate']}")  #Adds updated tasks


#Second Window Class for Adding Tasks
class AddTaskWindow(tk.Toplevel):
    """The Add Task window allows users to input a new task with a name, due date, and category"""
    def __init__(self, parent):
        """Initializes the AddTaskWindow."""
        super().__init__(parent)
        self.title("Add New Task") #Second window title
        self.geometry("350x300") #Sets window size
        self.configure(bg="#f4f4f4") 

        #Input fields for task details
        self.taskNameLabel = tk.Label(self, text="Task Name:", bg="#f4f4f4")
        self.taskNameLabel.pack(pady=5)
        self.taskNameEntry = tk.Entry(self)
        self.taskNameEntry.pack(pady=5)

        self.dueDateLabel = tk.Label(self, text="Due Date (YYYY-MM-DD):", bg="#f4f4f4")
        self.dueDateLabel.pack(pady=5)
        self.dueDateEntry = tk.Entry(self)
        self.dueDateEntry.pack(pady=5)

        self.categoryLabel = tk.Label(self, text="Category (Work/Personal):", bg="#f4f4f4")
        self.categoryLabel.pack(pady=5)
        self.categoryEntry = tk.Entry(self)
        self.categoryEntry.pack(pady=5)

        #Save and Cancel buttons
        self.saveButton = tk.Button(self, text="Save Task", command=self.saveTask, bg="#4CAF50", fg="white")
        self.saveButton.pack(pady=10)

        self.cancelButton = tk.Button(self, text="Cancel", command=self.destroy, bg="#E91E63", fg="white")
        self.cancelButton.pack(pady=5)

    def saveTask(self):
        """Saves the task and adds it to the main task list."""
        taskName = self.taskNameEntry.get().strip()
        dueDate = self.dueDateEntry.get().strip()
        category = self.categoryEntry.get().strip()

        if not taskName or not dueDate or not category: #Validates to ensure all fields are entered
            messagebox.showerror("Input Error", "All fields are required.")
        elif not validateDate(dueDate): #Validates the date format
            messagebox.showerror("Date Error", "Please enter a valid date in the format YYYY-MM-DD.")
        else:
            self.master.addTask(taskName, dueDate, category)  #Add task to main list
            self.destroy()  #Close Add Task window

if __name__ == "__main__":
    app = ClockWiseApp()  
    app.mainloop()