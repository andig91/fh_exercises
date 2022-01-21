# viele Personen mit Name, Geburtstag, Wohnort
# Problem:
from datetime import date


class Person:

    #Konstruktor, wird sofort nach Objekterzeugung aufgerufen und das Objekt wird initialisiert
    def __init__(self, name, geburtstag, wohnort):
        self.name = name
        self.geburtstag = geburtstag
        self.wohnort = wohnort


    def alterBerechnen(self):
        # split nach .
        self.alter = date.today().year - int(self.geburtstag.split('.')[-1])



    def __str__(self):
        return f'{self.name} hat am {self.geburtstag} Geburtstag | ist {self.alter} Jahre alt und wohnt in {self.wohnort}'


personenListe = []          # werden alle Personen Objekte gespeichert
personenListe.append(Person('Max1', '20.10.1951', 'Wien'))
personenListe.append(Person('Max2', '20.10.1999', 'Wien'))
personenListe.append(Person('Max3', '20.10.1991', 'Wien'))
personenListe.append(Person('Max4', '20.10.1992', 'Wien'))
personenListe.append(Person('Max5', '20.10.2002', 'Wien'))
del personenListe[0]

#person2 = Person('Max5', '20.10.2002', 'Wien')
#person2.alterBerechnen()

#personenListe[1].alterBerechnen()
#print(personenListe[1])
#print(len(personenListe))

for p in personenListe:
    p.alterBerechnen()
    print(p)





