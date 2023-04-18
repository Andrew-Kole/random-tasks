import modules.functions as fs
import PySimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My to-do app",
                   layout=[[label], [input_box, add_button]],
                   font=("Helvetica", 20))

while True:
    event, values= window.read()
    print(values)
    print(event)
    match event:
        case "Add":
            todos = fs.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fs.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()
