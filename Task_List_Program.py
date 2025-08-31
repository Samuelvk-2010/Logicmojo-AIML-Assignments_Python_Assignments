
tasks = {
    "1.Wakeup": "Not Done",
    "2.Brush": "Not Done",
    "3.Bath": "Not Done",
    "4.Breakfast": "Not Done"
}

for key, value in tasks.items():
    print(f"{key}: {value}")
print("***************")

# print(" 1. Add Task \n 2. Show Task \n 3. Mark Task as Done \n 4. Exit")

# print(op)
i=0
while (i>=0):
    i=i+1
    print("Choose task list !!!")
    op = input(" 1. Add Task \n 2. Show Task \n 3. Mark Task as Done \n 4. Exit \n")
    match op:
        case '1':
            add_inp = input("Enter task name(without space)....")
            tasks[add_inp] = "Not Done"
            print(f"Task Added \n")
            # print(tasks)
        case '2':    
            print(f"Show Tasks")
            for key, value in tasks.items():
                print(f"{key}: {value}")
        case '3':
            task_upd = input("Enter exact task name from above list(without space) to be marked as Done....")
            tasks[task_upd] = "Done"
            print(f"Task {task_upd} updated \n")
            # print(tasks)
        case '4':    
            print(f"Exiting program \n")
            print(f"Final output below \n" )
            # print(tasks)
            for key, value in tasks.items():
                print(f"{key}: {value}")
            break
        case _:
            print(f"Invalid input {op} try again!! \n")
            continue


print("Program completed")
        
            

            

