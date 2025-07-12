import FreeSimpleGUI as fg

def convert(feet, inch):
    meters = feet * 0.3048 + inch * 0.0254
    return meters

label_feet = fg.Text("Enter feet")
input_feet = fg.InputText(tooltip="Enter feet", key="feet")

label_inches = fg.Text("Enter feet")
input_inches = fg.InputText(tooltip="Enter feet", key="inches")

convert_button = fg.Button("Convert")
output_label = fg.Text("", key="output")

window = fg.Window("Convertor", [[label_feet, input_feet],
                                 [label_inches, input_inches],
                                 [convert_button, output_label]])

while True:
    event, values = window.read()
    feet_value = float(values["feet"])
    inches = float(values["inches"])

    result = convert(feet_value, inches)
    window["output"].update(value=f"{result} m", text_color="white")

window.close()