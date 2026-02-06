import os
#Use class for this
list_tasks = [{"Task" :"Clean the house",
              "ID" : 1},
              {"Task" : "Do homework",
               "ID" : 2 },
               {"Task" : "Study french",
               "ID" : 3}]

# Starts the program and list the functions avaliable
def initiate_program():
    os.system('cls')
    print("𝙏𝙖𝙨𝙠 𝙏𝙧𝙖𝙘𝙠𝙚𝙧")
    print("1 - Add task")
    print("2 - Update task")
    print("3 - Delete task")
    print("7 - Exit")

    number = int(input("Pick a function: "))
    match number:
        case 1:
            add_task()
    match number:
        case 2:
            update_task()
    match number:
        case 3:
            delete_task()
    match number:
        case 7:
            exit()


#Add, Update, and Delete tasks
def add_task():
    task_added = input("What task do you want to add: ")
    list_tasks.append({"Task" : task_added, "ID" : (len(list_tasks)+1)})
    print(list_tasks)
    input("Press any key to return to the menu.")
    initiate_program()

def update_task():
    task_updated = input("What task do you want to update: ")
    list_tasks
    input("Press any key to return to the menu.")
    initiate_program()

def delete_task():
    print("Tasks:", list_tasks)
    task_deleted = input("What task do you want to delete: ")
    if task_deleted in list_tasks:
        list_tasks.remove(task_deleted)
    else:
        print("Task not found")
    input("Press any key to return to the menu.")
    initiate_program()

#Mark a task as in progress or done

#List all tasks

#List all tasks that are done

#List all tasks that are not done

#List all tasks that are in progress

initiate_program()