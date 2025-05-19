tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added ")
    return

def view_tasks():
    if not tasks:
        print("No tasks")
    else:
        for task in tasks:
            print(task)
            return
def remove_task(index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        print(f"Task '{removed_task}' removed ")
    else:
        print("Invalid task index.")
        return
while True:
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task ")
        add_task(task)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        index = int(input("Enter task index to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice.")