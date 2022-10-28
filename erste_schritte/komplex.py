#komplex.py
import PySimpleGUI as sg

layout = [[sg.Text('Name'), sg.Input()], [sg.Text('Adresse'),
                                          sg.Input()],
          [sg.Text('Ort'), sg.Input()], [sg.Ok(), sg.Cancel()]]

sg.Window("Komplex", layout, element_justification='r').read()
