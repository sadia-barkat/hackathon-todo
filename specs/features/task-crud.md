# Phase I: Todo Console Application

## Requirements

### Language
- Python 3.13

### Functionality
Create a CLI application to manage tasks with the following operations:

1. **Add Task**
   - User can add a new task with title (required)
   - User can optionally add a description

2. **View Tasks**
   - View all tasks (completed and pending)
   - View only pending tasks
   - Display task ID, title, description, completion status, and created date

3. **Update Task**
   - Update task title
   - Update task description
   - Identify task by ID

4. **Complete Task**
   - Mark task as completed
   - Identify task by ID

5. **Delete Task**
   - Remove task permanently
   - Identify task by ID
   - Ask for confirmation before deletion

### Storage
- In-memory list (no persistence required)
- Tasks stored only during application runtime
- Data is lost when application closes

### Data Model
Each task should contain:
- `id`: Unique identifier (auto-increment)
- `title`: Task title (required)
- `description`: Task description (optional)
- `completed`: Boolean status (default: false)
- `created_at`: Timestamp of creation

### User Interface
- Command-line menu-based interface
- Clear numbered options for each operation
- Input validation and error messages
- Confirmation prompts for destructive operations

### Success Criteria
- ✅ All CRUD operations working
- ✅ User-friendly CLI interface
- ✅ Input validation
- ✅ No external dependencies (standard library only)
```

Save karo: **Ctrl+X**, **Y**, **Enter**

Ab aapke paas complete project structure hai:
```
todo-app/
├── specs/
│   └── features/
│       └── task-crud.md    ← Specifications
├── src/
│   └── main.py             ← Code
└── CLAUDE.md               ← Documentation
