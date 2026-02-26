def print_menu():
    print("\nTask Manager Application")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Exit")


def main():

  from task_manager import TaskManager
  task_manager = TaskManager()

  while True:
    print_menu()
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


if __name__ == "__main__":
    main()
