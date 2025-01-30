Task Management Application - Niveshartha
Features:
1. Add a New Task
2. View All Tasks
3. View Pending Tasks
4. View Completed Tasks
5. Update a Task
6. Delete a Task
7. Search Tasks by Description
8. Sort Tasks by Deadline, Status, or Priority
9. Due Date Reminders
10. Exit the Application

Prerequisites:
- Python 3.11.4 or higher
- SQLite 3.48.0 or higher

Installation:
1. Clone the repository or download the files to your local machine.
2. Ensure that Python 3.11.4 is installed on your system.
3. Install any required dependencies (if necessary).

How to Run:
1. Open a terminal/command prompt and navigate to the folder where the `task_manager.py` file is located.
2. Run the program using the following command:
   python task_manager.py

Usage:
After running the program, you'll see the main menu with the following options:
1. Add a Task: Enter task description, optional deadline, and priority.
2. View All Tasks: View all tasks in the system.
3. View Pending Tasks: View tasks that are pending.
4. View Completed Tasks: View tasks that are completed.
5. Update a Task: Modify the task details using the task ID.
6. Delete a Task: Delete a task by providing the task ID.
7. Search Tasks by Description: Search for tasks by entering a keyword.
8. Sort Tasks: Sort tasks by deadline, status, or priority.
9. Due Date Reminders: View tasks that are due within 24 hours.
10. Exit: Exit the application.

Database:
The tasks are stored in an SQLite database file named `tasks.db`. This database will be automatically created when you run the program. The database contains a `tasks` table with the following columns:
- id (INTEGER, Primary Key)
- description (TEXT)
- deadline (TEXT, optional)
- status (TEXT, either 'pending' or 'completed')
- priority (TEXT, optional)

Assumptions and Design Decisions:
1. SQLite Database: A local SQLite database (`tasks.db`) is used to persist tasks.
2. Status Field: Tasks have a `status` of either 'pending' or 'completed'.
3. Optional Deadline: A deadline for a task is optional. If not provided, it will remain NULL.
4. Priority Field: Priority for tasks is optional, with possible values like 'high', 'medium', or 'low'.
5. Unique Task IDs: Each task has a unique ID, which is automatically assigned by SQLite.