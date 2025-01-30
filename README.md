Task Management Application Niveshartha

Features:
- Add a new task

    - View all tasks

    - View pending tasks

    - View completed tasks

    - Update a task

    - Delete a task

    - Exit the application
Prerequisites:
    - Python 3.11.4

    - SQLite  3.48.0 
Installation:
1. Clone the repository or download the files to your local machine.

    2. Ensure that you have Python 3.11.4 installed on your system.

    3. Install any required dependencies (if necessary).
How to Run:
1. Open a terminal/command prompt and navigate to the folder where the `task_manager.py` file is located.

    2. Run the program using the following command:

    python task_manager.py
Usage:
After running the program, you'll see the main menu with the following options:

    1. Add a task

    2. View all tasks

    3. View pending tasks

    4. View completed tasks

    5. Update a task

    6. Delete a task

    7. Exit


    To add a task, simply enter a task description and an optional deadline. You can update or delete tasks by providing the task ID.
Database:
The tasks are stored in an SQLite database file named `tasks.db`. This database will be automatically created when you run the program. The database contains a `tasks` table with the following columns:

    - `id` (INTEGER, Primary Key)

    - `description` (TEXT)

    - `deadline` (TEXT, optional)

    - `status` (TEXT, either "pending" or "completed")
Assumptions and Design Decisions:
1. **SQLite Database**: A local SQLite database (`tasks.db`) is used to persist tasks.

    2. **Status Field**: Tasks are assumed to have a `status` of either "pending" or "completed".

    3. **Optional Deadline**: The deadline for a task is optional. If not provided, it will remain `NULL`.

    4. **Unique Task IDs**: Each task has a unique ID, which is automatically assigned by SQLite.