while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or "new" in user_action:
        todo = user_action[4:] + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action or "display" in user_action:

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip(("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        number = number - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        new_item = input("Enter new todo: ")
        todos[number] = new_item + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open("files/todos.txt", "w") as file:
            todos = file.writelines(todos)
    elif 'exit' in user_action:
        break
    else:
        print("Unknown command")


print("bye")


