from pydantic import BaseModel
from datetime import datetime
import json

menu_options = "(1) Add task\n(2) List tasks\n(3) Mark task done\n(4) Delete task\n(5) Filter by status\n(6) Statistics\n(7) Quit"

class Task(BaseModel):
    id: int
    title: str
    description: str = ""
    status: str
    priority: str
    created_at: datetime = datetime.now()
    due_date: str = ""

task_list = []

def load_tasks():
    try:
        with open("phase-0-python/week-2/output-files/tasks.json", "r") as f:
            tasks = json.load(f)
            for task in tasks:
                task_list.append(Task(**task))
    except FileNotFoundError:
        print("file not found")

def save_tasks():
    with open("phase-0-python/week-2/output-files/tasks.json", "w") as f:
        json_tasks_list = []
        for task in task_list:
            json_tasks_list.append(task.model_dump(mode="json"))
        json.dump(json_tasks_list, f, indent = 2)

def add_task():
    title = ""
    while not title:
        title = input("Enter task name: ")

    description = input("Enter description: ")
    
    priority = ""
    while not priority or priority.lower() not in ["low", "medium", "high"]:
         priority = input("Enter priority:(low/medium/high) ")

    due_date = input("Enter Due date: ")
    
    task_id = len(task_list) + 1
    task = Task(id = task_id, title = title, description = description, status = "pending", priority= priority, due_date = due_date)
    task_list.append(task)

def list_tasks():
    if not task_list:
        print("No tasks!")
        return
    for task in task_list:
        print(f"{task.id}. {task.title}, Status: {task.status}, Priority: {task.priority}\n")

def mark_task_done(name):
    for index, task in enumerate(task_list):
        if task.title.lower() == name.lower():
            task_list[index].status = "done"
            print(f"Task: {task.title} marked as done")
            break

def delete_task(name):
    for index, task in enumerate(task_list):
        if task.title.lower() == name.lower():
            print(f"Task: {task.title} Deleted")
            task_list.remove(task)
            break

def filter_by_status(status):
    if status in ["pending", "done", "in_progress"]:
        for task in task_list:
            if task.status.lower() == status.lower():
                print(f"{task.id}. {task.title}, Status: {task.status}, Priority: {task.priority}\n")
    else:
        print("Please select valid status (pending/done/in_progress")

def show_statistics():
    print("Statistics:")
    print(f"Total tasks: {len(task_list)}")
    
    done_task_count = 0
    low_count = 0
    medium_count = 0
    high_count = 0

    for task in task_list:
        if task.status.lower() == "done":
            done_task_count += 1
        
        if task.priority.lower() == "low":
            low_count += 1
        elif task.priority.lower() == "medium":
            medium_count += 1
        elif task.priority.lower() == "high":
            high_count += 1
        
    if len(task_list) > 0:
        done_percentage = (done_task_count * 100 ) / len(task_list)
        print(f"Done percentage: {done_percentage}%")


    print(f"Low: {low_count}")
    print(f"Medium: {medium_count}")
    print(f"High: {high_count}")

load_tasks()
while True:
    print(f"{menu_options}")
    choice = int(input("Choose: "))

    if choice == 7:
        save_tasks()
        break
    elif choice == 1:
        add_task()
    elif choice == 2:
        list_tasks()
    elif choice == 3:
        task_name = input("Enter task name:")
        mark_task_done(task_name)
    elif choice == 4:
        task_name = input("Enter task name to delete:")
        delete_task(task_name)
    elif choice == 5:
        status = input("Enter the status to filter:")
        filter_by_status(status)
    elif choice == 6:
        show_statistics()
    else:
        print("Invalid choice")