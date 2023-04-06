while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('files/todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            new_todos = []

            for item in todos:
                new_item = item.strip("\n")
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
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
        case 'exit' :
            break
        case _:
            print("Unknown command")

print("bye")


