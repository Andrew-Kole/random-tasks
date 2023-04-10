def get_todos():
    with open("files/todos.txt", "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + "\n"

        todos = get_todos()

        todos.append(todo + "\n")

        with open('files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show") or user_action.startswith("display"):

        todos = get_todos()

        # new_todos = [item.strip(("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()


            new_item = input("Enter new todo: ")
            todos[number] = new_item + "\n"

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            todos.pop(number - 1)

            with open("files/todos.txt", "w") as file:
                todos = file.writelines(todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command")


print("bye")


