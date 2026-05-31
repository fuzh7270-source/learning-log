tasks = []

def add_task():
    task = input("Enter task:")

    tasks.append(task)

    print("Task added!")

def show_tasks():

    print(tasks)

def delete_task():
     
     try:
         print(tasks)
         
         index = int(input("Enter task number:"))
         
         tasks.pop(index)

     except:
         print("Invalid task number.")

while True:

    print("1. Add task")

    print("2. Show tasks")

    print("3. Delete task")

    print("4. Exit")

    choice = input("Choose:")

    if choice == "1":
        add_task()

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        delete_task()

    elif choice == "4":
        print("Goodbye!")
        break         