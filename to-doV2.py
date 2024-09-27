# Personal use python to-do list.
# TODO: Create file on desktop if file does not already exist.

#!!!!!!!!!!!!!!!!!!!
# TODO: Implement a failsafe so that if the application is force-closed, it saves the state. Maybe to circumvent this, save state in between update!
# TODO: Switch system command "cls" to "clear" and vice versa based on running OS for cross platform compatibility.


# TODO: Make the options look nicer/cleaner.
# TODO: Package file into an executable.
# TODO: Initialize to a remote server? Maybe purchase a raspberry pi that can connect to and from your to do lists.


import os

# Initializing list.
listFile = open(r"C:\Users\aa12m\OneDrive\Desktop\Coding\simpleTODO\test.txt", "r")
tasks = (listFile.read())
tasks = tasks.splitlines()

# Updates file based on current modified list.
def updateFile() :

    global tasks
    with open(r"C:\Users\aa12m\OneDrive\Desktop\Coding\simpleTODO\test.txt", "w") as f:

        for index, tasks in enumerate(tasks):
            f.write(f"{tasks}\n")

    print("File updated.")

# TODO: Why is this here? Check later.
status = (f"Awaiting task.")


# Adds a new task.
def newTask() :
    global status

    addedTask = input("Input a task to add:\nPress enter to return.\n> ")
    if addedTask == "" :
        clearTerminal()
        return
    else :
        tasks.append(addedTask)
        status = (f'Task "{addedTask}" has been added.')

    clearTerminal()


# Deletes a task.

# Checks if there are any tasks.
# If there aren't, it returns with listTask.
# If there are, it displays the tasks.
def deleteTask() :
    global status

    if bool(tasks) == False :
        listTask(False)
        return
    
    listTask(False)

    print('\nPress enter to return.')
    deletedTask = input("Input a task # to delete:\n> ")
# Checks if the string is a digit, and if its not, it will restart deleteTask.

    if deletedTask == "" :
        return

    if deletedTask.isdigit() == True :
        deletedTask = int(deletedTask)

    elif deletedTask.isdigit() == False :
        status = ("Invalid task ID.")
        return


    if deletedTask < len(tasks) :
        status = (f'Task #{deletedTask} "{tasks[deletedTask-1]}" has been deleted.')
        tasks.pop(deletedTask-1)
    else :
        status = ("Invalid task ID.")
        


def listTask(standAlone) :
    global status
    if not tasks :
        status = ("There are currently no tasks.")
        return
    

    else :
        clearTerminal()
        print("Current tasks:\n")
        for taskNum, currentTask in enumerate(tasks) :
            print(f'Task #:{taskNum+1} "{currentTask}"')

    if standAlone == True :
        doesReturn = input('\nPress enter to return.')
        if type(doesReturn) == str :
            return



                        
        
def clearTerminal() :
    os.system('cls')


while True :

    clearTerminal()
    print(" ______   ______           _____     ______    ")
    print("/\__  _\ /\  __ \         /\  __-.  /\  __ \   ")
    print("\/_/\ \/ \ \ \/\ \        \ \ \/\ \ \ \ \/\ \  ")
    print("   \ \_\  \ \_____\        \ \____-  \ \_____\ ")
    print("    \/_/   \/_____/         \/____/   \/_____/ ")
    print("                                               ")

    print("\nPlease select one of the following options:")
    print("-------------------------------------------")
    print("1. Add a new task.")
    print("2. Delete a task.")
    print("3. List tasks.")
    print("4. Quit.")
    print(f"\nStatus: {status}")

    option = (input("> "))
    

    if option == "1" :
        newTask()

    elif option == "2" :
        deleteTask()
        clearTerminal()

    elif option == "3" :
        listTask(True)
        clearTerminal()

    elif option == "4" :
        clearTerminal()
        updateFile()
        print("Terminated to-do list.")
        break

    else :
        status = ("Invalid command")