tasks = []
task_count = 1

while True:
    print("\nWelcome to the Task Manager application")
    print(f"Please enter details for Task {task_count}")

    # Task name (required)
    while True:
        name = input("Task Name: ").strip()
        if name:
            break
        print("Task Name cannot be empty. Please try again.")

    # Task description (optional)
    desc = input("Task Description: ").strip()

    tasks.append({"name": name, "desc": desc})
    task_count += 1

    # Continue prompt (validated)
    while True:
        choice = input("Continue? (Y/N): ").strip().lower()
        if choice in ("y", "n"):
            break
        print("Please enter Y or N.")

    if choice == "n":
        break

# Print results
print("\n--- Tasks ---")
if not tasks:
    print("No tasks created.")
else:
    for i, task in enumerate(tasks, start=1):
        print(f"\nTask {i}")
        print(f"Name: {task['name']}")
        print(f"Desc: {task['desc']}")

