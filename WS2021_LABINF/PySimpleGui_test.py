# %%
#Installation von PySimpleGUI - einfach folgenden Befehl auskommentieren
#!pip install PySimpleGUI

import PySimpleGUI as sg

#%%
#BEISPIEL 1
sg.Window(title='Mein erstes GUI-Programm', layout=[[]], size=(600,100), margins=(100, 50)).read()


#%%
#BEISPIEL 2

#Liste aller Themes für das Fenster anzeigen
#theme_list = sg.theme_list()
#print(theme_list)

sg.theme('SandyBeach')

#Sehr einfaches Fenster
#returnwerte mit automatischen Keys, die zugeordnet werden können
layout = [[sg.Text('Name, Alter und Größe eingeben:')],                 #[[0,0],
          [ sg.Text('Name', size=(6,1)), sg.InputText()],               # [(1,0), (1,1)],
          [sg.Text('Alter', size=(6,1)), sg.InputText()],               # [(2,0), (2,1)],
          [sg.Text('Größe', size=(6,1)), sg.InputText()],
          [sg.Text('Geburtstag', size=(10,1)), sg.Text('', size=(15,1)), sg.CalendarButton('Auswählen')],
          [sg.Submit(), sg.Cancel()]
         ]

window = sg.Window(title='Mein zweites GUI-Programm', layout=layout)
event, values = window.read()
window.close()

#Input schaut wie eine einfach Liste aus
print(event, values)

#%%
#Taschenrechner GUI
import PySimpleGUI as sg

#GUI Layout
layout = [[sg.Text('', size=(15,1), font=('Arial', 18), text_color='red', key='input')],
          [sg.ReadFormButton('c'), sg.ReadFormButton('<<')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('/')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('*')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')]
          ]

window = sg.Window('Taschenrechner', layout=layout, default_button_element_size=(5,2), auto_size_buttons=False)

#Ergebnis
result = ''

while True:
    #Button Values
    button, value = window.read()

    print(button, value)

    #Fenster schließen
    if button == 'Quit' or button == None:
        break                                   # aus endlosschleife entweichen

    elif button == 'c':
        result = ''

    elif button == '<<':
        result = result[:-1]

    elif button == '=':
        try:
            result = eval(result)          #Berechnung innerhalb des strings result wird durchgeführt
            result = str(round(result,3))
        except ZeroDivisionError:
            result = result[:-1]
            print('Division durch zero')

    else:
        result = result + button

    window['input'].update(result)


#%%
import PySimpleGUI as sg

layout = [[sg.Text('Liste von BuiltIn-Themes')],
          [sg.Text('Wähle ein Theme aus und sieh dir die Demo an')],
          [sg.Listbox(values=sg.theme_list(),
                      size=(22, 12),
                      key='LIST',
                      enable_events=True)],
          [sg.Button('Exit')]
          ]

window = sg.Window('Theme Demo', layout=layout)

#Event Schleife
while True:
    event, values = window.read()

    #if event == 'Quit' or button == None:
    if event in (None, 'Exit'):
        break

    #print(values)
    #print(values['LIST'])
    #print(values['LIST'][0])
    sg.theme(values['LIST'][0])

    #DEMO Fenster mit ausgewählten Theme
    sg.popup_get_text(f'Das ist {values["LIST"][0]}')

# %%
