while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            # new_todos = [item.strip(("\n") for item in todos]

            for index, item in enumerate(todos):
                item = item.strip("\n")
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("The number of todo to edit: "))
            number = number - 1
            new_item = input("Enter new todo")
            todos[number] = new_item
        case 'complete':
            number = int(input("Which item number do you wish to complete"))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Unknown command")

print("bye")


