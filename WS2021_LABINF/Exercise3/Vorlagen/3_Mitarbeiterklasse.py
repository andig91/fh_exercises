import random

#Klassenerstellen: class <name>
class MitarbeiterIn:

    #Konstruktor; wird aufgerufen sobald ein Objekt der Klasse erstellt wird
    def __init__(self, id, name, salary):
        self.salary = salary
        self.name = name
        self.id = id

    #Klassenfunktionen
    def changeNameToUpperCase(self):
        self.name = self.name.upper()

    def changeNameToLowerCase(self):
        self.name = self.name.lower()

    def increaseSalary(self, prozent):
        self.salary += prozent

    #Vergleich mit toString()-Funktion aus Java
    #Für Ausgabe bei Objektaufruf mit print
    def __str__(self):
        return f'ID: {self.id}, Name: {self.name}, Gehalt: {round(self.salary, 2)}€'

    #für Objekte innerhalb Liste
    #Für verschönerte Ausgabe von Objekten, die innerhalb einer Liste sind
    def __repr__(self):
        return f'ID: {self.id} Name: {self.name}'

names = ['Lisa', 'Jane', 'Paul', 'Oliver', 'Max', 'Karl', 'Xi']

mitarbeiterListe = []           #wird mit Objekten von Miterarbeiterklasse befüllt


for id, name in enumerate(names):
    mitarbeiterListe.append(MitarbeiterIn(id, name, random.uniform(1000,5000)))

#print(mitarbeiterListe[0])     # __str__
#print(mitarbeiterListe)        # __repr__

for m in mitarbeiterListe:
    if m.id < 3 and m.salary < 3000:
        m.increaseSalary(random.uniform(1.05, 1.3))
        print(f'{m.name} bekommt eine Gehaltserhöhung')
    print(m)

print(f'Anzahl der Mitarbeiter/Objekte : {len(mitarbeiterListe)}')
