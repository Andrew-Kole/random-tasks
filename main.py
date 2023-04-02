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
                row = f"{index + 1}-{item}"
                print(row)
            print(f"Length is {index + 1}")
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


