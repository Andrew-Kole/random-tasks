"""
Create a desktop GUI program that gets feet and inches from the user and outputs the results in meters.
"""

import PySimpleGUI as sg
import modules.func_for_day17task1 as ff17

label1 = sg.Text("Enter feet")
input_box1 = sg.InputText(tooltip="Enter feet", key="feet")

label2 = sg.Text("Enter inches")
input_box2 = sg.InputText(tooltip="Enter inches", key="inches")

convert_button = sg.Button("Convert")
result_label = sg.Text(key="result", text_color="red")

window = sg.Window("Convertor", layout=[[label1, input_box1],
                                        [label2, input_box2],
                                        [convert_button, result_label]])

while True:
    event, values = window.read()
    print(event, values)
    match event:
        case "Convert":
            feet= values["feet"]
            inches = values["inches"]
            parsed_feet, parsed_inches = ff17.parse(feet, inches)
            result = ff17.convert(parsed_feet, parsed_inches)
            window["result"].update(value=result)
        case sg.WIN_CLOSED:
            break



window.close()

