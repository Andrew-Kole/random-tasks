todos = []

while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            number = int(input("The number of todo to edit: "))
            number = number - 1
            new_item = input("Enter new todo")
            todos[number] = new_item
        case 'exit' :
            break
        case _:
            print("Unknown command")

print("bye")


