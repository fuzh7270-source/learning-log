tasks = []

def add_task():
    task = input("Enter task:")
    tasks.append(task)
    print("Task added successfully")

def show_tasks():
    print(tasks)

def save_tasks():
    file = open("tasks.txt","w")
   
    for task in tasks:
        file.write(task + "\n")
   
    file.close()
    print("Tasks saved ")

def load_tasks():
    file = open("tasks.txt","r")
   
    for line in file:
        tasks.append(line.strip())
   
    file.close()
    print("Tasks Loaded")

while True:
    print("1. Add task")
    print("2. Show tasks")
    print("3. Save tasks")
    print("4. Load tasks")
    print("5. Exit")

    choice = input("Choose:")
   
    if choice == "1":
        add_task()
    elif choice =="2":
        show_tasks()
    elif choice =="3":
        save_tasks()
    elif choice =="4":
        load_tasks()
    elif choice =="5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")

