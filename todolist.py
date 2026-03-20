import os
from pathlib import Path
import json

class todoWithList:
    def __init__(self):
        self.Task_list = []
    
    def display_menu(self):
        print("To-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
    
    def create_task(self):
        task = input("Enter the task: ")
        self.Task_list.append(task)
        print("Task added.")
    
    def view_task(self):
        print("-"*24)
        if not self.Task_list:
            print("Empty Task.")
            return True
        print("Tasks list:")
        for index, task in enumerate(self.Task_list):
            print(f"{index + 1}. {task}")
        
    def remove_task(self):
        if self.view_task():
            return
        number = int(input("Enter the task number: "))
        if 0 < number <= len(self.Task_list):
            removed_task = self.Task_list.pop(number - 1)
            print(f"\nTask removed.")
        else:
            print("\nInvalid number.")
    
    def todolist_App(self):    
        while True:
            print("-"*24)
            self.display_menu()
            try:
                choice = int(input("Enter your choice (1-4): "))
                if choice == 1: 
                    self.create_task()
                elif choice == 2:
                    self.view_task()
                elif choice == 3:
                    self.remove_task()
                elif choice == 4:
                    print("Exiting the program...\n")
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Enter only number. Try Again!!!")

class todoWithFile:
    def __init__(self):
        self.file_path = Path("todolist.txt")
        self.textfile = "todolist.txt"

    def view_task(self):
        if self.file_path.stat().st_size == 0:
            print("\nEmpty Task")
            return
        with open(self.textfile, 'r') as file:
            print("-"*45)
            print("Recent Task List:")
            for number, line in enumerate(file):
                print(f"{number+1}. {line}",end="")

    def display_menu(self):
        print("\n"+"-"*45)
        print("1. Add a task 2. View tasks 3. Remove a task 4. Mark complete task 5. Exit")
        print("-"*45)
    
    def create_task(self):
        task = input("Enter a task : ")
        with open(self.textfile, 'a+') as file:
            if self.file_path.stat().st_size == 0:
                file.write(task)
            file.write("\n"+task)
            print("Task added successfully!")
    
    def remove_task(self):
        while True:
            self.view_task()
            with open(self.textfile, 'r+') as file:
                lines = file.readlines()
                file.seek(0)
                task_number = input("\nEnter line number or 'q' for exit: ")
                if task_number == 'q':
                    break
                number = int(task_number)
                if 0 < number <= len(lines):
                    line_to_delete = lines[number-1]
                    for line in lines:
                        if line_to_delete not in line:
                            file.write(line)
                    file.truncate()
                    print("Taks deleted successfully!")
                else:
                    print("Invalid line number")

    def mark_complete(self):
        while True:
            self.view_task()
            print("\n"+"-"*24)
            choice = input("Enter line number or 'q' for exit: ")
            if choice == 'q':
                break
            task_number = int(choice)
            with open(self.textfile, 'r') as file:
                lines = file.readlines()
                if "[Completed]" in lines[task_number-1]:
                    print("Already Marked!")
                else:
                    text = str(lines[task_number-1]).strip('\n')
                    if task_number == len(lines):
                        lines[task_number-1] =  text + " [Completed]"
                    else:
                        lines[task_number-1] =  text + " [Completed]\n"
                    with open(self.textfile, 'w') as file:
                        for line in lines:
                            file.write(line)
                        print("Marked successfully")

    def todo_App(self):
        print("-"*45)
        print("\t\tWelcome Todo List")
        while True:
            self.display_menu()
            try:
                choice = int(input("Enter a choice : "))   
                if choice == 1:
                    self.create_task()
                elif choice == 2:
                    self.view_task()
                elif choice == 3:
                    self.remove_task()    
                elif choice == 4:
                    self.mark_complete()
                else:
                    print("Exiting....!")
                    break
            except ValueError:
                print("Please Enter number only")

class todoWithJson:  

    def __init__(self):
        self.json_file = "todolist.json"

    def load_tasks(self):
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except:
            return {"Task": []}
        
    def save_task(self,tasks):
        try:
            with open(self.json_file, 'w') as file:
                json.dump(tasks, file)
        except:
            print("Faild to save.")

    def create_task(self, tasks):
        title = input("Enter the title: ")
        if title:
            tasks['Tasks'].append({'Title': title, "Complete": False})
            self.save_task(tasks)
            print ("Task added.")
        else:
            print("Task can't be empty")

    def delete_task(self, tasks):
        task_list = tasks['Tasks']
        number = int(input("Enter the line no: "))
        if number > 0 and number <= len(task_list) :
            tasks['Tasks'].pop(number-1)
            self.save_task(tasks)
            print("Task delete successfully.")
        else:
            print("Invalid Task number.")

    def mark_complete(self, tasks):
        task_list = tasks['Tasks']
        number = int(input("Enter the line no: "))
        if number > 0 and number <= len(task_list) :
            if tasks['Tasks'][number-1]['Complete']:
                print("-> Task already completed.")
                return
            tasks['Tasks'][number-1]['Complete'] = True
            self.save_task(tasks)
            print("-> Task marked as complete.")
        else:
            print("Invalid Task number.")

    def show_task(self, tasks):
        task_list = tasks['Tasks']
        if len(task_list) == 0:
            print ("Your task is empty")
        else:
            print("\nYour TODO list tasks.")
            for number, task in enumerate(task_list):
                status = '[Completed]' if task['Complete'] else '[Pending]'
                print(f"{number+1}. {task['Title']} | {status}")
    def display_menu(self):
        print("\n"+"-"*45)
        print("1. Add a task 2. View tasks 3. Remove a task 4. Mark complete task 5. Exit")
        print("-"*45)

    def todoMainApp(self):
        tasks = self.load_tasks()
        while True:
            self.display_menu()
            choice = int(input("Enter your choice (1-5): "))
            if choice == 1:
                self.create_task(tasks)
            elif choice == 2:
                self.show_task(tasks)
            elif choice == 3:
                self.delete_task(tasks)
            elif choice == 4:
                self.mark_complete(tasks)
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please Try again!!!")
    
if __name__ == "__main__":
    todo_App = todoWithFile()
    todo_App.todo_App()
    # todo_App = todoWithList()
    # todo_App.todolist_App()

    # todoApp = todoWithJson()
    # todoApp.todolist_main()

   
