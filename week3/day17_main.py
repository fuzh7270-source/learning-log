class Task:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


tasks = []

while True:

    print("1. Add task")
    print("2.Show tasks")
    print("3. Exit")

    choice = input("Choice:")

    if choice == "1":

        name = input("Enter task:")

        task = Task(name)

        tasks.append(task)

        print("Task added!")

    elif choice == "2":

        for task in tasks:
            task.show()

    elif choice == "3":

        print("Goodbye!")
        break

