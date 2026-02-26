from task_manager import TaskManager

def print_menu():
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")

def main():

    task_manager = TaskManager()

    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice: ")
            match choice:
                case "1":
                    description = input("Enter task description: ")
                    task_manager.add_task(description)
                case "2":
                    task_manager.list_tasks()
                case "3":
                    task_id = int(input("Enter task ID to complete: "))
                    task_manager.complete_task(task_id)
                case "4":
                    task_id = int(input("Enter task ID to remove: "))
                    task_manager.remove_task(task_id)
                case "5":
                    print("Exiting the application.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
