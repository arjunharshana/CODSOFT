import json
import os

# Define the filename for storing tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    # Check if the file exists
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            return tasks
    except (json.JSONDecodeError, IOError):
        # If the file is empty, return an empty list
        return []

def save_tasks(tasks):
    # Saves the current list of tasks to the JSON file.
    try:
        with open(TASKS_FILE, 'w') as f:
            json.dump(tasks, f, indent=4)
    except IOError as e:
        print(f"Error saving tasks: {e}")

def display_tasks(tasks):
    # Displays all the tasks.
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\n--- Your To-Do List ---")
    # Sort tasks to show pending ones first
    sorted_tasks = sorted(tasks, key=lambda x: x['completed'])

    for idx, task in enumerate(sorted_tasks, 1):
        status_symbol = "[X]" if task['completed'] else "[ ]"
        task_text = task['task']

        # Apply strikethrough for completed tasks
        if task['completed']:
            task_text = f"\033[9m{task_text}\033[0m"
        print(f"{idx}. {status_symbol} {task_text}")
    print("-----------------------\n")


def add_task(tasks):
    task_description = input("Enter the new task: ").strip()
    if task_description:
        new_task = {"task": task_description, "completed": False}
        tasks.append(new_task)
        save_tasks(tasks)
        print(f"\nTask '{task_description}' added successfully!")
    else:
        print("\nTask description cannot be empty.")

def mark_task_complete(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to mark as complete: "))
        # Adjust for zero-based index
        task_index = task_num - 1

        if 0 <= task_index < len(tasks):
            # Mark the task as complete
            tasks[task_index]['completed'] = True
            save_tasks(tasks)
            print(f"\nTask {task_num} marked as complete. Well done!")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def delete_task(tasks):
    display_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the number of the task to delete: "))
        # Adjust for zero-based index
        task_index = task_num - 1
        if 0 <= task_index < len(tasks):
            # Remove the task from the list
            removed_task = tasks.pop(task_index)
            save_tasks(tasks)
            print(f"\nTask '{removed_task['task']}' has been deleted.")
        else:
            print("\nInvalid task number. Please try again.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

def main():
    # Main function to run the To-Do List application.
    tasks = load_tasks()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View To-Do List")
        print("2. Add a New Task")
        print("3. Mark a Task as Complete")
        print("4. Delete a Task")
        print("5. Exit")
        print("===========================")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("\nThank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option (1-5).")

if __name__ == "__main__":
    main()
