import sqlite3
from datetime import datetime, timedelta

# Database setup
DATABASE_NAME = "tasks.db"

def initialize_database():
    """Initialize the SQLite database and create the tasks table if it doesn't exist."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                deadline TEXT,
                status TEXT NOT NULL,
                priority TEXT
            )
        ''')
        conn.commit()

# Task class
class Task:
    def __init__(self, id, description, deadline, status, priority):
        self.id = id
        self.description = description
        self.deadline = deadline
        self.status = status
        self.priority = priority

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Deadline: {self.deadline}, Status: {self.status}, Priority: {self.priority}"

# CRUD Operations
def add_task(description, deadline=None, status="pending", priority=None):
    """Add a new task to the database."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (description, deadline, status, priority)
            VALUES (?, ?, ?, ?)
        ''', (description, deadline, status, priority))
        conn.commit()

def get_all_tasks():
    """Retrieve all tasks from the database."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks')
        tasks = cursor.fetchall()
        return [Task(*task) for task in tasks]

def get_task_by_id(task_id):
    """Retrieve a task by its ID."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
        task = cursor.fetchone()
        return Task(*task) if task else None

def update_task(task_id, description=None, deadline=None, status=None, priority=None):
    """Update a task's details."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        if description:
            cursor.execute('UPDATE tasks SET description = ? WHERE id = ?', (description, task_id))
        if deadline:
            cursor.execute('UPDATE tasks SET deadline = ? WHERE id = ?', (deadline, task_id))
        if status:
            cursor.execute('UPDATE tasks SET status = ? WHERE id = ?', (status, task_id))
        if priority:
            cursor.execute('UPDATE tasks SET priority = ? WHERE id = ?', (priority, task_id))
        conn.commit()

def delete_task(task_id):
    """Delete a task by its ID."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()

def filter_tasks_by_status(status):
    """Filter tasks by their status (pending/completed)."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE status = ?', (status,))
        tasks = cursor.fetchall()
        return [Task(*task) for task in tasks]

def search_tasks_by_description(keyword):
    """Search tasks by description containing a specific keyword."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE description LIKE ?', (f'%{keyword}%',))
        tasks = cursor.fetchall()
        return [Task(*task) for task in tasks]

def sort_tasks(sort_by):
    """Sort tasks by deadline or status."""
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        if sort_by == "deadline":
            cursor.execute('SELECT * FROM tasks ORDER BY deadline')
        elif sort_by == "status":
            cursor.execute('SELECT * FROM tasks ORDER BY status')
        elif sort_by == "priority":
            cursor.execute('SELECT * FROM tasks ORDER BY priority')
        tasks = cursor.fetchall()
        return [Task(*task) for task in tasks]

def check_due_date_reminders():
    """Check for tasks due within 24 hours."""
    now = datetime.now()
    tomorrow = now + timedelta(days=1)
    with sqlite3.connect(DATABASE_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tasks WHERE deadline BETWEEN ? AND ?', (now.strftime('%Y-%m-%d'), tomorrow.strftime('%Y-%m-%d')))
        tasks = cursor.fetchall()
        return [Task(*task) for task in tasks]

# User Interface
def display_menu():
    """Display the main menu."""
    print("\nTask Management Application Niveshartha")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. View pending tasks")
    print("4. View completed tasks")
    print("5. Update a task")
    print("6. Delete a task")
    print("7. Search tasks by description")
    print("8. Sort tasks")
    print("9. Due date reminders")
    print("10. Exit")

def add_task_ui():
    """UI for adding a task."""
    description = input("Enter task description: ")
    deadline = input("Enter deadline (YYYY-MM-DD, optional): ")
    deadline = deadline if deadline else None
    priority = input("Enter priority (high/medium/low, optional): ")
    priority = priority if priority else None
    add_task(description, deadline, "pending", priority)
    print("Task added successfully!")

def view_all_tasks_ui():
    """UI for viewing all tasks."""
    tasks = get_all_tasks()
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def view_tasks_by_status_ui(status):
    """UI for viewing tasks by status."""
    tasks = filter_tasks_by_status(status)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print(f"No {status} tasks found.")

def update_task_ui():
    """UI for updating a task."""
    task_id = input("Enter task ID to update: ")
    task = get_task_by_id(task_id)
    if task:
        print(f"Current task details: {task}")
        description = input("Enter new description (leave blank to keep current): ")
        deadline = input("Enter new deadline (YYYY-MM-DD, leave blank to keep current): ")
        status = input("Enter new status (pending/completed, leave blank to keep current): ")
        priority = input("Enter new priority (high/medium/low, leave blank to keep current): ")
        update_task(task_id, description or None, deadline or None, status or None, priority or None)
        print("Task updated successfully!")
    else:
        print("Task not found.")

def delete_task_ui():
    """UI for deleting a task."""
    task_id = input("Enter task ID to delete: ")
    task = get_task_by_id(task_id)
    if task:
        delete_task(task_id)
        print("Task deleted successfully!")
    else:
        print("Task not found.")

def search_tasks_ui():
    """UI for searching tasks by description."""
    keyword = input("Enter a keyword to search for tasks: ")
    tasks = search_tasks_by_description(keyword)
    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found matching the keyword.")

def sort_tasks_ui():
    """UI for sorting tasks."""
    print("Sort by:")
    print("1. Deadline")
    print("2. Status")
    print("3. Priority")
    sort_choice = input("Enter your choice: ")
    if sort_choice == "1":
        tasks = sort_tasks("deadline")
    elif sort_choice == "2":
        tasks = sort_tasks("status")
    elif sort_choice == "3":
        tasks = sort_tasks("priority")
    else:
        print("Invalid choice.")
        return

    if tasks:
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")

def due_date_reminders_ui():
    """UI for displaying due date reminders."""
    tasks = check_due_date_reminders()
    if tasks:
        print("Tasks due within 24 hours:")
        for task in tasks:
            print(task)
    else:
        print("No tasks due within 24 hours.")

# Main program loop
def main():
    initialize_database()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task_ui()
        elif choice == "2":
            view_all_tasks_ui()
        elif choice == "3":
            view_tasks_by_status_ui("pending")
        elif choice == "4":
            view_tasks_by_status_ui("completed")
        elif choice == "5":
            update_task_ui()
        elif choice == "6":
            delete_task_ui()
        elif choice == "7":
            search_tasks_ui()
        elif choice == "8":
            sort_tasks_ui()
        elif choice == "9":
            due_date_reminders_ui()
        elif choice == "10":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()