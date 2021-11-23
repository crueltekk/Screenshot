import PySimpleGUI as sg

# needed variables to pass over

dldriver = ''
load = False

# GUI layout

layout = [
    [sg.Text('Choose Webdriver to use:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Combo(['firefox', 'chrome', 'edge', 'opera'], default_value='', key='webdriver', size=(20, 1))],
    [sg.Button('Start'), sg.Button('Quit')]
]


# Define Window

window = sg.Window('Screenshot a Website', layout)

# Event listeners for buttons

event, values = window.Read()
print(event, values)
if event in (None, 'Quit'):
    window.close()

# Sets load to true so it starts downloading

if event == 'Start':
    dldriver = values['webdriver']
    load = True