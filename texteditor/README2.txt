# Editor

```python
#editor.py
import PySimpleGUI as sg

sg.theme('Dark Gray 12')

left = [
    [sg.Menu([
        ['File', ['Open','Exit']],
        ['Edit', ['Copy','Insert','Settings']],
        ['View'],
        ['Help']], k='-MENUBAR-', p=0)
    ]
]

right = [[sg.Multiline(size=(80, 40))]]

layout = [[left, right]]

window = sg.Window("Menü", layout)


window.close()
```





Hallo Welt! 42




# Editor

```python
#editor.py
import PySimpleGUI as sg

sg.theme('Dark Gray 12')

left = [
    [sg.Menu([
        ['File', ['Open','Exit']],
        ['Edit', ['Copy','Insert','Settings']],
        ['View'],
        ['Help']], k='-MENUBAR-', p=0)
    ]
]

right = [[sg.Multiline(size=(80, 40))]]

layout = [[left, right]]

window = sg.Window("Menü", layout)

while True:
    event, value = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Open':
        print(sg.FileBrowse())
    print(event, value)

window.close()
```