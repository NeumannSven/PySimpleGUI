import PySimpleGUI as sg

layout = [[sg.Text('Hallo Welt!')], [sg.Button('Ok')]]

sg.Window("Anordnen", layout).read()
