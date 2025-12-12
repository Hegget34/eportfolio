# Student Records Management System
# Created for CS 260 - Data Structures

import random

class StudentRecord:
    def __init__(self, id, name, gpa, major):
        self.id = id
        self.name = name
        self.gpa = gpa
        self.major = major
    
    def display(self):
        print(f"{self.id} | {self.name} | GPA: {self.gpa} | {self.major}")

# Using a simple list to store students
students = []

def addStudent(id, name, gpa, major):
    s = StudentRecord(id, name, gpa, major)
    students.append(s)

def bubbleSort():
    # Bubble sort by GPA - O(n^2) complexity
    n = len(students)
    for i in range(n):
        for j in range(0, n-i-1):
            if students[j].gpa > students[j+1].gpa:
                temp = students[j]
                students[j] = students[j+1]
                students[j+1] = temp

def linearSearch(studentId):
    # Linear search - O(n) complexity
    for i in range(len(students)):
        if students[i].id == studentId:
            return students[i]
    return None

def searchByName(name):
    # Linear search through all records
    found = []
    for i in range(len(students)):
        if name.lower() in students[i].name.lower():
            found.append(students[i])
    return found

def calculateAverage():
    total = 0
    for i in range(len(students)):
        total = total + students[i].gpa
    avg = total / len(students)
    return avg

def findTopStudents(n):
    # Inefficient: sorts entire list just to get top n
    bubbleSort()
    top = []
    count = 0
    for i in range(len(students)-1, -1, -1):
        if count < n:
            top.append(students[i])
            count = count + 1
    return top

def filterByMajor(major):
    result = []
    for student in students:
        if student.major == major:
            result.append(student)
    return result

def removeStudent(studentId):
    for i in range(len(students)):
        if students[i].id == studentId:
            students.pop(i)
            return True
    return False

# Generate sample data
def generateSampleData(num):
    majors = ['Computer Science', 'Mathematics', 'Engineering', 'Physics', 'Chemistry']
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Henry', 'Iris', 'Jack']
    
    for i in range(num):
        id = 1000 + i
        name = random.choice(names) + ' ' + random.choice(names)
        gpa = round(random.uniform(2.0, 4.0), 2)
        major = random.choice(majors)
        addStudent(id, name, gpa, major)

def displayAll():
    for s in students:
        s.display()

def menu():
    print('\n=== Student Records System ===')
    print('1. Add Student')
    print('2. Search by ID')
    print('3. Search by Name')
    print('4. Sort by GPA')
    print('5. Display All')
    print('6. Calculate Average GPA')
    print('7. Find Top Students')
    print('8. Filter by Major')
    print('9. Generate Sample Data')
    print('10. Exit')
    return input('Choice: ')

def main():
    while True:
        choice = menu()
        
        if choice == '1':
            id = int(input('Enter student ID: '))
            name = input('Enter name: ')
            gpa = float(input('Enter GPA: '))
            major = input('Enter major: ')
            addStudent(id, name, gpa, major)
            print('Student added!')
            
        elif choice == '2':
            id = int(input('Enter student ID: '))
            result = linearSearch(id)
            if result:
                result.display()
            else:
                print('Student not found')
                
        elif choice == '3':
            name = input('Enter name to search: ')
            results = searchByName(name)
            print(f'Found {len(results)} students:')
            for r in results:
                r.display()
                
        elif choice == '4':
            print('Sorting students by GPA...')
            bubbleSort()
            print('Sorted!')
            displayAll()
            
        elif choice == '5':
            displayAll()
            
        elif choice == '6':
            if len(students) > 0:
                avg = calculateAverage()
                print(f'Average GPA: {avg:.2f}')
            else:
                print('No students in system')
                
        elif choice == '7':
            n = int(input('How many top students? '))
            top = findTopStudents(n)
            print(f'Top {n} students:')
            for s in top:
                s.display()
                
        elif choice == '8':
            major = input('Enter major: ')
            results = filterByMajor(major)
            print(f'Found {len(results)} students in {major}:')
            for r in results:
                r.display()
                
        elif choice == '9':
            num = int(input('How many sample records? '))
            generateSampleData(num)
            print(f'Generated {num} sample records')
            
        elif choice == '10':
            break

if __name__ == '__main__':
    main()
