import PySimpleGUI as sg

sg.theme('LightBrown9')

layout = [[sg.Text('Enter Member ID:'), sg.Input(key='-IN-')],
          [sg.Text('VGA Student Details', key='-OUT-')],
          [sg.Button('OK'), sg.Button('Exit')]]


window = sg.Window('Visionary Student Database', layout)

while True:
    event, values =  window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break

    window['-OUT-'].update(values['-IN-'])

window.close()


