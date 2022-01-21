#Beispiel 3

#Klasse definieren
class Wellnesscenter:

    def __init__(self, id, name, guthaben, geburtstag):
        pass


    def chargeCredit(self, betrag):
        """
        Methode um Guthaben aufzuladen
        :param betrag: Aufladebetrag
        :return:
        """
        pass

    def bookService(self, service, extraService):
        """
        Check ob Service gebucht werden können (Guthaben vorhanden?) wenn ja Services buchen und Guthaben neu berechnen
        :param service: welche Tageskarte
        :param extraService: welcher zusatzservice wurde gebucht
        :return:
        """
        pass

    def __str__(self):
        return ''



#Hauptprogram
#Tipp: Zuerst Punkt a-c via Konsole ausgeben und danach erst die GUI machen
# Tipp zur GUI: Combofelder oder Listfelder

import PySimpleGUI as sg

services = ['Erwachsene', 'Studierende', 'Kinder']
extraServices = ['kein Service', 'Sauna', 'Private SPA']

#GUI Layout für Combofelder oder Listfeld:
#https://pysimplegui.readthedocs.io/en/latest/     Suche nach Combo oder Listbox
layout = [[sg.Combo(values=services, size=(50,3))],
          [sg.Listbox(values=extraServices, size=(50,3))]
          ]

window = sg.Window('WellnessCenter', layout=layout)
window.read()