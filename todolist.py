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
