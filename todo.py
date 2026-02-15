# ============================
#   TO-DO LIST APP (With Save)
# ============================

FILE_NAME = "tasks.txt"

# Load tasks from file when app starts
def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Main Program Starts
tasks = load_tasks()

while True:
    print("\n------ TO DO LIST MENU ------")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added & saved!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("⚠️ No tasks available.")
        else:
            print("\n📌 Your Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    # Remove Task
    elif choice == "3":
        if len(tasks) == 0:
            print("⚠️ No tasks to remove.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

            remove = int(input("Enter task number to remove: "))
            tasks.pop(remove - 1)
            save_tasks(tasks)
            print("🗑️ Task removed & saved!")

    # Exit
    elif choice == "4":
        print("👋 Goodbye Varun! Tasks are saved.")
        break

    else:
        print("❌ Invalid choice. Please enter 1-4.")
