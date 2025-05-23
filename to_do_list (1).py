# -*- coding: utf-8 -*-
"""to do list

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1W5X_zhimZOhqPHVFNi_GzHQiAQYK6ByP
"""

class Task:

  def __init__(self):
    self.tasks = []


#Background of the To-Do-list
# add task
  def add_task(self, task, deadline, completeness):
    self.tasks.append({"task": task, "deadline": deadline, "completeness": completeness})
    print(" -----Task added successfully----- ")

#remove task
  def remove_task(self, task):
    for t in self.tasks:
      if t["task"] == task:
        self.tasks.remove(t)
        print(" -----Task removed successfully----- ")
        return
    print(" -----Task not found----- ")

# completeness
  def update_completeness(self, task, new_completeness):
    for t in self.tasks:
      if t["task"] == task:
       t["completeness"] = new_completeness
       if t["completeness"] == "completed" :
            print(" -----Task marked as completed----- ")
            return
       elif t["completeness"] == "pending":
            print(" -----Task marked as pending----- ")
            return
       elif t["completeness"] not in "completed" and "pending":
            print(" -----Invalid completeness----- ")
            return
    print(" -----Task not found----- ")

#view task
  def view_tasks(self):
    for i, task in enumerate(self.tasks):
      print(f"{i+1}. {task['task']} - {task['deadline']} - {task['completeness']}")
    if not self.tasks:
      print(" -----No tasks found----- ")
      return

#clear task
  def clear_task(self):
    self.tasks.clear()
    print(" -----All tasks cleared successfully----- ")


#update deadline
  def update_deadline(self, task, new_deadline, completeness):
    for t in self.tasks:
      if t["task"] == task:
        t["deadline"] = new_deadline
        t["completeness"] = completeness
        print(" -----Deadline updated successfully----- ")
        return
    print(" -----Task not found----- ")





todolist= Task()

# user interface

print("Welcome to your to do list")
print("\n------To-Do-List------\n")
print("1. Add Task")
print("2. Remove Task")
print("3. View tasks")
print("4. Update Deadline")
print("5. Update Completeness")
print("6. Clear all tasks")
print("7. Exit")
print()

while True:
  try:
    welcome= int(input("Enter your choice : "))
    print()
  except ValueError:
    print("Enter valid index number between 1 and 6")
    print()
    continue


  if welcome==1:
    print(" -----Add Task------ ")
    task= input("Enter a new task : ")
    try:
       deadline= int(input("Enter the deadline for the task (DD/MM/YYYY) : "))
    except ValueError:
      print("Enter valid date")
      print()
      continue
    completeness= input("Enter whether the task is completed / pending : ")
    todolist.add_task(task, deadline, completeness)
    print()


  elif welcome==2:
    print(" -----Remove Task------ ")
    task= input("Enter the task to remove :  ")
    todolist.remove_task(task)
    print()


  elif welcome==3:
    print(" -----View tasks------ ")
    todolist.view_tasks()
    print()


  elif welcome==4:
    print(" -----Update Deadline------ ")
    task= input("Enter the task to update the deadline for  :  ")
    if task not in [t["task"] for t in todolist.tasks]:
      print(" -----Task not found----- ")
      print()

    new_deadline= int(input("Enter the new deadline for the task :  "))
    completeness= input("Enter whether the task is completed / pending : ")
    todolist.update_deadline(task, new_deadline, completeness)
    print()


  elif welcome==5:
    print(" -----Update Completeness------ ")
    task= input("Enter the task to update the completeness for :  ")
    if task not in [t["task"] for t in todolist.tasks]:
      print(" -----Task not found----- ")
      print()
      continue
    completeness= input("Enter whether the task is completed / pending : ")
    todolist.update_completeness(task, completeness)
    print()

  elif welcome==6:
    print(" -----Clear all tasks------ ")
    todolist.clear_task()
    print()


  elif welcome==7:
    print(" -----Exit------ ")
    print(" -----Thank you for using our to-do-list----- ")
    print()

    with open("tasks.txt", "w") as f:
      for task in todolist.tasks:
        taskstr = f"{task['task']}, {task['deadline']}, {task['completeness']}"
        f.write(taskstr)
    break

  else:
   print("Enter valid index")
   print()

