"""
Lotto spielen mit Guthaben (GUI-Version)
"""
from collections import Counter
import random
from tkinter import Message
import PySimpleGUI as sg

#%%
def user_numbers(input_gui):
    """
    Einlesen der Userzahlen
     - check ob Zahl ist zwischen 1-45
     - check ob alle Zahlen eindeutig sind
     - check ob 6 eindeutige Zahlen in Liste sind
    :return: Liste mit 6 eindeutigen Zahlen [1,2,3,4,5,6]
    """
    # Beginn: Array sicherheitshalber leeren
    user_nr = []            # meine Zahlen
    # Beginn: Message-Sting sicherheitshalber leeren
    message_zahlentest = ""

    #testzahlen = '11 22 33 44 1 6'          # Testzahlen um muehsame Eingaben zu umgehen
    #tipp = testzahlen.split(' ')
    tipp = input_gui.split(' ') 
    
    #Checks durchführen
    for zahl in tipp:
        #Anpassung, negative Zahlen wurden nicht als Zahlen erkannt
        if zahl.strip('-').isnumeric():
            #Wenn Zahl den Bedingungen entspricht zum Array hinzufügen
            if 1 <= int(zahl) <=45:
                user_nr.append(int(zahl))
            else:
                #Fehlerausgabe wenn Zahl nicht im Bereich ist
                message_zahlentest = message_zahlentest + str(zahl) + ': Alle Zahlen muessen zwischen 1 und 45 sein!\n'
                break
        else:
            #Fehlerausgabe wenn es keine Zahl ist
            message_zahlentest += str(zahl)
            message_zahlentest += ': Es wurde keine Zahl eingegeben! \n'
            break
    if len(set(user_nr))!= 6:
        #Fehlerausgabe, dass es sich nicht um 6 eindeutige Zahlen handelt.
        message_zahlentest += "Bei Ihrer Eingabe handelt es sich nicht um 6 eindeutige Zahlen.\nBitte nochmals versuchen.\n"
    # Wenn alle Pruefungen ok, dann befuelle den entsprechenden Text
    if message_zahlentest == "":
        message_zahlentest = "OK. Zahlen entsprechen den Bedingungen."
    # Egal ob Zahlen passend oder nicht, liefere das Ergebnis mit passenden Text an das Unterprogramm zurueck
    return user_nr, message_zahlentest

#%%
# Unterprogramm: Generiere Lottozahlen
def computer_numbers():
    """
    Generiert Computerzahlen
    :return: Liste mit 6 zufälligen eindeutigen Zahlen im Bereich von 1-45
    """
    # Generiere 6 eindeutige Zahlen und sortiere diese aufsteigend
    return sorted(random.sample(range(1,46), 6))


#%%
# Unterprogramm: Zahlen vergleichen
def compare(userNumber, computerNumbers):
    """
    Vergleichen der beiden Listen mit set().interscetion und die Länge davon zurückgeben
    :param userNumber: Ergebnis von Funktion user_numbers() -> Liste
    :param computerNumbers: Ergebnis von Funktion computer_numbers() -> Liste
    :return: Anzahl der gleichen Zahlen (Ergebnis)
    """
    #Vergleiche die Computerzahlen und die Zahlen des Benutzers
    matching=set(userNumber).intersection(set(computerNumbers))
    #Gib die Schnittmenge und die Anzahl der Zahlen in der Schnittmenge zurueck
    return len(matching)

#%%
# Unterprogramm: Ziehungen
def ziehungen(guthaben,tippkosten,message_ziehung):
    ziehungsergebnis = []
    ziehungsCount = 0

    #Wiederhole die Ziehung so oft, bis das Guthaben verbraucht ist
    while guthaben >= tippkosten:
        #Buche pro Tipp etwas vom Guthaben ab
        guthaben -= tippkosten
        # Zaehlen der Ziehungen
        ziehungsCount += 1
        #Erzeuge Lottozahlen im Unterprogramm
        cpu_numbers = computer_numbers()
        #Vergleiche Userzahlen mit dem Lottozahlen im Unterprogramm
        ergebnis = compare(usernum,cpu_numbers)
        #Frage ab, wenn das Set leer ist (Extra, weil leeres Set anders verhaelt)
        if ergebnis==0:
            #Schreibe eine 0 ins Array
            ziehungsergebnis.append(0)
        else:
            #Schreibe das Ziehungsergebnis ins Array
            ziehungsergebnis.append(ergebnis)
            # Buche Guthaben auf, wenn ein 3er oder hoeher gewonnen wird
            if ergebnis == 3:
                guthaben += 5.5
            if ergebnis == 4:
                guthaben += 55
            if ergebnis == 5:
                guthaben += 2500     
            # Zusatz bei einen 6er: 1 Mio Euro und Ende des Spiels 
            if ergebnis == 6:
                # Extra Text, wenn ein 6er!!
                guthaben += 1000000
                message_ziehung = message_ziehung + "\n\nWahnsinn!!! Jackpot!!!\n\n"
                # Steige aus Schleife aus
                break    

    #Gib alle notwendigen Infos zurueck
    return ziehungsergebnis,ziehungsCount,guthaben,message_ziehung


#%%
# Unterprogramm: Output
def output(ziehungsergebnis,ziehungsCount,guthaben,message):
    #print("\nBei {} Ziehungen mit den Zahlen \"{}\" gab es folgendes Ergebnis: ".format(ziehungsCount,str(usernum)[1:-1]))
    message = message + "\nBei " + str(ziehungsCount) + " Ziehungen mit den Zahlen \"" + str(str(usernum)[1:-1]) + "\" gab es folgendes Ergebnis:"
    a = Counter(ziehungsergebnis)
    #print(a)
    for i in range(0,7):
        if i in a:
            #print("Es gab {} {}er".format(a[i],i))
            message = message + "\nEs gab " + str(a[i]) + " " + str(i) + "er"
            #message = message + str(i)
        else:
            #print("Es gab 0 {}er".format(i))
            message = message + "\nEs gab " + "0 " + str(i) +"er"
    #print("Restliches Guthaben {}".format(guthaben))
    message = message + "\nRestliches Guthaben " + str(guthaben)
    # Gib die erweiterte Nachricht zurueck
    return message


#%%
# Hauptprogramm

# Waehle das Theme fur die GUI
sg.theme('DarkBlue13')
# Gib das Layout fur die GUI vor
layout = [  [sg.Text('!!!!Lottospiel!!!!\nSie haben 3500 € Guthaben und ein Tipp kostet 1,5 €.\nEs wird solange gespielt, bis der 6er geknackt wird oder das Guthaben aufgebraucht ist.\nGeben Sie 6 eindeutige Zahlen zwischen 1-45 mit Leerzeichen ein:')],
            [sg.Text('Ihr Tipp: '), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Exit')] ]

# Erzeuge das Fenster mit Titel bei Aufruf des Programms
window = sg.Window('Lottospiel', layout)

while True:
    # Lese die Buttons und die eingetragenen Werte aus dem GUI-Fenster ein
    event, values = window.read()
    # Fenster schliessen bis das "X" betaetigt wird oder "Exit" betaetigt
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        break
    # Wenn "Ok" betaetigt wird
    if event == 'Ok':
        #print('You entered ', values[0])
        # Startbedingungen
        guthaben = 3500
        tippkosten = 1.5

        # Uebergib die Eingabe an das Userzahlen Unterprogramm fuer eine Pruefung der Zahlen
        usernum, message = user_numbers(values[0])

        # Pruefe ob Userzahlen-Message den Text fuer eine Ziehung entspricht.
        if message == "OK. Zahlen entsprechen den Bedingungen.":
            # Fuehre die Ziehungen mit Hilfe eines Unterprogramms durch
            ergebnis,anzahl,guthaben,message = ziehungen(guthaben,tippkosten,message)
            # Bereite den User einen leserlichen Output auf
            message = output(ergebnis,anzahl,guthaben,message)

        # Popup mit Erfolgmeldung oder Fehlermeldung
        sg.popup_ok('{}\n{}'.format(usernum,message),title='Ziehungsergebnis',line_width=95)

# Schliesse das Fenster bei Programmende
window.close()