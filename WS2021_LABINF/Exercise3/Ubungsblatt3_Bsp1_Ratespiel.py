##################################################################################################################################
# Uebungblatt 3
# Beispiel 1
# 
# Ratespiel
# 
# Programmieren Sie ein Ratespiel inkl. einer kleinen künstliche Intelligenz (KI). Ratespiel: Umgekehrter
# Weg in random_example.py zu sehen. Diesmal sollen nicht Sie die Zufallszahl erraten, sondern der Computer.
# Hinweis: Versuchen Sie den Code in Funktionen aufzuteilen und diese aufzurufen.
#
# a) Zufallszahlen: Überlegen Sie sich eine Zahl zwischen 1-100. Das Programm rät danach eine zufällige Zahl zwischen 1-100.
# b) Userinput: Sie als UserIn geben niedriger (lower) oder höher (higher) oder richtig (correct) für die korrekte Zahl ein. 
# D.h. der Computer beginnt zu raten und Sie antworten, solange bis die richtige Zahl erraten wurde.
# c) Counter: Zählen Sie die Anzahl der Versuche, die der Computer benötigt, um ihre Zahl zu erraten, mit.
# Tipp für eine künstliche Intelligenz:
# Sie können ihr Programm vorerst immer um eins höher/niedriger raten lassen. Ziel der Übung ist es strategisch vorzugehen:
# Überlegen Sie sich oder diskutieren Sie mit ihren KollegInnen eine Strategie aus und setzen Sie diese um 
# z.B.: der Computer berechnet sich die Mitte des Bereichs und nimmt diese Zahl
#
#################################################################################################################################


import random

# Unterprogramm Welcome Message
def welcome(lowNumber,upNumber):
    # Ausfuehrliche Beschreibung
    print("""Willkommen im Spiel \"PC erraet Zufallszahl!\"\n
Ueberlegen Sie sich eine Zahl zwischen {} und {}.
Die künstliche Intellegenz des PCs versucht diese Zahl zu erraten.
Ist das Ergebnis richtig, dann bitte mit \"correct\" oder \"=\" antworten.
Bei jedem falschen Rateversuch können Sie mit \"higher\" oder \"lower\" antworten. (Bzw \"+\" und \"-\")
Es wird die Anzahl der Versuche mitgezählt, bis es zu einer korrekten Antwort kommt.""".format(lowNumber,upNumber))
    
    # Erlauterung, dass es zwei Modis gibt
    print("""\nDer PC hat zwei verschiedene Ratemodis.
Ohne weitere Details zu nennen.
Wenn Sie sich eine Zahl ueberlegt haben und bereit sind, geben Sie \"1\" oder \"2\" ein und die Enter-Taste!\n""")

    return

# Unterprogramm Modus-Auswahl
def modeSelect():
    # Schleife bis Modus korrekt gewaehlt wurde
    while True:
        mode=input("Welcher Modus?    ")
        # Abfrage ob Modus in der Auswahl liegt
        if mode in ("1","2"):
            break
        # Erneuter Versuch, wenn nicht
        else:
            print("Falsche Eingabe, bitte erneut probieren")
    # Gib Modus als Integer zurueck
    return int(mode)
        
# Unterprogramm: Nummern-Ermittlung
def tryNumberGenerator(lowNumber,upNumber,mode):
    #print("{} {}".format(lowNumber,upNumber))
    # Mode 1 => Immer die Mitte des gewaehlten Bereichs
    if mode == 1:
        trynumber=int((lowNumber+upNumber)/2)
    # Mode 2 => Zufällige Zahl im gewaehlten Bereich
    else:
        trynumber=random.randrange(lowNumber,upNumber+1)
    # Gib Zahl zurueck
    return trynumber

# Unterprogramm: Userabfrage + Logik
def askuser(lowNumber,upNumber,trynumber,mode,maxNumber):
    # Fake-Parameter bei Unterprogrammaufruf auf 0
    fake = 0
    # Schleife bis User korrekte Eingabe gemacht hat
    while True:
        # Ausgabe geratene Zahl und Frage an User ob korrekt
        print("Tipp des PCs: {}".format(trynumber))
        answer=input("Ist das korrekt?  ")
        # Zweig, wenn gesucht Zahl hoeher
        if answer in ("+","higher"):
            # Verhalten bei Modus 2
            if mode == 2:
                # Schummelerkennung
                if trynumber == upNumber:
                    fake = 1
                # Setze untere Grenzen fuer Ratebereich neu
                lowNumber=trynumber+1
            # Verhalten bei Modus 1
            else:
                # Formel braucht Hilfe, falls die gesuchte Zahl gleich dem Maximum ist.
                if trynumber==maxNumber-1:
                    lowNumber=maxNumber
                else:
                    # Schummelerkennung
                    if ((trynumber+1) == upNumber) or (trynumber == maxNumber):
                        fake = 1
                    # Setze untere Grenzen fuer Ratebereich neu
                    lowNumber=trynumber
            break
        # Zweig, wenn gesucht Zahl niedriger
        elif answer in ("-","lower"):
            # Schummelerkennung
            if trynumber == lowNumber:
                fake = 1
            # Verhalten bei Modus 2
            if mode == 2:
                # Setze obere Grenzen fuer Ratebereich neu
                upNumber=trynumber-1
            # Verhalten bei Modus 2
            else:
                # Setze obere Grenzen fuer Ratebereich neu
                upNumber=trynumber
            break
        # Zweig, wenn gesucht Zahl gefunden wurde
        elif answer in ("=","correct"):
            # Steige aus Schleife aus
            break
        # Wiederholen, wenn eingabe nicht korrekt
        else:
            print("Das war keine richtige Eingabe. Erneut versuchen.  ")
    # Gib alle notwendigen Parameter zurueck
    return lowNumber,upNumber,answer,fake

# Unterprogramm Output
def output(fake,trynumber):
    # Nachricht, wenn alles korrekt gelaufen ist
    if fake != 1:
        print("\nIhre Zahl {} wurde in {} Versuchen vom PC erraten".format(trynumber,counter))
    # Nachricht, wenn User geschummelt hat
    else:
        print("\nAbbruch!!!! Irgendwo wurde bei einer Antwort gelogen!!!!!")

# Global Parameters
lowNumber=1
maxNumber=100
counter=0
# Merke dir die maximale Nummer
upNumber=maxNumber

# Rufe Unterprogramm: Welcome Message mit Global Parameters
welcome(lowNumber,upNumber)

# Rufe Unterprogramm: Rate-Modus-Auswahl
mode=modeSelect()


# Schleife solange der die geratene Zahl nicht korrekt ist
while True:
    # Anzahl Versuche + 1
    counter+=1
    # Aufruf Unterprogramm: Nummern-Ermittlung
    trynumber=tryNumberGenerator(lowNumber,upNumber,mode)
    # Aufruf Unterprogramm: Userabfrage + Logik
    lowNumber,upNumber,answer,fake=askuser(lowNumber,upNumber,trynumber,mode,maxNumber)
    # Verlasse Programm, wenn die Zahl erraten wurde oder der User schummelt
    if (fake == 1) or (answer in ("=","correct")):
        break

# Rufe Unterprogramm Output
output(fake,trynumber)



