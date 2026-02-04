import os
list_tasks = []
# Starts the program and list the functions avaliable
def initiate_program():
    os.system('cls')
    print("𝙏𝙖𝙨𝙠 𝙏𝙧𝙖𝙘𝙠𝙚𝙧")
    print("1 - Add task")
    print("2 - Update task")
    print("3 - Delete task")
    numero = int(input("Pick a function: "))
    match numero:
        case 1:
            add_task()
#Add, Update, and Delete tasks
def add_task():
    task = input("What tasks do you want to add: ")
    list_tasks.append(task)
    print(list_tasks)

#Mark a task as in progress or done

#List all tasks

#List all tasks that are done

#List all tasks that are not done

#List all tasks that are in progress

initiate_program()