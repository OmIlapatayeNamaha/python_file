def main():
    action = ['Add a new task','Read all the task', 'Remove a task','Clear list \n']
    for i, task in enumerate(action):
        print(f"{i+1}. {task.strip()}")

    choice = int(input("Enter your choice (1-4): "))

    match choice:
        case 1:
            add = todolist.addtask()
            print(second_question)
            main()
        case 2:
            print("Here is your to do list: \n")
            read =todolist.readtask()
            print("\n",second_question)
            main()
        case 3:
            remove = todolist.deletetask()
            print("\n",second_question)
            main()
        case 4:
            clear = todolist.clear_file(tasks.txt)
            print(second_question)
            main()