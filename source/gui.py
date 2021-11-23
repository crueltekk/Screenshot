import PySimpleGUI as sg

dldriver = ''
load = False

layout = [
    [sg.Text('Choose Webdriver to use:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Combo(['firefox', 'chrome', 'edge', 'opera'], default_value='', key='webdriver', size=(20, 1))],
    [sg.Button('Start'), sg.Button('Quit')]
]


# Define Window

window = sg.Window('Screenshot a Website', layout)

event, values = window.Read()
print(event, values)
if event in (None, 'Quit'):
    window.close()

if event == 'Start':
    dldriver = values['webdriver']
    load = True