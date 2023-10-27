# Initialize an empty list to store tasks
tasks = []

# Function to display the current tasks
def show_tasks():
    if not tasks:
        print("No tasks in your to-do list.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Function to add a task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the list
def remove_task():
    show_tasks()
    if tasks:
        try:
            task_index = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_index < len(tasks):
                removed_task = tasks.pop(task_index)
                print(f"Task '{removed_task}' removed from your to-do list.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")

# Main loop to interact with the to-do list
while True:
    print("\nTo-Do List Menu:")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Quit")
    
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
