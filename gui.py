import functions
import FreeSimpleGUI as sgi
import time

sgi.theme("DarkPurple4")

clock = sgi.Text('', key='clock')
label = sgi.Text("Type in a to-do")
input_box = sgi.InputText(tooltip="Enter todo", key="todo")
add_button = sgi.Button(size=10, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add Todo", key="Add")
list_box = sgi.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=[45, 10])
edit_button = sgi.Button("Edit")
complete_button = sgi.Button("Complete")
exit_button = sgi.Button("Exit")

window = sgi.Window('My To-Do App',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                    font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)

                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sgi.popup("Please select an item first")
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sgi.popup("Select an item to complete")
        case "Exit":
            break
        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sgi.WIN_CLOSED:
            break

print("Hello")
window.close()