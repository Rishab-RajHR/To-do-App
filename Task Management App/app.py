def task():
    tasks = []  # Empty list to store all tasks
    print("----WELCOME TO THE TASK MANAGEMENT APP----")

    # Taking total number of initial tasks
    total_task = int(input("Enter how many tasks you want to add = "))

    # Looping through the number of tasks
    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)  # FIXED: was task.append()

    print(f"Today's tasks are\n{tasks}")

    while True:
        # Menu-driven choices
        operation = int(input("\nEnter:\n1 - Add Task\n2 - Update Task\n3 - Delete Task\n4 - View Tasks\n5 - Exit\nYour choice: "))

        if operation == 1:
            # Add new task
            add = input("Enter task you want to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been successfully added.")

        elif operation == 2:
            # Update existing task
            updated_val = input("Enter the task name you want to update = ")
            if updated_val in tasks:
                new_task = input("Enter new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = new_task
                print(f"Task updated to '{new_task}'.")
            else:
                print("Task not found!")

        elif operation == 3:
            # Delete a task
            del_val = input("Enter task name you want to delete = ")
            if del_val in tasks:
                tasks.remove(del_val)  # simpler method
                print(f"Task '{del_val}' has been deleted.")
            else:
                print("Task not found!")

        elif operation == 4:
            # View all tasks
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            # Exit program
            print("Closing the program...")
            break

        else:
            print("Invalid operation. Please enter a number from 1 to 5.")

# Calling the function
task()
