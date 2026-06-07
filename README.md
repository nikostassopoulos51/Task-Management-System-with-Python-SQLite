# Task-Management-System-with-Python-SQLite

A simple command-line Task Management System built with Python and SQLite. This application allows users to manage daily tasks efficiently by adding, viewing, completing, and deleting tasks.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Persistent storage using SQLite database
* Simple menu-driven interface

## Technologies Used

* Python 3
* SQLite3

## Project Structure

```text
TaskManagementSystem/
│
├── main_system.py      # Main application menu
├── task_manager.py     # Task management operations
├── database.py         # Database connection and initialization
└── tasks.db            # SQLite database (generated automatically)
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/task-management-system.git
```

2. Navigate to the project folder:

```bash
cd task-management-system
```

3. Run the application:

```bash
python main_system.py
```

## Usage

When the application starts, you will see the following menu:

```text
===== TASK MANAGER =====
1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
0. Exit
```

Choose an option by entering the corresponding number.

## Database

The system automatically creates an SQLite database file (`tasks.db`) with a `tasks` table containing:

| Field     | Type    |
| --------- | ------- |
| id        | INTEGER |
| title     | TEXT    |
| completed | INTEGER |

## Future Improvements

* Task deadlines
* Task priorities
* Task categories
* Search and filter tasks
* Graphical User Interface (GUI)
* User authentication

## Author

Developed as a Python Task Management System project.

## License

This project is open-source and available under the MIT License.
