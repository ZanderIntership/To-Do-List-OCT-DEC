📝 Task Manager (Console Application)
Overview

This is a simple command-line Task Manager written in Python.
It allows users to:

Create multiple tasks interactively

Add a name and description for each task

Review all tasks at the end

Optionally export the tasks to a .txt file 📄

This project is ideal for learning:

Loops and input validation

Lists and dictionaries

File handling in Python

Features

✅ Prevents empty task names

🔁 Allows adding unlimited tasks

📋 Displays all tasks in a clear format

💾 Optional export to a .txt file

🛡️ Basic input validation (Y/N prompts)

Requirements

Python 3.8+

No external libraries required

How to Run

Save the script as task_manager.py

Open a terminal or command prompt

Run:

python task_manager.py

How It Works
1. Add Tasks

You’ll be prompted to enter:

Task Name (required)

Task Description (optional)

Example:

Task Name: Buy groceries
Task Description: Milk, bread, eggs

2. Continue or Stop

After each task, you choose:

Continue? (Y/N):


Y → add another task

N → finish and review tasks

Task Summary Output

Once finished, all tasks are displayed:

--- Tasks ---

Task 1
Name: Buy groceries
Desc: Milk, bread, eggs

Export to TXT File 📄

After reviewing tasks, you’ll be asked:

Do you want to save these tasks to a .txt file? (Y/N):


If you choose Y:

You can enter a custom filename

The file is saved in the same directory as the script

Example file content:

Task Manager Export
===================

Task 1
Name: Buy groceries
Desc: Milk, bread, eggs
