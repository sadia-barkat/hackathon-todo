#!/usr/bin/env python3
"""
Todo Console Application - Complete CRUD with Search, Filter & Sort
Supports: Add, View, Update, Delete, Search, Filter by Priority/Category, and Sorting
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum


class Priority(Enum):
    """Task priority levels."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


@dataclass
class Task:
    """Represents a single task with priority and category."""
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: Priority = Priority.MEDIUM
    category: str = "General"
    created_at: datetime = field(default_factory=datetime.now)
    completed_at: Optional[datetime] = None


class TodoApp:
    """Main Todo application with advanced features."""
    
    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1
    
    def add_task(self, title: str, description: str = "", 
                 priority: Priority = Priority.MEDIUM, category: str = "General") -> Task:
        """Add a new task with priority and category."""
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            priority=priority,
            category=category
        )
        self.tasks.append(task)
        self.next_id += 1
        return task
    
    def view_tasks(self, show_completed: bool = True) -> List[Task]:
        """View all tasks or filter by completion status."""
        if show_completed:
            return self.tasks
        return [t for t in self.tasks if not t.completed]
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def update_task(self, task_id: int, title: str = None, description: str = None,
                   priority: Priority = None, category: str = None) -> bool:
        """Update a task's details."""
        task = self.get_task(task_id)
        if not task:
            return False
        
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        if priority is not None:
            task.priority = priority
        if category is not None:
            task.category = category
        return True
    
    def complete_task(self, task_id: int) -> bool:
        """Mark a task as completed."""
        task = self.get_task(task_id)
        if not task:
            return False
        task.completed = True
        task.completed_at = datetime.now()
        return True
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task."""
        task = self.get_task(task_id)
        if not task:
            return False
        self.tasks.remove(task)
        return True
    
    def search_tasks(self, query: str) -> List[Task]:
        """Search tasks by title or description."""
        query = query.lower()
        return [t for t in self.tasks 
                if query in t.title.lower() or query in t.description.lower()]
    
    def filter_by_priority(self, priority: Priority) -> List[Task]:
        """Filter tasks by priority."""
        return [t for t in self.tasks if t.priority == priority]
    
    def filter_by_category(self, category: str) -> List[Task]:
        """Filter tasks by category."""
        return [t for t in self.tasks if t.category.lower() == category.lower()]
    
    def sort_tasks(self, tasks: List[Task], by: str = "id", reverse: bool = False) -> List[Task]:
        """Sort tasks by: id, title, priority, created_at, or category."""
        if by == "id":
            return sorted(tasks, key=lambda t: t.id, reverse=reverse)
        elif by == "title":
            return sorted(tasks, key=lambda t: t.title.lower(), reverse=reverse)
        elif by == "priority":
            priority_order = {Priority.LOW: 1, Priority.MEDIUM: 2, Priority.HIGH: 3}
            return sorted(tasks, key=lambda t: priority_order[t.priority], reverse=reverse)
        elif by == "created":
            return sorted(tasks, key=lambda t: t.created_at, reverse=reverse)
        elif by == "category":
            return sorted(tasks, key=lambda t: t.category.lower(), reverse=reverse)
        return tasks
    
    def get_categories(self) -> List[str]:
        """Get all unique categories."""
        return list(set(t.category for t in self.tasks))


def display_task(task: Task, detailed: bool = True):
    """Display a single task."""
    status = "✓" if task.completed else " "
    priority_icons = {Priority.LOW: "🟢", Priority.MEDIUM: "🟡", Priority.HIGH: "🔴"}
    
    print(f"[{status}] ID: {task.id} | {priority_icons[task.priority]} {task.title}")
    if detailed:
        if task.description:
            print(f"    📝 Description: {task.description}")
        print(f"    🏷️  Category: {task.category} | ⚡ Priority: {task.priority.value}")
        print(f"    📅 Created: {task.created_at.strftime('%Y-%m-%d %H:%M')}")
        if task.completed and task.completed_at:
            print(f"    ✅ Completed: {task.completed_at.strftime('%Y-%m-%d %H:%M')}")
    print()


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("        📋 TODO APP - MAIN MENU")
    print("="*50)
    print("1️⃣  Add Task")
    print("2️⃣  View All Tasks")
    print("3️⃣  View Pending Tasks")
    print("4️⃣  Update Task")
    print("5️⃣  Complete Task")
    print("6️⃣  Delete Task")
    print("7️⃣  Search Tasks")
    print("8️⃣  Filter by Priority")
    print("9️⃣  Filter by Category")
    print("🔟 Sort Tasks")
    print("0️⃣  Exit")
    print("="*50)


def get_priority_input() -> Priority:
    """Get priority input from user."""
    print("\nSelect Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    choice = input("Enter choice (1-3, default: 2): ").strip()
    
    if choice == "1":
        return Priority.LOW
    elif choice == "3":
        return Priority.HIGH
    return Priority.MEDIUM


def main():
    """Main application loop."""
    app = TodoApp()
    
    print("\n" + "="*50)
    print("    🎉 WELCOME TO TODO CLI APPLICATION! 🎉")
    print("="*50)
    
    while True:
        display_menu()
        choice = input("👉 Enter your choice (0-10): ").strip()
        
        if choice == "1":
            # Add Task
            print("\n➕ ADD NEW TASK")
            print("-" * 50)
            title = input("Task title: ").strip()
            if not title:
                print("❌ Title cannot be empty!")
                continue
            description = input("Description (optional): ").strip()
            category = input("Category (default: General): ").strip() or "General"
            priority = get_priority_input()
            
            task = app.add_task(title, description, priority, category)
            print(f"✅ Task added successfully! (ID: {task.id})")
        
        elif choice == "2":
            # View All Tasks
            print("\n📋 ALL TASKS")
            print("-" * 50)
            tasks = app.view_tasks(show_completed=True)
            if not tasks:
                print("📭 No tasks found.")
            else:
                print(f"Total: {len(tasks)} task(s)\n")
                for task in tasks:
                    display_task(task)
        
        elif choice == "3":
            # View Pending Tasks
            print("\n⏳ PENDING TASKS")
            print("-" * 50)
            tasks = app.view_tasks(show_completed=False)
            if not tasks:
                print("🎉 No pending tasks!")
            else:
                print(f"Total: {len(tasks)} pending task(s)\n")
                for task in tasks:
                    display_task(task)
        
        elif choice == "4":
            # Update Task
            print("\n✏️  UPDATE TASK")
            print("-" * 50)
            try:
                task_id = int(input("Enter task ID: ").strip())
                task = app.get_task(task_id)
                if not task:
                    print(f"❌ Task with ID {task_id} not found!")
                    continue
                
                print(f"\nCurrent: {task.title}")
                new_title = input("New title (Enter to keep): ").strip()
                
                print(f"Current: {task.description}")
                new_desc = input("New description (Enter to keep): ").strip()
                
                print(f"Current: {task.category}")
                new_category = input("New category (Enter to keep): ").strip()
                
                print(f"Current: {task.priority.value}")
                update_priority = input("Update priority? (y/n): ").strip().lower()
                new_priority = get_priority_input() if update_priority == 'y' else None
                
                if app.update_task(
                    task_id,
                    new_title or None,
                    new_desc or None,
                    new_priority,
                    new_category or None
                ):
                    print("✅ Task updated successfully!")
                else:
                    print("❌ Failed to update task!")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "5":
            # Complete Task
            print("\n✅ COMPLETE TASK")
            print("-" * 50)
            try:
                task_id = int(input("Enter task ID: ").strip())
                if app.complete_task(task_id):
                    print("✅ Task marked as completed!")
                else:
                    print(f"❌ Task with ID {task_id} not found!")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "6":
            # Delete Task
            print("\n🗑️  DELETE TASK")
            print("-" * 50)
            try:
                task_id = int(input("Enter task ID: ").strip())
                task = app.get_task(task_id)
                if task:
                    print(f"\nTask: {task.title}")
                    confirm = input("⚠️  Delete this task? (y/n): ").strip().lower()
                    if confirm == 'y':
                        if app.delete_task(task_id):
                            print("✅ Task deleted successfully!")
                    else:
                        print("❌ Deletion cancelled.")
                else:
                    print(f"❌ Task with ID {task_id} not found!")
            except ValueError:
                print("❌ Invalid ID!")
        
        elif choice == "7":
            # Search Tasks
            print("\n🔍 SEARCH TASKS")
            print("-" * 50)
            query = input("Enter search query: ").strip()
            if query:
                results = app.search_tasks(query)
                if results:
                    print(f"\n✨ Found {len(results)} result(s):\n")
                    for task in results:
                        display_task(task)
                else:
                    print("❌ No tasks found matching your query.")
            else:
                print("❌ Search query cannot be empty!")
        
        elif choice == "8":
            # Filter by Priority
            print("\n⚡ FILTER BY PRIORITY")
            print("-" * 50)
            priority = get_priority_input()
            results = app.filter_by_priority(priority)
            if results:
                print(f"\n✨ {len(results)} task(s) with {priority.value} priority:\n")
                for task in results:
                    display_task(task)
            else:
                print(f"❌ No tasks found with {priority.value} priority.")
        
        elif choice == "9":
            # Filter by Category
            print("\n🏷️  FILTER BY CATEGORY")
            print("-" * 50)
            categories = app.get_categories()
            if categories:
                print("Available categories:")
                for idx, cat in enumerate(categories, 1):
                    print(f"  {idx}. {cat}")
            category = input("\nEnter category name: ").strip()
            if category:
                results = app.filter_by_category(category)
                if results:
                    print(f"\n✨ {len(results)} task(s) in '{category}' category:\n")
                    for task in results:
                        display_task(task)
                else:
                    print(f"❌ No tasks found in '{category}' category.")
            else:
                print("❌ Category cannot be empty!")
        
        elif choice == "10":
            # Sort Tasks
            print("\n🔀 SORT TASKS")
            print("-" * 50)
            print("Sort by:")
            print("1. ID")
            print("2. Title")
            print("3. Priority")
            print("4. Created Date")
            print("5. Category")
            sort_choice = input("Enter choice (1-5): ").strip()
            
            sort_map = {"1": "id", "2": "title", "3": "priority", "4": "created", "5": "category"}
            sort_by = sort_map.get(sort_choice, "id")
            
            reverse = input("Descending order? (y/n, default: n): ").strip().lower() == 'y'
            
            tasks = app.view_tasks()
            sorted_tasks = app.sort_tasks(tasks, by=sort_by, reverse=reverse)
            
            if sorted_tasks:
                print(f"\n✨ Tasks sorted by {sort_by}:\n")
                for task in sorted_tasks:
                    display_task(task)
            else:
                print("❌ No tasks to sort.")
        
        elif choice == "0":
            # Exit
            print("\n" + "="*50)
            print("       👋 THANK YOU FOR USING TODO APP!")
            print("="*50)
            break
        
        else:
            print("❌ Invalid choice! Please enter 0-10.")


if __name__ == "__main__":
    main()
