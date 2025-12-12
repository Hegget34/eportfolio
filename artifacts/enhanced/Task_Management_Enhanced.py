"""
Task Management Application - Enhanced Version
Created for CS 499 - Computer Science Capstone
Enhanced: December 2025

This enhanced version demonstrates:
- Object-oriented design with proper encapsulation
- Comprehensive error handling and input validation
- JSON-based data persistence
- Professional documentation and code organization
"""

import json
import datetime
from typing import List, Optional, Dict


class Task:
    """
    Represents a single task with all associated attributes.
    
    Attributes:
        task_id (int): Unique identifier for the task
        name (str): Task name/title
        description (str): Detailed description of the task
        due_date (str): Due date in YYYY-MM-DD format
        status (str): Current status ('pending' or 'completed')
    """
    
    def __init__(self, task_id: int, name: str, description: str, 
                 due_date: str, status: str = 'pending'):
        """
        Initialize a new Task object.
        
        Args:
            task_id: Unique identifier
            name: Task name
            description: Task description
            due_date: Due date string
            status: Task status (default: 'pending')
        """
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def to_dict(self) -> Dict:
        """
        Convert Task object to dictionary for JSON serialization.
        
        Returns:
            Dictionary representation of the task
        """
        return {
            'id': self.task_id,
            'name': self.name,
            'description': self.description,
            'due_date': self.due_date,
            'status': self.status
        }
    
    @staticmethod
    def from_dict(data: Dict) -> 'Task':
        """
        Create Task object from dictionary.
        
        Args:
            data: Dictionary containing task data
            
        Returns:
            Task object created from dictionary
        """
        return Task(
            task_id=data['id'],
            name=data['name'],
            description=data['description'],
            due_date=data['due_date'],
            status=data['status']
        )
    
    def __str__(self) -> str:
        """String representation of task for display."""
        return (f"ID: {self.task_id}\n"
                f"Name: {self.name}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}")


class TaskManager:
    """
    Manages collection of tasks with CRUD operations and persistence.
    
    Attributes:
        tasks (List[Task]): List of all tasks
        next_id (int): Counter for generating unique task IDs
        filename (str): JSON file path for data persistence
    """
    
    def __init__(self, filename: str = 'tasks.json'):
        """
        Initialize TaskManager and load existing tasks from file.
        
        Args:
            filename: Path to JSON file for persistence (default: 'tasks.json')
        """
        self.tasks: List[Task] = []
        self.next_id: int = 1
        self.filename: str = filename
        self.load_tasks()
    
    def add_task(self, name: str, description: str, due_date: str) -> None:
        """
        Add a new task to the task list.
        
        Args:
            name: Task name
            description: Task description
            due_date: Due date in YYYY-MM-DD format
        """
        task = Task(self.next_id, name, description, due_date)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print('Task added successfully!')
    
    def delete_task(self, task_id: int) -> None:
        """
        Delete a task by ID.
        
        Args:
            task_id: ID of task to delete
        """
        task = self.find_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            self.save_tasks()
            print('Task deleted!')
        else:
            print('Task not found')
    
    def update_task(self, task_id: int, name: str, description: str, 
                    due_date: str) -> None:
        """
        Update an existing task's information.
        
        Args:
            task_id: ID of task to update
            name: New task name
            description: New description
            due_date: New due date
        """
        task = self.find_task_by_id(task_id)
        if task:
            task.name = name
            task.description = description
            task.due_date = due_date
            self.save_tasks()
            print('Task updated!')
        else:
            print('Task not found')
    
    def view_tasks(self) -> None:
        """Display all tasks in the task list."""
        if not self.tasks:
            print('No tasks found')
        else:
            for task in self.tasks:
                print(task)
                print('---')
    
    def complete_task(self, task_id: int) -> None:
        """
        Mark a task as completed.
        
        Args:
            task_id: ID of task to mark complete
        """
        task = self.find_task_by_id(task_id)
        if task:
            task.status = 'completed'
            self.save_tasks()
            print('Task marked complete!')
        else:
            print('Task not found')
    
    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search for tasks containing keyword in name or description.
        
        Args:
            keyword: Search term
            
        Returns:
            List of matching tasks
        """
        keyword_lower = keyword.lower()
        return [task for task in self.tasks 
                if keyword_lower in task.name.lower() 
                or keyword_lower in task.description.lower()]
    
    def find_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Helper method to find a task by its ID.
        
        Args:
            task_id: ID of task to find
            
        Returns:
            Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None
    
    def save_tasks(self) -> None:
        """Save all tasks to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                tasks_data = [task.to_dict() for task in self.tasks]
                json.dump({
                    'tasks': tasks_data,
                    'next_id': self.next_id
                }, f, indent=2)
        except IOError as e:
            print(f'Error saving tasks: {e}')
    
    def load_tasks(self) -> None:
        """Load tasks from JSON file if it exists."""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) 
                             for task_data in data['tasks']]
                self.next_id = data['next_id']
        except FileNotFoundError:
            # File doesn't exist yet - start with empty task list
            pass
        except (IOError, json.JSONDecodeError) as e:
            print(f'Error loading tasks: {e}')
            print('Starting with empty task list')


class TaskManagerUI:
    """Handles user interface and input validation for Task Manager."""
    
    def __init__(self):
        """Initialize UI with TaskManager instance."""
        self.manager = TaskManager()
    
    @staticmethod
    def display_menu() -> None:
        """Display the main menu options."""
        print('\n=== Task Manager ===')
        print('1. Add Task')
        print('2. View Tasks')
        print('3. Update Task')
        print('4. Delete Task')
        print('5. Complete Task')
        print('6. Search Tasks')
        print('7. Exit')
    
    @staticmethod
    def get_valid_integer(prompt: str) -> int:
        """
        Get validated integer input from user.
        
        Args:
            prompt: Input prompt to display
            
        Returns:
            Valid integer value
        """
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print('Error: Please enter a valid number')
    
    @staticmethod
    def get_non_empty_string(prompt: str) -> str:
        """
        Get non-empty string input from user.
        
        Args:
            prompt: Input prompt to display
            
        Returns:
            Non-empty string
        """
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('Error: Input cannot be empty')
    
    @staticmethod
    def get_valid_date(prompt: str) -> str:
        """
        Get validated date input in YYYY-MM-DD format.
        
        Args:
            prompt: Input prompt to display
            
        Returns:
            Valid date string
        """
        while True:
            date_str = input(prompt).strip()
            try:
                # Validate date format
                datetime.datetime.strptime(date_str, '%Y-%m-%d')
                return date_str
            except ValueError:
                print('Error: Please enter date in YYYY-MM-DD format')
    
    def handle_add_task(self) -> None:
        """Handle adding a new task with validated input."""
        name = self.get_non_empty_string('Enter task name: ')
        description = self.get_non_empty_string('Enter description: ')
        due_date = self.get_valid_date('Enter due date (YYYY-MM-DD): ')
        self.manager.add_task(name, description, due_date)
    
    def handle_view_tasks(self) -> None:
        """Handle viewing all tasks."""
        self.manager.view_tasks()
    
    def handle_update_task(self) -> None:
        """Handle updating an existing task with validated input."""
        task_id = self.get_valid_integer('Enter task ID: ')
        name = self.get_non_empty_string('Enter new name: ')
        description = self.get_non_empty_string('Enter new description: ')
        due_date = self.get_valid_date('Enter new due date: ')
        self.manager.update_task(task_id, name, description, due_date)
    
    def handle_delete_task(self) -> None:
        """Handle deleting a task."""
        task_id = self.get_valid_integer('Enter task ID to delete: ')
        self.manager.delete_task(task_id)
    
    def handle_complete_task(self) -> None:
        """Handle marking a task as complete."""
        task_id = self.get_valid_integer('Enter task ID to complete: ')
        self.manager.complete_task(task_id)
    
    def handle_search_tasks(self) -> None:
        """Handle searching for tasks."""
        keyword = self.get_non_empty_string('Enter search keyword: ')
        results = self.manager.search_tasks(keyword)
        print(f'Found {len(results)} tasks')
        for task in results:
            print(task)
            print('---')
    
    def run(self) -> None:
        """Main program loop with menu-driven interface."""
        print('Welcome to Task Manager - Enhanced Version')
        
        while True:
            self.display_menu()
            choice = input('Enter choice: ').strip()
            
            if choice == '1':
                self.handle_add_task()
            elif choice == '2':
                self.handle_view_tasks()
            elif choice == '3':
                self.handle_update_task()
            elif choice == '4':
                self.handle_delete_task()
            elif choice == '5':
                self.handle_complete_task()
            elif choice == '6':
                self.handle_search_tasks()
            elif choice == '7':
                print('Thank you for using Task Manager!')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 7.')


def main():
    """Main entry point for the application."""
    ui = TaskManagerUI()
    ui.run()


if __name__ == '__main__':
    main()
