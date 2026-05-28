tasks = []

while True:

        print("1. Add task")
        print("2. Show tasks")
        print("3. Exit")
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
        else:
                print("Invalid choice")
                    