import functions
import FreeSimpleGUI as sgi

label = sgi.Text("Type in a to-do")
input_box = sgi.InputText(tooltip="Enter todo")
add_button = sgi.Button("Add")

window = sgi.Window('My To-Do App', layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()