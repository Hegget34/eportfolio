# Task Management Application
# Created for CS 320 - Software Engineering

import datetime

# Global variables
tasks = []
id = 1

def addTask(name, desc, date):
    global id
    global tasks
    t = {}
    t['id'] = id
    t['name'] = name
    t['description'] = desc
    t['due_date'] = date
    t['status'] = 'pending'
    tasks.append(t)
    id = id + 1
    print('Task added successfully!')

def deleteTask(taskId):
    global tasks
    for i in range(len(tasks)):
        if tasks[i]['id'] == taskId:
            tasks.pop(i)
            print('Task deleted!')
            return
    print('Task not found')

def updateTask(taskId, name, desc, date):
    global tasks
    for i in range(len(tasks)):
        if tasks[i]['id'] == taskId:
            tasks[i]['name'] = name
            tasks[i]['description'] = desc
            tasks[i]['due_date'] = date
            print('Task updated!')
            return
    print('Task not found')

def viewTasks():
    global tasks
    if len(tasks) == 0:
        print('No tasks found')
    else:
        for t in tasks:
            print('ID: ' + str(t['id']))
            print('Name: ' + t['name'])
            print('Description: ' + t['description'])
            print('Due Date: ' + t['due_date'])
            print('Status: ' + t['status'])
            print('---')

def completeTask(taskId):
    global tasks
    for i in range(len(tasks)):
        if tasks[i]['id'] == taskId:
            tasks[i]['status'] = 'completed'
            print('Task marked complete!')
            return

def searchTasks(keyword):
    global tasks
    results = []
    for t in tasks:
        if keyword in t['name'] or keyword in t['description']:
            results.append(t)
    return results

# Main menu
def menu():
    print('\n=== Task Manager ===')
    print('1. Add Task')
    print('2. View Tasks')
    print('3. Update Task')
    print('4. Delete Task')
    print('5. Complete Task')
    print('6. Search Tasks')
    print('7. Exit')
    choice = input('Enter choice: ')
    return choice

# Main program loop
def main():
    while True:
        c = menu()
        if c == '1':
            n = input('Enter task name: ')
            d = input('Enter description: ')
            dt = input('Enter due date (YYYY-MM-DD): ')
            addTask(n, d, dt)
        elif c == '2':
            viewTasks()
        elif c == '3':
            tid = int(input('Enter task ID: '))
            n = input('Enter new name: ')
            d = input('Enter new description: ')
            dt = input('Enter new due date: ')
            updateTask(tid, n, d, dt)
        elif c == '4':
            tid = int(input('Enter task ID to delete: '))
            deleteTask(tid)
        elif c == '5':
            tid = int(input('Enter task ID to complete: '))
            completeTask(tid)
        elif c == '6':
            kw = input('Enter search keyword: ')
            r = searchTasks(kw)
            print('Found ' + str(len(r)) + ' tasks')
            for task in r:
                print(task)
        elif c == '7':
            break

if __name__ == '__main__':
    main()
