"""
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
"""

class Reminder:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        self.name = name
        pass

    def remind_me_to(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to the self object
        self.task = task
        pass

    def remind(self):
        # Returns:
        #   A string reminding the user to do the task
        # Side-effects:
        #   Throws an exception if no task is set
        if self.task == "":
            raise Exception("No task set.")
        else:
            return f"{self.task}, {self.name}!"
    

reminder = Reminder("Kay")

print(reminder.remind_me_to("Walk the dog."))
print(reminder.task)
print(reminder.remind())