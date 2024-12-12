'''Task tracker is a project used to track and manage your tasks. In this task, you will build a simple command line interface (CLI) to track what you need todo, what you have done, and what you are currently working on. This project will help you practice your programming skills, including working with the filesystem, handling user inputs, and building a simple CLI application.

Requirements
The application should run from the command line, accept user actions and inputs as arguments, and store the tasks in a JSON file. The user should be able to:

Add, Update, and Delete tasks
Mark a task as in progress or done
List all tasks
List all tasks that are done
List all tasks that are not done
List all tasks that are in progress
Here are some constraints to guide the implementation:

You can use any programming language to build this project.
Use positional arguments in command line to accept user inputs.
Use a JSON file to store the tasks in the current directory.
The JSON file should be created if it does not exist.
Use the native file system module of your programming language to interact with the JSON file.
Do not use any external libraries or frameworks to build this project.
Ensure to handle errors and edge cases gracefully.'''

import json
import os
import sys
TASKS_FILE = "tasks.json" #file name where tasks are stored

def read_tasks():
    if not os.path.exists(TASKS_FILE): # if file doesn't exist, create a new file
        with open(TASKS_FILE, 'w') as file:
            json.dump([], file)
        return []
    with open(TASKS_FILE, 'r') as file:
        return json.load(file)
    
def write_task(tasks): # to write tasks or update json file so that the changes reflect in the json file
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(title): # add task with the title provided, the status will be todo by default
    tasks = read_tasks() 
    task_id = max([task['id'] for task in tasks], default = 0) + 1 # id will be max of all the task ids + 1, i.e the next id
    tasks.append({"id": task_id, "title": title, "status": "todo"}) # add the new task to the dictionary
    write_task(tasks)
    print(f"task added successfully with task_id{task_id}")

def update_task(task_id, title):
    tasks = read_tasks()
    for task in tasks:
        if task['id'] == task_id: # find task id to update the title of the task
            task['title'] = title # modifies the title of the task
            write_task(tasks) # write back the task to the file
            print(f"task {task_id} updated successfully")
            return
    print(f"task id {task_id} not found") # if task id is not found


def delete_task(task_id):
    tasks = read_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    write_task(tasks)
    print(f"task{task_id} deleted successfully")

    

def mark_task(task_id, status):
    tasks = read_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            write_task(tasks)
            print(f"Task {task_id} marked as {status}.")
            return
    print(f"Task with ID {task_id} not found.")
    
def list_tasks(filter = None):
    tasks = read_tasks()
    if filter == "Done":
        tasks = [task for task in tasks if task['status'] == "Done"]
    elif filter == "todo":
        tasks = [task for task in tasks if task['status'] == "todo" ]
    elif filter == "In Progress":
        tasks = [task for task in tasks if task['status'] == "In Progress" ]
    for task in tasks:
        print(f"ID: {task['id']}, Title: {task['title']}, Status: {task['status']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python task_tracker.py <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        title = "".join(sys.argv[2])
        add_task(title)

    elif command == "delete":
        task_id = int(sys.argv[2])
        delete_task(task_id)

    elif command == "update":
        task_id = int(sys.argv[2])
        title = "".join(sys.argv[3:])
        update_task(task_id, title)
    
    elif command == "mark in progress":
        task_id = int(sys.argv[2])
        mark_task(task_id, status = "InProgress")
    
    elif command == "mark done":
        task_id = int(sys.argv[2])
        mark_task(task_id, status = "Done")

    elif command == "list":
        filter = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else None
        list_tasks(filter)

    else: 
        print("unknown command")
    



    

