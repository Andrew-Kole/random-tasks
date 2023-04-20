import modules.functions as fs
import PySimpleGUI as sg
import time
import os

if not os.path.exists("C:/Users/Acer/PycharmProjects/pythonProject/files/todos.txt"):
    with open("C:/Users/Acer/PycharmProjects/pythonProject/files/todos.txt", "w") as file:
        pass

sg.theme("Black")

label_time = sg.Text("", key="clock")
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=2, image_source='C:/Users/Acer/PycharmProjects/pythonProject/pictures/add.png', mouseover_colors="LightBlue",
                       tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=fs.get_todos(),
                      key="todos",
                      enable_events=True,
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(image_source="C:/Users/Acer/PycharmProjects/pythonProject/pictures/complete.png", mouseover_colors="LightBlue",
                            tooltip="Complete", key="Complete")
exit_button = sg.Button("Exit")

window = sg.Window("My to-do app",
                   layout=[[label_time],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))

while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    print(1, values)
    print(2, event)
    print(3, values["todos"])
    match event:
        case "Add":
            todos = fs.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            fs.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = fs.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                fs.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!",
                         font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = fs.get_todos()
                todos.remove(todo_to_complete)
                fs.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please select an item first!",
                         font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break

window.close()
