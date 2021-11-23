import PySimpleGUI as sg

# needed variables to pass over

dldriver = ''
load = False
links = ''

# GUI layout

layout = [
    [sg.Text('Choose Webdriver to use:', size=(20, 1), font='Lucida', justification='left')],
    [sg.Combo(['firefox', 'chrome', 'edge', 'opera'], default_value='', key='webdriver', readonly=True, size=(20, 1))],
    [sg.Input(default_text='Enter webadress you want to screenshot here', key='adress')],
    [sg.Button('Start', button_color='Green', bind_return_key=True), sg.Button('Quit', button_color='Red')]
]


# Define Window

window = sg.Window('Screenshot a Website', layout, size=(320, 130))

# Event listeners for buttons

event, values = window.Read()
print(event, values)
if event in ('Quit'):
    window.close()

# Sets load to true so it starts downloading

if event == 'Start':
    dldriver = values['webdriver']
    links = values['adress']
    load = True