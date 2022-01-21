#Uebungsblatt 3 Beispiel 3

# Zusatz: Initial gibt es Kunde 1 und Kunde 2
# Kunden werden zum Programmende und beim naechsten Programmstart importiert (Falls Datei vorhanden)
# Log ueberlebt auch Neustart

#GUI Layout für Combofelder oder Listfeld:
#https://pysimplegui.readthedocs.io/en/latest/     Suche nach Combo oder Listbox



# Klasse definieren
class Wellnesscenter:
    import time

    # Lese Parameter ein
    def __init__(self, id, name, guthaben, geburtstag):
        self.id = int(id)
        self.name = str(name)
        self.guthaben = float(guthaben)
        self.geburtstag = str(geburtstag)

    # Unterprogramm in Klasse um zu bestimmen ob Kunde ein Kind ist
    def is_child(self):
        geburtssplit=self.geburtstag.split('.')
        if (int(self.time.strftime("%Y")) - int(geburtssplit[2]) < 18) or ((int(self.time.strftime("%Y")) - int(geburtssplit[2]) == 18) and (int(self.time.strftime("%m")) >= int(geburtssplit[1])) and (int(self.time.strftime("%d")) >= int(geburtssplit[0]))):
            return True
        else:
            return False

    # Unterprogramm in Klasse das bestimmt ob es moeglich ist in eine float umzuwandeln
    def is_float(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def chargeCredit(self, betrag):
        """
        Methode um Guthaben aufzuladen
        :param betrag: Aufladebetrag
        :return:
        """

        # Wenn eine float-Zahl eingegeben wurde und die Zahl groesser 5 ist
        if self.is_float(betrag) and float(betrag) >= 5:
            # Frage ab ob Endergebnis ueber 200 waere
            if float(betrag)+self.guthaben <= 200:
                # Dann buche auf
                self.guthaben+=float(betrag)
                # Erzeuge Nachricht
                message = betrag + " Euro Guthaben wurde erfolgreich aufgeladen. Kontostand: " + str(self.guthaben) + " Euro"
                # Schreibe in Logdatei
                self.log("append",message)
            else:
                # Nachricht, wenn 200 Euro ueberschritten sind
                message = "Guthaben ueber 200 Euro nicht erlaubt"
        else:
            # Nachricht, wenn Bedinungen nicht erfuellt sind
            message = "Bitte mindestens 5 Euro aufladen oder es wurde keine korrekte Zahl eingegeben.\nTipp: Dezimaltrennzeichen = \".\""
        return message

    def bookService(self, service, extraService, mode):
        """
        Check ob Service gebucht werden können (Guthaben vorhanden?) wenn ja Services buchen und Guthaben neu berechnen
        :param service: welche Tageskarte
        :param extraService: welcher zusatzservice wurde gebucht
        :return:
        """
        abzug = 0
        # Dictionary mit Preistabelle
        serviceKosten = {'Erwachsene': 25, 'Studierende': 18, 'Kinder': 12, "Sauna": 5, "Private SPA": 10, 'kein Service': 0}
        # Wenn extraService leer, dann wie "kein Service"
        if extraService == "":
            extraService = 'kein Service'
        # Grundservice muss gewaehlt sein
        if service == "": 
            message = "Kein Service gewaehlt, daher keine Abbuchung"

        # Wenn Bedingungen erfuellt sind
        else:
            # Kunde bekommt, Popup mit Info zu den Kosten, bevor gebucht wird und kann diese ablehnen
            if mode == 'prebook':
                message = str(service) + ": " + str(serviceKosten[service]) +" Euro\n" + str(extraService) + ": " + str(serviceKosten[extraService]) +" Euro\nWollen Sie wirklich buchen?\n"
            # Abrechnung, wenn Kunde bestaetigt
            else:
                # Addiere Kosten
                abzug += serviceKosten[service]
                abzug += serviceKosten[extraService]

                # Fehlermeldung, falls Kinderticket ausgewahlt wurde und man zu alt ist
                if service == 'Kinder' and self.is_child() == False:
                    message = "Nicht moeglich. Kinder sind maximal 18 Jahre alt."
                # Fehlermeldung, falls nicht genug Guthaben vorhanden ist
                elif abzug > self.guthaben:
                    message = "Nicht genug Guthaben vorhanden"
                # Wenn alles passt, dann ziehe Betrag ab und schreibe Meldungen + Logs
                else:
                    self.guthaben-=float(abzug)
                    message = str(abzug) + " Euro [" + str(service) + ", " + str(extraService) + "] Guthaben wurde erfolgreich abgebucht. Kontostand: " + str(self.guthaben) + " Euro"
                    self.log("append",message)
        # Gib Message zurueck
        return message

    # Unterprogramm fuer schreiben der Logs
    def log(self, action, text):
        logfile = "wellness_accesslog.txt"
        if action == "append":
            file = open(logfile, "a")
            file.write("\n" + str(self.id) + ";" + self.time.strftime("%Y/%m/%d_%H:%M:%S") + ": " + text)
            file.close()
        if action == "read":
            file = open(logfile, "r")
            readlog = ""
            #readlog = []
            for line in file:
                linePart=line.split(";")
                if line.startswith(str(self.id) + ";") == True:
                    #readlog.append(line)
                    readlog += linePart[1]
            #print(readlog)
            return readlog
    
    # Unterprogramm zum schreiben, des Exports
    def export(self, kundenfile):
        file = open(kundenfile, "a")
        file.write(str(self.id) + ";" + str(self.name) + ";" + str(self.guthaben) + ";" + str(self.geburtstag) + "\n")
        file.close()

    # Standardausgabe der Klasse    
    def __str__(self):
        return f'Die ID {self.id} heisst {self.name}, hat am {self.geburtstag} und hat {self.guthaben} Euro Guthaben'

# importiere notwendige Libs
import PySimpleGUI as sg
import os

# Ermittelt welcher Arrayindex zur Kundennummer passt
def indexermittlung(login,kunden):
    index = 0
    for k in kunden:
        if k.id == login:
            break
        index += 1
    if index < len(kunden):
        #print(index)
        #print(len(kunden))
        #print("gefunden")
        return index, True
    else:
        #print("Nicht gefunden")
        return index, False

# Unterprogramm zur Erstellung des Hauptfensters
def makewin(title):
    layoutLogin = [  [sg.Text('Willkommen im Welnesscenter der FHSTP.\nHier können Sie ihr Guthaben verwalten und Zutrittskarten buchen.\nGeben Sie Ihr ID (1-999) ein um sich einzuloggen: ',font=(None,15))],
        [sg.Text('Ihre ID: ',font=(None,15)), sg.InputText(font=(None,15))],
        [sg.Button('Ok',size=(26,1),font=(None,15)), sg.Button('Exit',size=(26,1),font=(None,15))] ]
    return sg.Window(title, layoutLogin, finalize=True)

# Unterprogramm zum Erstellen des Datenexports
def datenexport(kunden):
    kundenfile = "kundendatei.txt"
    if os.path.exists(kundenfile):
        os.remove(kundenfile)
    for k in kunden:
        k.export(kundenfile)

# Unterprogramm zum Importieren der Kundendaten
def datenimport(kunden):
    kundenfile = "kundendatei.txt"
    if os.path.exists(kundenfile):
        file = open(kundenfile, "r")
        for line in file:
            if len(line) > 6:
                linePart=line.split(";")
                kunden.append(Wellnesscenter(int(linePart[0]), str(linePart[1]), float(linePart[2]), str(linePart[3])))
            #print(readlog)
    else:
        kunden.append(Wellnesscenter(1, "Andreas", 30, "20.08.1996"))
        kunden.append(Wellnesscenter(2, "Tommy", 14, "02.01.1993"))


#Hauptprogram
#Tipp: Zuerst Punkt a-c via Konsole ausgeben und danach erst die GUI machen
# Tipp zur GUI: Combofelder oder Listfelder

#from turtle import color, width


# Auswahl der Services und Zusatzleistungen
services = ['Erwachsene', 'Studierende', 'Kinder']
extraServices = ['kein Service', 'Sauna', 'Private SPA']

# Erzeuge Kundenarray
kunden = []
# Importiere Daten
datenimport(kunden)


#layoutLogin = [  [sg.Text('Willkommen im Welnesscenter der FHSTP.\nHier können Sie ihr Guthaben verwalten und Zutrittskarten buchen.\nGeben Sie Ihr ID (1-999) ein um sich einzuloggen: ',font=(None,15))],
#        [sg.Text('Ihre ID: ',font=(None,15)), sg.InputText(font=(None,15))],
#        [sg.Button('Ok',size=(26,1),font=(None,15)), sg.Button('Exit',size=(26,1),font=(None,15))] ]

# Rufe das Grundfenster auf
windowLogin = makewin('WellnessCenter')

while True:
    #windowLogin = sg.Window('WellnessCenter', layout=layoutLogin)

    # Nehme Eingaben auf
    event, values = windowLogin.read()
    # Wenn Hauptfenster geschlossen wird, dann Programmende und Datenexport
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
        datenexport(kunden)
        break

    # Wenn OK geklickt wird
    if event == 'Ok':
        # Pruefe ob zwischen 0 und 1000
        if values[0].isnumeric() == True and int(values[0]) > 0 and int(values[0]) < 1000:
            login = int(values[0])
            #print(login)
            # Pruefe ob Kunde existiert
            index, kundeexist = indexermittlung(login,kunden)

            # Wenn Kunde existiert, dann schliesse Hauptfenster
            if kundeexist == True:
                windowLogin.close()

            # Wenn Kunde nicht existiert
            else:
                #print("Existiert nicht")
                newUser = sg.popup_get_text('Die ID {} existiert nicht.\nMoechten Sie diese anlegen?\nBitte geben Sie mit einen Abstand getrennt ihren Vornamen und ihr Geburtsdatum an:\nBeispiel: Max TT.MM.YYYY'.format(login),title='ID nicht bekannt')

                while True:
                    #if len(newUser) > 0:
                    if type(newUser) is str:
                        newUserArg = newUser.split(" ")
                        if len(newUserArg) == 2:
                            newUserDate = newUserArg[1].split(".")
                            #print(newUserArg[0])
                            #print(newUserDate)
                            #print(newUserDate)
                            if (len(newUserDate) == 3) and newUserDate[0].isnumeric() and newUserDate[1].isnumeric() and newUserDate[2].isnumeric() and (1 <= int(newUserDate[0]) <= 31) and (1 <= int(newUserDate[1]) <= 12) and (1900 <= int(newUserDate[2]) <= 2022):
                                print("ID: {}, Name: {}, Geburtstag: {}, Geburtsmonat: {}, Geburtsjahr: {}".format(login,newUserArg[1],int(newUserDate[0]),int(newUserDate[1]),int(newUserDate[2])))
                                kunden.append(Wellnesscenter(login, newUserArg[0], 10, newUserArg[1]))
                                sg.popup_ok("Danke, dass Sie eine Mitgliedschaft bei uns abgeschlossen haben!\nJeder Neukunde erhält von uns 10 Euro Startguthaben.",title="Willkommensbonus",line_width=200)
                                windowLogin.close()
                                index, kundeexist = indexermittlung(login,kunden)
                                kunden[index].log("append","Kunde mit 10 Euro Startguthaben angelegt.")
                                break
                        newUser = sg.popup_get_text('Die Eingabe war nicht korrekt.\nBitte korrigieren Sie ihre Eingabe:\nBeispiel: Max TT.MM.YYYY'.format(login),title='ID nicht bekannt',default_text=newUser)    

                    else:
                        break

            # Wenn Kunde existiert, dann mache Benutzerfenster auf
            if kundeexist == True:
                kunden[index].log("append","Kundenkonto geoeffnet")
                
                # Konfiguriere und oeffne Benutzerfenster
                layoutBuy = [
                            [sg.Text("KundenID: ",font=(None,25)),sg.Text(kunden[index].id,font=(None,25),text_color="Blue")],
                            [sg.Text("Name: ",font=(None,25)),sg.Text(kunden[index].name,font=(None,25),text_color="Blue")],
                            [sg.Text(" ",font=(None,5))],
                            [sg.Text("Guthaben: ",auto_size_text=None,font=(None,25)),sg.Text(str(kunden[index].guthaben)+"€",font=(None,25),text_color="Red",key="credit")],
                            [sg.InputText(font=(None,20),size=(10,4)),sg.Button('Guthaben\naufladen',font=(None,15),size=(12,2),key="buyCredit")],
                            [sg.Text(" ",font=(None,5))],
                            [sg.Text("Services: ",auto_size_text=None,font=(None,25))],
                            [sg.Combo(values=services, size=(13,5),font=(None,15))],
                            [sg.Combo(values=extraServices, size=(13,5),font=(None,15)),sg.Button('Services\nbuchen',font=(None,15),size=(12,2),key="buySerice")],
                            [sg.Text(" ",font=(None,5))],
                            [sg.Text("Log: ",auto_size_text=None,font=(None,15))],
                            [sg.Multiline(kunden[index].log("read",""),size=(65,8),key="log")],
                            [sg.Button('Logout',font=(None,15),size=(12,2),key="logout")]
                            ]
                windowBuy = sg.Window('WellnessCenter', layout=layoutBuy)
                
                while True:
                    # Lese Eingabe vom Benutzerfenster ein
                    event, values = windowBuy.read()

                    #print(event)
                    #print(values)

                    # Verhalten wenn auf Guthaben aufladen gedrueckt wurde
                    if event == "buyCredit":
                        message = kunden[index].chargeCredit(values[0])
                        #print("Test" + str(kunden[index].guthaben))

                    # Verhalten wenn auf Service buchen gedrueckt wurde
                    elif event == "buySerice":
                        # Berechne Betraege
                        message = kunden[index].bookService(values[1],values[2],"prebook")
                        event = sg.popup_ok_cancel(message)
                        # Wenn bestaetigt, buchen
                        if event == "OK":
                            message = kunden[index].bookService(values[1],values[2],"book")
                        else:
                            message = "Buchung abgebrochen!"
                    # Sollte Logout oder Close sein
                    else:
                        windowBuy.close()
                        kunden[index].log("append","Kundenkonto geschlossen")
                        break
                    # Nachricht von den Buchungen
                    sg.popup_ok(message)
                    # Aktualisiere Felder = Guthaben, Log-Fenster
                    windowBuy["credit"].Update(str(kunden[index].guthaben))
                    windowBuy["log"].Update(kunden[index].log("read",""))
                



    # Wenn Hauptfenster geschlossen, mache es erneut auf
    if windowLogin.was_closed() == True:
        windowLogin = makewin('WellnessCenter')

