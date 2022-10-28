# Erste Schritte

```python
#einfach.py
import PySimpleGUI as sg

sg.Window("Einfaches Fenster", [[]], size=(300, 100)).read()
```


```python
#anordnen.py
import PySimpleGUI as sg

layout = [[sg.Text('Hallo Welt!')], [sg.Button('Ok')]]

sg.Window("Anordnen", layout, size=(300, 100)).read()
```

```python
#komplex.py
import PySimpleGUI as sg

layout = [
    [sg.Text('Name'), sg.Input()],
    [sg.Text('Adresse'), sg.Input()],
    [sg.Text('Ort'), sg.Input()],
    [sg.Ok(), sg.Cancel()]
]

sg.Window("Komplex", layout, element_justification='r').read()
```

```python
#komplexer.py
import PySimpleGUI as sg

left = [
    [sg.Text('Name'), sg.Input()],
    [sg.Text('Adresse'), sg.Input()],
    [sg.Text('Ort'), sg.Input()],
    [sg.Ok(), sg.Cancel()]
]

right = [
    [sg.Multiline(size=(40, 5))]
]

layout = [
    [sg.Column(left, element_justification='r'), sg.VSeparator(), sg.Column(right)]
]

sg.Window("Komplexer", layout).read()
```