tasks = []

def add_task():
    title = input("Enter task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{index}. {task['title']} - {status}")
    print()

def mark_task_completed():
    view_tasks()
    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to mark as completed: "))
        tasks[task_number - 1]["completed"] = True
        print("Task marked as completed!\n")
    except (IndexError, ValueError):
        print("Invalid task number.\n")

def main():
    while True:
        print("TO-DO LIST APPLICATION")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_completed()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")

main()