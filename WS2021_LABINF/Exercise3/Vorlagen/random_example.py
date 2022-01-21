"""
Der Computer wählt per Zufall eine Zahl zwischen 1-10 aus
Danach versucht der/die UserIn die Zahl des COmputers zu erraten
Computer gibt nur Tipps: zu hoch, zu niedrig oder richtig
Wie viele Versuche wurden benötigt?
"""

import random #um Zufallszahlen generieren zu können

number = random.randint(1,10)
print(number)

guessNumber = -1        #geratene Zahl
cnt = 0                 #Anzahl der Versuche

#solange geratene Zahl != computerzahl ist
while guessNumber != number:
    #Variante1
    try:
        #Zahl einlesen
        guessNumber = int(input('Welche Zahl: '))
    except ValueError:
        guessNumber = -1
        print('Falsche Eingabe!!')
        continue

    #wenn Zahl eingegeben wurde, läuft Programm hier weiter
    if guessNumber < number:
        print('zu niedrig geraten')
    elif guessNumber > number:
        print('zu hoch geraten')

    cnt += 1                # Anzahl d. Versuche werden erhöht um 1

print(f'Richtig!\nAnzahl der Versuche: {cnt}')


"""
Tipps für Übungsblatt3 Bsp1:
Bereich 1-100 zu erraten
min=1
max=100


zahl=72

1) cpu ratet die Hälfte des Bereichs oder zuerst eine zufällige Zahl
cpu = 50
higher

2) min, max anpassen
min=50
max=100
cpu=75
lower

3) min, max solange anpassen bis Bereich <10 ist -> dann schrittweise weitergehen
min=50
max=75
cpu=62
higher

min=62
max=75
cpu=69
higher

#bereich <10
cpu=70
higher
cpu=71
higher
cpu=72
correct

x Versuche benötigt


Bei Lust und Laune probieren Sie ihr Programm für den Bereich 1-1000 aus

"""