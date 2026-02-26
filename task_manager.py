
class Task:

  def __init__(self, id, description, completed=False):
    self.id = id
    self.description = description
    self.completed = completed

  def __str__(self):
    status = "Completed" if self.completed else "Pending"
    return f"Task ID: {self.id}, Description: {self.description}, Status: {status}"


class TaskManager:

  def __init__(self):
    self._tasks = []
    self._next_id = 1

  def add_task(self, description):
    task = Task(self._next_id, description)
    self._tasks.append(task)
    self._next_id += 1
    print(f"Added task: {task}")

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




