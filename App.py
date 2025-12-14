
TasksName = []
TaskDesc = []
TaskCount = 1


Ending = False

while Ending == False:
    print("Welcome to the Task Manager application\n")

    print(f"Please Enter Details For Task {TaskCount}")
    TaskName = input("Task Name : ")
    TaskDescription = input("Task Description : ")
    # -------------
    TasksName.append(TaskName)
    TaskDesc.append(TaskDescription)

    Input = input("Continue? (Y/N) : ")

    if Input == "Y" or Input == "y":
        Ending = False
        TaskCount += 1
    else:
        Ending = True

for I in range(len(TasksName)):
    print(f"Task {I + 1}\n{TasksName[I]} : {TaskDesc[I]} \n")
