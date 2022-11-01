#menu.py
import PySimpleGUI as sg

sg.theme('Dark Gray 12')

left = [
    [sg.Menu([
        ['File', ['Exit']],
        ['Edit', ['Copy','Insert','Settings']],
        ['View'],
        ['Help']], k='-MENUBAR-', p=0)
    ]
]

right = [[sg.Multiline(size=(80, 40))]]

layout = [[left, right]]

window = sg.Window("Menue", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event, value)

window.close()
