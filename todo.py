tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Added {task}")

def show_task():
    if not tasks:
        print("no tasks yet")
    else:
         print("\n ------ Your Tasks------")
         for i, task in enumerate(tasks,1):
             print(f"{i}. {task}")


def delete_task(number):
    if 1 <=number <= len(tasks):
        removed = tasks.pop(number-1)
        print(f"Deleted",{removed})
    else:
        print("Invalid Task number.")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Show Task")
        print("3. Delete Task")
        print("4. Quit")


        choice= input("Choose an Option\n")

        if choice == "1":
            task = input("Enter Task: ")
            add_task(task)
        elif choice =="2":
            show_task()
        elif choice == "3":
            show_task()
            num = int(input("Task number to be delete:  "))
            delete_task(num)
        elif choice == "4":
            print("Have a Nice Weekend")
        else:
            print("Invalid option Selected")

if __name__ == "__main__":
    main()