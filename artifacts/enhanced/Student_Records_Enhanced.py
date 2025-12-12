"""
Student Records Management System - Enhanced Version
Created for CS 499 - Computer Science Capstone
Enhanced: December 2025

This enhanced version demonstrates:
- Efficient sorting algorithms (O(n log n) instead of O(n²))
- Hash table data structure for O(1) lookups
- Optimized search operations
- Comprehensive input validation and error handling
- Performance benchmarking capabilities
"""

import random
import time
from typing import Dict, List, Optional
import heapq


class StudentRecord:
    """
    Represents a single student record.
    
    Attributes:
        student_id (int): Unique student identifier
        name (str): Student's full name
        gpa (float): Grade point average (0.0-4.0)
        major (str): Student's major/program
    """
    
    def __init__(self, student_id: int, name: str, gpa: float, major: str):
        """
        Initialize a new StudentRecord.
        
        Args:
            student_id: Unique identifier
            name: Student name
            gpa: Grade point average
            major: Academic major
        """
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.major = major
    
    def display(self) -> None:
        """Display student information in formatted output."""
        print(f"{self.student_id} | {self.name} | GPA: {self.gpa:.2f} | {self.major}")
    
    def __repr__(self) -> str:
        """String representation for debugging."""
        return f"StudentRecord({self.student_id}, {self.name}, {self.gpa}, {self.major})"


class StudentDatabase:
    """
    Manages student records with efficient data structures and algorithms.
    
    Uses hash table (dictionary) for O(1) ID lookups instead of O(n) linear search.
    Implements efficient sorting with O(n log n) complexity.
    
    Attributes:
        students (Dict[int, StudentRecord]): Hash table of student records
        performance_stats (Dict): Stores performance metrics
    """
    
    def __init__(self):
        """Initialize empty student database with hash table structure."""
        self.students: Dict[int, StudentRecord] = {}
        self.performance_stats: Dict = {
            'add_count': 0,
            'search_count': 0,
            'sort_count': 0
        }
    
    def add_student(self, student_id: int, name: str, gpa: float, major: str) -> None:
        """
        Add a student to the database.
        
        Args:
            student_id: Unique student ID
            name: Student name
            gpa: Grade point average
            major: Academic major
            
        Raises:
            ValueError: If student ID already exists or GPA out of range
        """
        # Input validation
        if student_id in self.students:
            raise ValueError(f"Student ID {student_id} already exists")
        
        if not 0.0 <= gpa <= 4.0:
            raise ValueError(f"GPA must be between 0.0 and 4.0, got {gpa}")
        
        if not name.strip():
            raise ValueError("Student name cannot be empty")
        
        student = StudentRecord(student_id, name, gpa, major)
        self.students[student_id] = student
        self.performance_stats['add_count'] += 1
        print('Student added successfully!')
    
    def search_by_id(self, student_id: int) -> Optional[StudentRecord]:
        """
        Search for student by ID using hash table O(1) lookup.
        
        This is dramatically faster than the original O(n) linear search.
        For 10,000 students, this is ~10,000x faster.
        
        Args:
            student_id: Student ID to find
            
        Returns:
            StudentRecord if found, None otherwise
        """
        start_time = time.time()
        result = self.students.get(student_id)
        elapsed = time.time() - start_time
        
        self.performance_stats['search_count'] += 1
        self.performance_stats['last_search_time'] = elapsed
        
        return result
    
    def search_by_name(self, name: str) -> List[StudentRecord]:
        """
        Search for students by name (case-insensitive partial match).
        
        Args:
            name: Name or partial name to search
            
        Returns:
            List of matching StudentRecord objects
        """
        name_lower = name.lower()
        return [student for student in self.students.values()
                if name_lower in student.name.lower()]
    
    def get_sorted_by_gpa(self) -> List[StudentRecord]:
        """
        Get all students sorted by GPA using efficient O(n log n) algorithm.
        
        Uses Python's Timsort (hybrid merge sort/insertion sort) instead of
        the original O(n²) bubble sort. For 10,000 students, this is ~1,000x faster.
        
        Returns:
            List of students sorted by GPA (ascending)
        """
        start_time = time.time()
        
        # Convert dictionary values to list and sort - O(n log n)
        sorted_students = sorted(self.students.values(), 
                                key=lambda s: s.gpa)
        
        elapsed = time.time() - start_time
        self.performance_stats['sort_count'] += 1
        self.performance_stats['last_sort_time'] = elapsed
        
        return sorted_students
    
    def calculate_average_gpa(self) -> float:
        """
        Calculate average GPA of all students.
        
        Returns:
            Average GPA, or 0.0 if no students
        """
        if not self.students:
            return 0.0
        
        total = sum(student.gpa for student in self.students.values())
        return total / len(self.students)
    
    def find_top_students(self, n: int) -> List[StudentRecord]:
        """
        Find top N students by GPA using heap algorithm.
        
        Uses heapq.nlargest() with O(n log k) complexity instead of
        sorting entire list with O(n²) bubble sort.
        
        Args:
            n: Number of top students to return
            
        Returns:
            List of top N students by GPA
        """
        if n <= 0:
            return []
        
        start_time = time.time()
        
        # Use heap algorithm for efficient top-N selection
        top = heapq.nlargest(n, self.students.values(), 
                            key=lambda s: s.gpa)
        
        elapsed = time.time() - start_time
        self.performance_stats['last_top_n_time'] = elapsed
        
        return top
    
    def filter_by_major(self, major: str) -> List[StudentRecord]:
        """
        Get all students in a specific major.
        
        Args:
            major: Major to filter by
            
        Returns:
            List of students in the major
        """
        return [student for student in self.students.values()
                if student.major.lower() == major.lower()]
    
    def remove_student(self, student_id: int) -> bool:
        """
        Remove a student from the database.
        
        Args:
            student_id: ID of student to remove
            
        Returns:
            True if removed, False if not found
        """
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
    
    def display_all(self) -> None:
        """Display all students in the database."""
        if not self.students:
            print('No students in system')
        else:
            for student in self.students.values():
                student.display()
    
    def get_student_count(self) -> int:
        """Get total number of students."""
        return len(self.students)
    
    def display_performance_stats(self) -> None:
        """Display performance statistics for operations."""
        print("\n=== Performance Statistics ===")
        print(f"Total students: {len(self.students)}")
        print(f"Add operations: {self.performance_stats['add_count']}")
        print(f"Search operations: {self.performance_stats['search_count']}")
        print(f"Sort operations: {self.performance_stats['sort_count']}")
        
        if 'last_search_time' in self.performance_stats:
            print(f"Last search time: {self.performance_stats['last_search_time']:.6f} seconds")
        if 'last_sort_time' in self.performance_stats:
            print(f"Last sort time: {self.performance_stats['last_sort_time']:.6f} seconds")
        if 'last_top_n_time' in self.performance_stats:
            print(f"Last top-N time: {self.performance_stats['last_top_n_time']:.6f} seconds")


def generate_sample_data(database: StudentDatabase, num: int) -> None:
    """
    Generate sample student data for testing.
    
    Args:
        database: StudentDatabase instance
        num: Number of sample records to generate
    """
    majors = ['Computer Science', 'Mathematics', 'Engineering', 'Physics', 'Chemistry']
    first_names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 
                   'Henry', 'Iris', 'Jack', 'Kate', 'Liam', 'Maya', 'Noah', 'Olivia']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 
                  'Miller', 'Davis', 'Rodriguez', 'Martinez']
    
    for i in range(num):
        student_id = 1000 + i
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        gpa = round(random.uniform(2.0, 4.0), 2)
        major = random.choice(majors)
        
        try:
            database.add_student(student_id, name, gpa, major)
        except ValueError:
            pass  # Skip if ID already exists
    
    print(f'Generated {num} sample records')


class StudentDatabaseUI:
    """Handles user interface and input validation."""
    
    def __init__(self):
        """Initialize UI with StudentDatabase instance."""
        self.database = StudentDatabase()
    
    @staticmethod
    def display_menu() -> None:
        """Display main menu options."""
        print('\n=== Student Records System - Enhanced ===')
        print('1. Add Student')
        print('2. Search by ID')
        print('3. Search by Name')
        print('4. Sort by GPA')
        print('5. Display All')
        print('6. Calculate Average GPA')
        print('7. Find Top Students')
        print('8. Filter by Major')
        print('9. Generate Sample Data')
        print('10. Performance Statistics')
        print('11. Exit')
    
    @staticmethod
    def get_valid_integer(prompt: str, min_val: int = None, max_val: int = None) -> int:
        """
        Get validated integer input from user.
        
        Args:
            prompt: Input prompt
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            Valid integer
        """
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f'Error: Value must be at least {min_val}')
                    continue
                if max_val is not None and value > max_val:
                    print(f'Error: Value must be at most {max_val}')
                    continue
                return value
            except ValueError:
                print('Error: Please enter a valid number')
    
    @staticmethod
    def get_valid_float(prompt: str, min_val: float = None, max_val: float = None) -> float:
        """
        Get validated float input from user.
        
        Args:
            prompt: Input prompt
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            
        Returns:
            Valid float
        """
        while True:
            try:
                value = float(input(prompt))
                if min_val is not None and value < min_val:
                    print(f'Error: Value must be at least {min_val}')
                    continue
                if max_val is not None and value > max_val:
                    print(f'Error: Value must be at most {max_val}')
                    continue
                return value
            except ValueError:
                print('Error: Please enter a valid number')
    
    @staticmethod
    def get_non_empty_string(prompt: str) -> str:
        """Get non-empty string from user."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('Error: Input cannot be empty')
    
    def handle_add_student(self) -> None:
        """Handle adding a new student."""
        student_id = self.get_valid_integer('Enter student ID: ', min_val=1)
        name = self.get_non_empty_string('Enter name: ')
        gpa = self.get_valid_float('Enter GPA (0.0-4.0): ', min_val=0.0, max_val=4.0)
        major = self.get_non_empty_string('Enter major: ')
        
        try:
            self.database.add_student(student_id, name, gpa, major)
        except ValueError as e:
            print(f'Error: {e}')
    
    def handle_search_by_id(self) -> None:
        """Handle searching for a student by ID."""
        student_id = self.get_valid_integer('Enter student ID: ')
        result = self.database.search_by_id(student_id)
        
        if result:
            result.display()
        else:
            print('Student not found')
    
    def handle_search_by_name(self) -> None:
        """Handle searching for students by name."""
        name = self.get_non_empty_string('Enter name to search: ')
        results = self.database.search_by_name(name)
        
        print(f'Found {len(results)} students:')
        for student in results:
            student.display()
    
    def handle_sort_by_gpa(self) -> None:
        """Handle sorting and displaying students by GPA."""
        print('Sorting students by GPA...')
        sorted_students = self.database.get_sorted_by_gpa()
        print('Sorted!')
        
        for student in sorted_students:
            student.display()
    
    def handle_display_all(self) -> None:
        """Handle displaying all students."""
        self.database.display_all()
    
    def handle_average_gpa(self) -> None:
        """Handle calculating and displaying average GPA."""
        if self.database.get_student_count() > 0:
            avg = self.database.calculate_average_gpa()
            print(f'Average GPA: {avg:.2f}')
        else:
            print('No students in system')
    
    def handle_top_students(self) -> None:
        """Handle finding and displaying top N students."""
        n = self.get_valid_integer('How many top students? ', min_val=1)
        top = self.database.find_top_students(n)
        
        print(f'Top {n} students:')
        for student in top:
            student.display()
    
    def handle_filter_by_major(self) -> None:
        """Handle filtering students by major."""
        major = self.get_non_empty_string('Enter major: ')
        results = self.database.filter_by_major(major)
        
        print(f'Found {len(results)} students in {major}:')
        for student in results:
            student.display()
    
    def handle_generate_sample_data(self) -> None:
        """Handle generating sample student data."""
        num = self.get_valid_integer('How many sample records? ', min_val=1, max_val=10000)
        generate_sample_data(self.database, num)
    
    def handle_performance_stats(self) -> None:
        """Handle displaying performance statistics."""
        self.database.display_performance_stats()
    
    def run(self) -> None:
        """Main program loop."""
        print('Welcome to Student Records System - Enhanced Version')
        print('Featuring: O(1) hash table lookups and O(n log n) sorting!')
        
        while True:
            self.display_menu()
            choice = input('Choice: ').strip()
            
            if choice == '1':
                self.handle_add_student()
            elif choice == '2':
                self.handle_search_by_id()
            elif choice == '3':
                self.handle_search_by_name()
            elif choice == '4':
                self.handle_sort_by_gpa()
            elif choice == '5':
                self.handle_display_all()
            elif choice == '6':
                self.handle_average_gpa()
            elif choice == '7':
                self.handle_top_students()
            elif choice == '8':
                self.handle_filter_by_major()
            elif choice == '9':
                self.handle_generate_sample_data()
            elif choice == '10':
                self.handle_performance_stats()
            elif choice == '11':
                print('Thank you for using Student Records System!')
                break
            else:
                print('Invalid choice. Please enter a number between 1 and 11.')


def main():
    """Main entry point for the application."""
    ui = StudentDatabaseUI()
    ui.run()


if __name__ == '__main__':
    main()
