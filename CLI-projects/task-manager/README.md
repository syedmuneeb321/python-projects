# Task Manager CLI

A lightweight **command-line task manager** built in Python.
This project demonstrates **file handling, CLI design, and virtual environment management** using `uv`.

---

## Features

* Add new tasks
* Show tasks with completion status
* Mark tasks as completed
* Delete tasks
* Persistent storage using `task.txt`

---

## Tech Stack

* **Language:** Python (≥3.10)
* **Environment Management:** `uv` (virtual environment + dependency manager)
* **File Storage:** Plain text (`task.txt`)

---

## How to Run

1. **Clone Repository**

```bash
git clone https://github.com/syedmuneeb321/python-projects.git
cd CLI-projects/task-manager
```

2. **Create and Activate Virtual Environment**

```bash
uv venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
```

3. **Run the Application**

```bash
uv run main.py
```

---

## Skills Demonstrated

* Python CLI application design
* Reading/writing data to files
* Clean code structure with functions
* Basic error handling and validation
* Using `uv` for project and environment management

---

## Project Structure

```
task-manager/
│
├── main.py         # Main CLI application
├── task.txt        # Task data storage
├── pyproject.toml  # Project configuration
├── uv.lock         # Lock file (uv)
└── README.md       # Documentation
```

