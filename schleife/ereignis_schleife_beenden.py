#ereignis_schleife_beenden.py
import PySimpleGUI as sg

sg.theme('Dark Gray 12')

left = [[sg.Text('Name'), sg.Input()],
        [sg.Text('Adresse'), sg.Input(key="Address")],
        [sg.Text('Ort'), sg.Input()], [sg.Ok(), sg.Cancel()]]

right = [[sg.Multiline(size=(40, 5))]]

layout = [[
    sg.Column(left, element_justification='r'),
    sg.VSeparator(),
    sg.Column(right)
]]

window = sg.Window("Ereignis Schleife Beende", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print(event, value)

window.close()
