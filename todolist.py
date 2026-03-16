def todolist_using_list():    
    work_list = []
    def menu():
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Exit")
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1: 
            task = input("Enter the task: ")
            work_list.append(task)
            print("Task added.")
        elif choice == 2:
            if not work_list:
                print("No tasks in the list.")
            else:
                print("Tasks:")
                for index, task in enumerate(work_list):
                    print(f"{index + 1}. {task}")
        elif choice == 3:
            if not work_list:
                print("No tasks to remove.")
            else:
                print("Tasks:")
                for index, task in enumerate(work_list):
                    print(f"{index + 1}. {task}")
                task_number = int(input("Enter the task number to remove: "))
                if 1 <= task_number <= len(work_list):
                    removed_task = work_list.pop(task_number - 1)
                    print(f"Task '{removed_task}' removed.")
                else:
                    print("Invalid task number.")
        elif choice == 4:
            print("Exiting the program.")
            break
import os
from pathlib import Path

def view_task(textfile):
    with open(textfile, 'r') as file:
        print("-"*45)
        print("Recent Task")
        for index, line in enumerate(file, 1):
            print(str(index)+". " + line,end="")

def display_menu():
    print("\n"+"-"*45)
    print("1. Add a task 2. View tasks 3. Remove a task 4. Mark complete task 5. Exit")
    print("-"*45)
    
def todolist_using_file():
    textfile = "todolist.txt"
    file_path = Path("todolist.txt")
    print("-"*45)
    print("\t\tWelcome Todo List")
    
    while True:
        try:
            display_menu()
            choice = int(input("Enter a choice : "))   
            if choice == 1:
                task = input("Enter a task : ")
                with open(textfile, 'a+') as file:
                    if file_path.stat().st_size != 0:
                        file.write("\n"+task)
                    else:
                        file.write(task)
                    print("Task added successfully!")    
            elif choice == 2:
                if file_path.stat().st_size != 0:
                    view_task(textfile)
                else:
                    print("\nNo Task Added")
            elif choice == 3:
                while True:
                    with open(textfile, 'r+') as file:
                        lines = file.readlines()
                        view_task(textfile)
                        index = input("\nEnter line number or 'q' for exit: ")
                        if str(index) == 'q':
                            break
                        index = int(index)-1
                        if index >= len(lines) or index < 0:
                            continue
                        else:
                            line_to_delete = lines[index]
                            file.seek(0)
                            for line in lines:
                                if line_to_delete not in line:
                                    file.write(line)
                            file.truncate()
                            print("Taks deleted successfully!")
            elif choice == 4:
                index = input("Enter line number or 'q' for exit: ")
                with open(textfile, 'r') as file:
                    lines = file.readlines()
                text = str(lines[int(index)-1]).strip('\n')
                lines[int(index)-1] =  text + " @Task Completed@"
                if "@Task Completed@" in text:
                    print("Already Marked!")
                else:
                    with open(textfile, 'w') as file:
                        for line in lines:
                            file.write(line)
                    print("Marked successfully")
            else:
                print("Exiting....!")
                break
        except(ValueError):
            print("Please enter number only", ValueError)

if __name__ == "__main__":
      todolist_using_file()
    # textfile = "demo.txt"
    
    # with open(textfile,'a') as file:
    #     while True:
    #         task = input("Please enter the task.")
    #         if task == 'q':    
    #             break
    #         file.write(task)
            
    # with open(textfile) as file:
    #     print(file.readlines())
