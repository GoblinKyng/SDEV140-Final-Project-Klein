"""
Author: Mark Klein
Date Written: 02/22/2025
"Insert Description of final project here" 

"""

import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from datetime import datetime

#Main Window Class for ClockWise
class ClockWiseApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ClockWise") #Set title
        self.geometry("400x400") #Set Window Size
        self.Tasks = [] #Create empty list for task to go

        self.Label = tk.Label(self, text="To-Do List", font=("Arial", 14)) #Create label to identify to-do list
        self.Label.pack(pady=20) #Padded

        #Create box to display tasks
        self.TaskListbox = tk.Listbox(self, width=40, height=10) #Set box size
        self.TaskListbox.pack(pady=10) #Padded

        #Buttons to manage tasks
        self.AddButton = tk.Button(self, text="Add Task") #Created button for adding task
        self.AddButton.pack(pady=5) #Padded

        self.CompleteButton = tk.Button(self, text="Complete Task") #Created button for completing task
        self.CompleteButton.pack(pady=5) #Padded

        self.RemindersButton = tk.Button(self, text="Show Reminders") #Created button to show whats due today
        self.RemindersButton.pack(pady=5) #Padded

        self.ExitButton = tk.Button(self, text="Exit", command=self.quit) #Created button to quit the application
        self.ExitButton.pack(pady=10) #Padded

        """
        Buttons added for moving task up or down the list? 

        perhaps all task can be sorted by due date only?"""


#Second Window Class for adding tasks
class AddTaskWindow(tk.Toplevel): #Ensured new window goes over old window
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Add New Task") #Set Title
        self.geometry("350x350") #Set Window Size

        """
        Entry field for new task
        Entry field for selecting due date, radial?, calendar picker?
        How to categorize task? Color code? selection box? type in field?
        Save task Button
        Cancel task Button
        """






if __name__ == "__main__":
    app = ClockWiseApp()
    app.mainloop()