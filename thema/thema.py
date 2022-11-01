#thema.py
import PySimpleGUI as sg

sg.theme('Dark Gray 12')

left = [[sg.Text('Name'), sg.Input()], [sg.Text('Adresse'),
                                        sg.Input()],
        [sg.Text('Ort'), sg.Input()], [sg.Ok(), sg.Cancel()]]

right = [[sg.Multiline(size=(40, 5))]]

layout = [[
    sg.Column(left, element_justification='r'),
    sg.VSeparator(),
    sg.Column(right)
]]

sg.Window("Thema", layout).read()