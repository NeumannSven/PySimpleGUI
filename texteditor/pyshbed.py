#pyshbed.py
import PySimpleGUI as sg
from pprint import pprint

#sg.theme('DarkGray12')

menu = [[
    sg.Menu([['Datei', ['Öffnen', 'Speichern', 'Speichern unter ..', '---', 'Beenden']],
             ['Bearbeiten', ['Kopieren', 'Einfügen', 'Ausschneiden']],
             ['Anzeige'], ['Einstellungen'], ['Hilfe']],
            k='-MENUBAR-', font=("Courier New", 16),
            p=0)
]]

editor_area = [[sg.Multiline(size=(80, 40), key='-EDITOR_AREA-', font=("Courier New", 16), autoscroll=True)]]

layout = [[menu, editor_area]]

window = sg.Window("pySpaceBremen - Editor", layout)

loaded_file_name = ""


def readFile(file_path):
    file_content = ""
    with open(file_path) as file_handle:
        file_content = file_handle.read()
    return file_content 

def writeFile(file_path):
    with open(file_path, 'w') as file_handle:
        file_handle.write(window['-EDITOR_AREA-'].get())


while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Beenden':
        break
    elif event == 'Öffnen':
        file_name = sg.popup_get_file('Öffnen', no_window=True)
        if file_name:
            window['-EDITOR_AREA-'].update(readFile(file_name))
            loaded_file_name = file_name
        else:
            loaded_file_name = ''            
    elif event == 'Speichern unter ..':
        file_name = sg.popup_get_file('Speichern unter ..', save_as=True, no_window=True)
        if file_name:
            writeFile(file_name)
            loaded_file_name = file_name
        else:
            loaded_file_name = ''
    elif event == 'Speichern':
        if loaded_file_name:
            writeFile(loaded_file_name)
    elif event == 'Kopieren':
        selection = window['-EDITOR_AREA-'].Widget.selection_get()
        sg.clipboard_set(selection)
    elif event == 'Einfügen':
        window['-EDITOR_AREA-'].Widget.insert(window['-EDITOR_AREA-'].Widget.index('insert'), sg.clipboard_get())
    print(event, value)

window.close()
