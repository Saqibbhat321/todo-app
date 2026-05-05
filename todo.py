import json
from datetime import datetime

FILE = "tasks.json"
tasks = []
PRIORITY_LABELS = {1: "High", 2: "Medium", 3: "Low"}


def load_tasks():
    global tasks
    try:
        with open(FILE, "r") as f:
            tasks = json.load(f)
        print(f"Loaded {len(tasks)} task(s).")
    except FileNotFoundError:
        tasks = []


def save_tasks():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def get_priority():
    while True:
        print("Priority: 1=High  2=Medium  3=Low")
        choice = input("Choose (1/2/3): ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        print("Enter 1, 2, or 3.")


def get_valid_date():
    while True:
        raw = input("Due date (YYYY-MM-DD) or leave blank: ")
        if raw == "":
            return "No due date"
        try:
            datetime.strptime(raw, "%Y-%m-%d")
            return raw
        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


def add_task():
    name = input("Task name: ")
    priority = get_priority()
    due = get_valid_date()
    task = {"name": name, "done": False, "priority": priority, "due": due}
    tasks.append(task)
    save_tasks()
    print(f"Added: {name}")


def show_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    if not task_list:
        print("No tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(task_list, 1):
        status = "[x]" if task["done"] else "[ ]"
        label = PRIORITY_LABELS[task["priority"]]
        print(f"{i}. {status} [{label}] {task['name']} — {task['due']}")


def show_sorted():
    sorted_tasks = sorted(tasks, key=lambda t: t["priority"])
    show_tasks(sorted_tasks)


def mark_done(number):
    if 1 <= number <= len(tasks):
        tasks[number - 1]["done"] = True
        save_tasks()
        print(f"Marked done: {tasks[number - 1]['name']}")
    else:
        print("Invalid number.")


def delete_task(number):
    if 1 <= number <= len(tasks):
        removed = tasks.pop(number - 1)
        save_tasks()
        print(f"Deleted: {removed['name']}")
    else:
        print("Invalid number.")


def main():
    load_tasks()
    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Show tasks by priority")
        print("4. Mark task done")
        print("5. Delete task")
        print("6. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_sorted()
        elif choice == "4":
            show_tasks()
            num = int(input("Task number to mark done: "))
            mark_done(num)
        elif choice == "5":
            show_tasks()
            num = int(input("Task number to delete: "))
            delete_task(num)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()