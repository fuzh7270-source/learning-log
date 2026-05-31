tasks = []

while True:

    print("1. Add task")
    print("2. Show tasks")
    print("3. Exit")
    print("4. Delete task")
    choice = input("Choose:")
    if choice == "1":
        task = input("Enter task:")
        tasks.append(task)

        print("Task added!")

    elif choice == "2":
        print(tasks)

    elif choice == "3":
        print("Goodbye!")
        break

    elif choice == "4":
        try:

            print(tasks)
            index = int(input("Enter task number:"))
        
            print("Invalid task number.")
        
            tasks.pop(index)
            print("Task deleted!")

        except:
            print("Invalid task number.")

    else:
        print("Invalid choice")




