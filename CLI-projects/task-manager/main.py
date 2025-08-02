import os 
from typing import Any

TASK_FILE = "task.txt"
CURRENT_DIR = os.getcwd()
file_path = os.path.join(CURRENT_DIR,TASK_FILE)


def load_task()->list:
    tasks  = []
    try:
        if (os.path.exists(file_path)):
            with open(file_path,'r',encoding='utf-8') as file:
                for line in file:
                    text,status = line.strip().rsplit("||",1)
                    tasks.append({"text":text,'done': status == "done"})
        
        else:
            print(f"File not found at: {file_path}")
 
    except Exception as e:
        print(f"Error loading tasks: {e}") 
    
    return tasks


def save_tasks(tasks:list[dict[str,Any]])->None:
    try:
        with open(file_path,'w',encoding='utf-8') as file:
            for task in tasks:
                status = "done" if task['done'] else "not_done"
                text = task['text']
                file.write(f"{text}||{status}\n")
    except Exception as e:
        print(f"Error saving tasks: {e}")


def display_tasks(tasks:list[dict[str,Any]])->None:
    if not tasks:
        print("No tasks available.")
        return 
    else:
        print("\n--- Your Tasks ---")
        for i , task in enumerate(tasks):
            checkbox = "✅" if task['done']  else ""
            print(f"{i+1}. [{checkbox}] {task['text']}")

    print()

def task_manager() -> None :
    tasks = load_task()

    while True:

        print("""
----- Task Manager -----
1. Add Task
2. Show Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
""")

        choice = input("Enter a number (1-5): ")
        match choice:
            case "1":
                task_text = input("Enter a task: ").strip()
                if task_text: 
                    tasks.append({"text":task_text,"done":False})
                    save_tasks(tasks=tasks)
                    print(f"Task '{task_text}' added successfully.\n")
                else:
                    print("Task cannot be empty!\n")
            case "2":
                display_tasks(tasks=tasks)
            case "3":
                try:
                    task_id = int(input("Enter task ID to mark as completed: ").strip())
                    if 1 <= task_id <= len(tasks):
                        tasks[task_id-1]['done'] = True
                        save_tasks(tasks=tasks)
                        print(f"Task #{task_id} marked as completed.\n")
                    else:
                        print("Invalid task ID.\n")
                except ValueError:
                    print("Please enter a valid number for task ID.\n")
            case "4":
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    if 1 <= task_id <= len(tasks):
                        removed_task=tasks.pop(task_id-1)
                        save_tasks(tasks=tasks)
                        print(f"Task '{removed_task['text']}' deleted successfully.\n")
                    else:
                        print("Invalid task ID.\n")
                except ValueError:
                    print("Please enter a valid number for task ID.\n")
            case "5":
                print("Exiting Task Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.\n")
                


    


task_manager()