import json
import os
from datetime import datetime

file = "task.json"
# test push

def load():
    try:
        if os.path.exists(file):
            with open(file, "r") as f:
                return json.load(f)
        return []
    
    except json.JSONDecodeError:
        print("⚠ File corrupted. Starting fresh.")
        return []
    except Exception as e:
        print("Error loading file:", e)
        return []
        
def save(tasks):
    try:
        with open(file, "w") as f:
            json.dump(tasks, f, indent=4)
    except Exception as e:
        print("Error saving file:", e)
        
        
def add_task(tasks):
    try:
        title = input("Enter task title: ").strip()
        desc = input("Enter task description: ").strip()
        priority = input("Enter task priority (low, medium, high): ").strip().lower()
        deadline = input("Enter task deadline (YYYY-MM-DD): ").strip()

        if not title:
            print("Title cannot be empty!")
            return

        if priority not in ["low", "medium", "high"]:
            print("Invalid priority!")
            return

        # validate date
        datetime.strptime(deadline, "%Y-%m-%d")

        task = {
            "title": title,
            "desc": desc,
            "priority": priority,
            "deadline": deadline,
            "done": False
        }

        tasks.append(task)
        save(tasks)
        print("Task Added!")

    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD")
    except Exception as e:
        print("Error:", e)
    
def show(tasks):
    if not tasks:
        print("No tasks!")
        return

    for i, t in enumerate(tasks, 1):
        status = "COMPLETED" if t["done"] else "NOT COMPLETED"
        print(f"{i}. [{status}] {t['title']} ({t['priority']}) - {t['deadline']}")
        
        
        
def complete(tasks):
    try:
        show(tasks)
        i = int(input("Task number: ")) - 1

        if i < 0 or i >= len(tasks):
            print("Invalid task number!")
            return

        if tasks[i]["done"]:
            print("Task already done!")
            return

        tasks[i]["done"] = True
        save(tasks)
        print("Marked as done!")
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print("Error:", e)
    

def delete(tasks):
    try:
        show(tasks)
        i = int(input("Task number: ")) - 1

        if i < 0 or i >= len(tasks):
            print("Invalid task number!")
            return

        tasks.pop(i)
        save(tasks)
        print("Deleted!")
    except ValueError:
        print("Please enter a valid number!")
    except Exception as e:
        print("Error:", e)
        

def search(tasks):

    try:
        keyword = input("Search: ").lower()
        results = [t for t in tasks if keyword in t["title"].lower()]

        if not results:
            print("No matching tasks found.")
            return

        for t in results:
            print(t["title"], "-", t["deadline"])
    except Exception as e:
        print("Error:", e)

def filter_tasks(tasks):
    choice = input("1. view Completed tasks 2. View Pending Tasks: ")
    for t in tasks:
        if choice == "1" and t["done"]:
            print(t["title"])
        elif choice == "2" and not t["done"]:
            print(t["title"])

def main():
    tasks = load()

    while True:
        print("\n1.Add 2.Show 3.Done 4.Delete 5.Search 6.Filter 7.Exit")

        try:
            ch = input("Choice: ")

            if ch == "1": add_task(tasks)
            elif ch == "2": show(tasks)
            elif ch == "3": complete(tasks)
            elif ch == "4": delete(tasks)
            elif ch == "5": search(tasks)
            elif ch == "6": filter_tasks(tasks)
            elif ch == "7": break
            else:
                print("Invalid choice!")

        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
   main()
    
    
    