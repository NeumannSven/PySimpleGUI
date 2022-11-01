#menu.py
import PySimpleGUI as sg

sg.theme('Gray 12')

left = [[
    sg.Menu([['File', ['Open', 'Exit']],
             ['Edit', ['Copy', 'Insert', 'Settings']], ['View'], ['Help']],
            k='-MENUBAR-',
            p=0)
]]

right = [[sg.Multiline(size=(80, 40), key='-EditWindow-', autoscroll=True)]]

layout = [[left, right]]

window = sg.Window("Menü", layout)


def fileOpen():
    filename = sg.popup_get_file('Open File')
    text = ''
    if filename == None:
        return text

    with open(filename) as f:
        for line in f.readlines():
            text += line
    return text


while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Open':
        window['-EditWindow-'].update(fileOpen())

    print(event, value)

window.close()
