#editor.py
import PySimpleGUI as sg

#sg.theme('Dark Gray 12')

left = [[
    sg.Menu([['File', ['Open', 'Exit']],
             ['Edit', ['Copy', 'Insert', 'Settings']], ['View'], ['Help']],
            k='-MENUBAR-',
            p=0)
]]

right = [[
    sg.Slider(enable_events=True, key="Slider"),
    sg.Button('Ok'),
    sg.Spin((1, 4, 6, 9), enable_events=True, key="Spin")
]]

layout = [[left, right]]

window = sg.Window("Menue", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Spin':
        window['Slider'].update(value['Spin'])
    print(event, value)

window.close()
