import os
import json
from datetime import datetime

#!/usr/bin/env python3

class TodoList:
    def __init__(self):
        self.tasks = []
        self.file_path = os.path.expanduser("~/.todo_list.json")
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as file:
                    self.tasks = json.load(file)
            except:
                self.tasks = []

    def save_tasks(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, description, priority="medium"):
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "completed": False,
            "priority": priority
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task added: {description}")

    def list_tasks(self, show_completed=False):
        if not self.tasks:
            print("No tasks found.")
            return

        filtered_tasks = self.tasks
        if not show_completed:
            filtered_tasks = [task for task in self.tasks if not task["completed"]]
            
        if not filtered_tasks:
            print("No pending tasks.")
            return
            
        print("\nID | Priority | Status | Description")
        print("-" * 50)
        for task in filtered_tasks:
            status = "✓" if task["completed"] else "✗"
            print(f"{task['id']:2} | {task['priority']:8} | {status:6} | {task['description']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self.save_tasks()
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task with ID {task_id} not found.")

    def update_task(self, task_id, description=None, priority=None):
        for task in self.tasks:
            if task["id"] == task_id:
                if description:
                    task["description"] = description
                if priority:
                    task["priority"] = priority
                self.save_tasks()
                print(f"Task {task_id} updated.")
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                del self.tasks[i]
                # Reindex tasks
                for j in range(i, len(self.tasks)):
                    self.tasks[j]["id"] = j + 1
                self.save_tasks()
                print(f"Task {task_id} deleted.")
                return
        print(f"Task with ID {task_id} not found.")


def print_help():
    print("\nTodo List App Commands:")
    print("  add <description> [priority]    - Add a new task (priority: low, medium, high)")
    print("  list                           - List all pending tasks")
    print("  list all                       - List all tasks including completed")
    print("  complete <id>                  - Mark a task as completed")
    print("  update <id> <description>      - Update task description")
    print("  priority <id> <priority>       - Update task priority")
    print("  delete <id>                    - Delete a task")
    print("  help                           - Show this help message")
    print("  exit                           - Exit the application")


def main():
    todo = TodoList()
    print("Welcome to Command Line Todo List!")
    print("Type 'help' for available commands.")

    while True:
        command = input("\nEnter command: ").strip().split()
        
        if not command:
            continue
            
        action = command[0].lower()

        if action == "exit":
            print("Goodbye!")
            break
            
        elif action == "help":
            print_help()
            
        elif action == "add":
            if len(command) < 2:
                print("Please provide a task description.")
                continue
            description = " ".join(command[1:])
            if "priority:" in description.lower():
                parts = description.split("priority:", 1)
                description = parts[0].strip()
                priority = parts[1].strip()
                todo.add_task(description, priority)
            else:
                todo.add_task(description)
                
        elif action == "list":
            if len(command) > 1 and command[1].lower() == "all":
                todo.list_tasks(show_completed=True)
            else:
                todo.list_tasks()
                
        elif action == "complete":
            if len(command) != 2:
                print("Please provide a task ID.")
                continue
            try:
                task_id = int(command[1])
                todo.complete_task(task_id)
            except ValueError:
                print("Task ID must be a number.")
                
        elif action == "update":
            if len(command) < 3:
                print("Please provide a task ID and new description.")
                continue
            try:
                task_id = int(command[1])
                description = " ".join(command[2:])
                todo.update_task(task_id, description=description)
            except ValueError:
                print("Task ID must be a number.")
                
        elif action == "priority":
            if len(command) != 3:
                print("Please provide a task ID and priority level.")
                continue
            try:
                task_id = int(command[1])
                priority = command[2].lower()
                todo.update_task(task_id, priority=priority)
            except ValueError:
                print("Task ID must be a number.")
                
        elif action == "delete":
            if len(command) != 2:
                print("Please provide a task ID.")
                continue
            try:
                task_id = int(command[1])
                todo.delete_task(task_id)
            except ValueError:
                print("Task ID must be a number.")
                
        else:
            print("Unknown command. Type 'help' for available commands.")


if __name__ == "__main__":
    main()