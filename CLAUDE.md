# Phase I: Todo Console Application

## Overview
A simple CLI-based todo application built with Python 3.13 that supports CRUD operations (Create, Read, Update, Delete) and task completion tracking. All data is stored in-memory.

## Features
- ✅ Add new tasks with title and optional description
- ✅ View all tasks or filter by pending tasks
- ✅ Update task title and description
- ✅ Mark tasks as completed
- ✅ Delete tasks
- ✅ In-memory storage with auto-incrementing IDs

## Running the Application

### Using Python directly
```bash
python3 src/main.py
```

### Using uv (if installed)
```bash
uv run src/main.py
```

## Usage Guide

Once the application starts, you'll see a menu with these options:

1. **Add Task** - Create a new task
2. **View All Tasks** - Display all tasks
3. **View Pending Tasks** - Display only incomplete tasks
4. **Update Task** - Modify task details
5. **Complete Task** - Mark a task as done
6. **Delete Task** - Remove a task
7. **Exit** - Close the application

## Testing

### Test Commands
```bash
# Run the application
python3 src/main.py

# Test adding, viewing, completing, and deleting tasks
```

## Project Structure
```
todo-app/
├── src/
│   └── main.py          # Main application code
└── CLAUDE.md            # This file
```

## Requirements
- Python 3.13
- No external dependencies (uses only Python standard library)
