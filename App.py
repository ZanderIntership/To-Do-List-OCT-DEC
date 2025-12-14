tasks = []
task_count = 1

while True:
    print("\nWelcome to the Task Manager application")
    print(f"Please enter details for Task {task_count}")


    while True:
        name = input("Task Name: ").strip()
        if name:
            break
        print("Task Name cannot be empty. Please try again.")


    desc = input("Task Description: ").strip()

    tasks.append({"name": name, "desc": desc})
    task_count += 1


    while True:
        choice = input("Continue? (Y/N): ").strip().lower()
        if choice in ("y", "n"):
            break
        print("Please enter Y or N.")

    if choice == "n":
        break


print("\n--- Tasks ---")
if not tasks:
    print("No tasks created.")
else:
    for i, task in enumerate(tasks, start=1):
        print(f"\nTask {i}")
        print(f"Name: {task['name']}")
        print(f"Desc: {task['desc']}")


if tasks:
    while True:
        export_choice = input("\nDo you want to save these tasks to a .txt file? (Y/N): ").strip().lower()
        if export_choice in ("y", "n"):
            break
        print("Please enter Y or N.")

    if export_choice == "y":
        filename = input("Enter a filename (e.g., tasks.txt): ").strip()
        if not filename:
            filename = "tasks.txt"
        if not filename.lower().endswith(".txt"):
            filename += ".txt"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("Task Manager Export\n")
                f.write("===================\n\n")
                for i, task in enumerate(tasks, start=1):
                    f.write(f"Task {i}\n")
                    f.write(f"Name: {task['name']}\n")
                    f.write(f"Desc: {task['desc']}\n")
                    f.write("\n")

            print(f"\nSaved successfully to: {filename}")
        except OSError as e:
            print(f"\nCould not save file: {e}")
