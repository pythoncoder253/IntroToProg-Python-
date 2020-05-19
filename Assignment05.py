# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#               When the program starts, load each " row" of data
#               in "ToDoToDoList.txt" into a python Dictionary.
#               Add each dictionary "row" to a python list "table"
# ChangeLog: (who,When,What):
# RRoot,1.1.2030,Created started script
# Binh Nguyen, 5/17/2020 Add code to complete assignment 5
#-------------------------------------------------------------------------#

# -- Data -- #
# declare variables and constants
menu = ''' 
            Menu of options
            1) Show current task
            2) Add a new task
            3) Remove an existing task
            4) Save task
            5) Exit
             '''
todolist = open("H:\Binh\PythonClass\Assignment05\ToDoList.txt", "r") # An object that represents a file
table = [] # A list that acts as a 'table' of rows
dicRow = {} # A row of data separated into elements of a dictionary {Task,Priority}

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

for item in todolist:
    row = item.split(',')
    dicRow = {'Task':row[0], 'Priority':row[1].strip()}
    table.append(dicRow)
todolist.close()

# -- Input/Output -- ##
# Step 2 - Display a menu of choices to the user

while (True):
    print(menu)
    choice = int(input('Which option you would like to perform? '))
    print('\nYour current tasks:\n')

# Step 3 - Show the current items in the table
    if choice == 1:
        print('Task' + ' ' + 'Priority')
        for dicRow in table:
            print(dicRow['Task'] + ' = ' + dicRow['Priority'])

# Step 4 - Add a new items to the list/Table
    if choice == 2:
        task = input('Enter a task: ')
        for dicRow in table:
            if task == dicRow['Task']:
                print('Task already exist!')
                break
        else:
            priority = input('Enter a priority: ')
            dicRow = {'Task': task, 'Priority': priority}
            table.append(dicRow)
            print('Your Task: ', dicRow['Task'], 'is added.')

# Step 5 - Remove a new item from the list/Table
    if choice == 3:
        removeTask = input('\nWhat do you want to remove?')
        if removeTask not in dicRow['Task']:
            print('Task does not exist')
            continue
        for dicRow in table:
            if removeTask in dicRow['Task']:
                table.remove(dicRow)
                print('\nTask', removeTask, 'has been removed !')
                print('\nThis is your current Task')
                print('Task', '', 'Priority')
                for dicRow in table:
                    print(dicRow['Task'] + ' = ' + dicRow['Priority'])

# Step 6 - Save task to the ToDoList.txt file
    if choice == 4:
        todolist = open("H:\Binh\PythonClass\Assignment05\ToDoList.txt", 'w')
        print('Your task is saved!')
        for dicRow in table:
            todolist.write(dicRow['Task'] + ',' + dicRow['Priority'] + '\n')
            print(dicRow['Task'])
        todolist.close()

# Step 7 - Exit program
    if choice == 5:
        input("Enter to exit!!")
        break








