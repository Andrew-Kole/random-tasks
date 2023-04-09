while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + "\n"

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        # new_todos = [item.strip(("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        print(number)
        number = number - 1

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        new_item = input("Enter new todo: ")
        todos[number] = new_item + "\n"

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        todos.pop(number - 1)

        with open("files/todos.txt", "w") as file:
            todos = file.writelines(todos)
    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command")


print("bye")


