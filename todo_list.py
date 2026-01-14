tasks = []

while True:
    print("\nTo-Do List")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added")

    elif choice == "2":
        if not tasks:
            print("No tasks yet")
        else:
            for i, task in enumerate(tasks, start=1):
                print(i, task)

    elif choice == "3":
        number = int(input("Enter task number to remove: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Task removed")
        else:
            print("Invalid number")

    elif choice == "4":
        print("Bye 👋")
        break

    else:
        print("Invalid choice")
