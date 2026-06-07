from database import initialize_database
from task_manager import TaskManager


def main():

    initialize_database()

    manager = TaskManager()

    while True:

        print("\n===== TASK MANAGER =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("0. Exit")

        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("Invalid input.")
            continue

        if choice == 1:

            title = input("Task Title: ")
            manager.add_task(title)

        elif choice == 2:

            manager.view_tasks()

        elif choice == 3:

            try:
                task_id = int(input("Task ID: "))
                manager.complete_task(task_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == 4:

            try:
                task_id = int(input("Task ID: "))
                manager.delete_task(task_id)
            except ValueError:
                print("Invalid ID.")

        elif choice == 0:
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()