import json


class Task:

  def __init__(self, id, description, completed=False):
    self.id = id
    self.description = description
    self.completed = completed

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"Task ID: {self.id}, Description: {self.description}, Status: {status}"


class TaskManager:
  FILENAME = "tasks.json"

  def __init__(self):
    self._tasks = []
    self._next_id = 1
    self.load_tasks(self.FILENAME)

  def add_task(self, description):
    task = Task(self._next_id, description)
    self._tasks.append(task)
    self._next_id += 1
    print(f"Added task: {task}")
    self.save_tasks()

  def list_tasks(self):
    if not self._tasks:
      print("No tasks available.")
      return
    for task in self._tasks:
      print(task)

  def complete_task(self, task_id):
    for task in self._tasks:
      if task.id == task_id:
        task.completed = True
        print(f"Completed task: {task}")
        return
    print(f"Task with ID {task_id} not found.")

  def remove_task(self, task_id):
    for task in self._tasks:
      if task.id == task_id:
        self._tasks.remove(task)
        print(f"Removed task: {task}")
        return
    print(f"Task with ID {task_id} not found.")
    
  def load_tasks(self, filename):
    try:
      with open(self.FILENAME, 'r') as file:
        data = json.load(file)
        self._tasks = [Task(**task_data) for task_data in data]
        self._next_id = max(task.id for task in self._tasks) + 1 if self._tasks else 1
        print(f"Loaded {len(self._tasks)} tasks from {filename}.")
    except FileNotFoundError:
      print(f"No existing task file found. Starting with an empty task list.")
    except json.JSONDecodeError:
      print(f"Error decoding JSON from {filename}. Starting with an empty task list.")

  def save_tasks(self):
    with open(self.FILENAME, 'w') as file:
      json.dump([task.__dict__ for task in self._tasks], file, indent=2)
      print(f"Saved {len(self._tasks)} tasks to {self.FILENAME}.")




