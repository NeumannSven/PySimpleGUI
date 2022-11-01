# Ereignis Schleife

```python
#ereignis.py
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

sg.Window("Ereignis", layout).read()

while True:     # The Event Loop
    event, value = window.read()
    if event in (sg.WIN_CLOSED, 'EXIT'):            # quit if exit button or X
        break
    if event == 'SEND':
        query = value['-QUERY-'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query), flush=True)

window.close()
```

```python
#ereignis_schleife.py
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

window = sg.Window("Ereignis Schleife", layout)

while True:
    event, value = window.read()
    print(event, value)
```



```python
#ereignis_schleife_beenden.py
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

window = sg.Window("Ereignis Schleife Beende", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print(event, value)

window.close()
```
