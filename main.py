def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add") or user_action.startswith("new"):
        todo = user_action[4:] + "\n"

        todos = get_todos("files/todos.txt")

        todos.append(todo + "\n")

        write_todos('files/todos.txt', todos)

    elif user_action.startswith("show") or user_action.startswith("display"):

        todos = get_todos("files/todos.txt")

        # new_todos = [item.strip(("\n") for item in todos]

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos("files/todos.txt")


            new_item = input("Enter new todo: ")
            todos[number] = new_item + "\n"

            write_todos('files/todos.txt', todos)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("files/todos.txt")

            todos.pop(number - 1)

            write_todos('files/todos.txt', todos)
        except IndexError:
            print("There is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Unknown command")


print("bye")


