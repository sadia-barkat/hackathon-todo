#!/usr/bin/env python3

from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    completed: bool = False
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

class TodoApp:
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "") -> Task:
        task = Task(id=self.next_id, title=title, description=description)
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def view_tasks(self, show_completed: bool = True) -> List[Task]:
        if show_completed:
            return self.tasks
        return [t for t in self.tasks if not t.completed]
    
    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        return True
    
    def complete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        task.completed = True
        return True
    
    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        return True

def display_task(task: Task):
    status = "✓" if task.completed else " "
    print(f"[{status}] ID: {task.id} | {task.title}")
    if task.description:
        print(f"    Description: {task.description}")
    print(f"    Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
    print()

def display_menu():
    print("\n=== Todo App ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. View Pending Tasks")
    print("4. Update Task")
    print("5. Complete Task")
    print("6. Delete Task")
    print("7. Exit")
    print("================")

def main():
    app = TodoApp()
    print("Welcome to Todo CLI Application!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            if not title:
                print("❌ Title cannot be empty!")
                continue
            description = input("Enter task description (optional): ").strip()
            task = app.add_task(title, description)
            print(f"✅ Task added successfully! (ID: {task.id})")
        
        elif choice == "2":
            tasks = app.view_tasks(show_completed=True)
            if not tasks:
                print("📋 No tasks found.")
            else:
                print(f"\n📋 All Tasks ({len(tasks)}):")
                print("-" * 50)
                for task in tasks:
                    display_task(task)
        
        elif choice == "3":
            tasks = app.view_tasks(show_completed=False)
            if not tasks:
                print("📋 No pending tasks!")
            else:
                print(f"\n📋 Pending Tasks ({len(tasks)}):")
                print("-" * 50)
                for task in tasks:
                    display_task(task)
        
        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to update: ").strip())
                task = app.get_task(task_id)
                if not task:
                    print(f"❌ Task with ID {task_id} not found!")
                    continue
                print(f"Current title: {task.title}")
                new_title = input("Enter new title (press Enter to keep current): ").strip()
                print(f"Current description: {task.description}")
                new_desc = input("Enter new description (press Enter to keep current): ").strip()
                title_update = new_title if new_title else None
                desc_update = new_desc if new_desc else None
                if app.update_task(task_id, title_update, desc_update):
                    print("✅ Task updated successfully!")
                else:
                    print("❌ Failed to update task!")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "5":
            try:
                task_id = int(input("Enter task ID to complete: ").strip())
                if app.complete_task(task_id):
                    print("✅ Task marked as completed!")
                else:
                    print(f"❌ Task with ID {task_id} not found!")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "6":
            try:
                task_id = int(input("Enter task ID to delete: ").strip())
                confirm = input(f"Are you sure you want to delete task {task_id}? (y/n): ").strip().lower()
                if confirm == 'y':
                    if app.delete_task(task_id):
                        print("✅ Task deleted successfully!")
                    else:
                        print(f"❌ Task with ID {task_id} not found!")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "7":
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice! Please enter 1-7.")

if __name__ == "__main__":
    main()
