"""
Lotto spielen bis der Gewinn eintritt
"""
from collections import Counter
import time
import random
#%%
# Unterprogramm: Ermittlung der Userzahlen
def user_numbers():
    """
    Einlesen der Userzahlen
     - check ob Zahl ist zwischen 1-45
     - check ob alle Zahlen eindeutig sind
     - check ob 6 eindeutige Zahlen in Liste sind
    :return: Liste mit 6 eindeutigen Zahlen [1,2,3,4,5,6]
    """

    user_nr = []            # meine Zahlen
    
    #Schleife solange es keine 6 eindeutigen Zahlen sind
    while len(set(user_nr))!= 6:
        user_nr.clear()             #Userzahlen zurücksetzen
        #testzahlen = '11 22 33 44 1 6'          # Testzahlen um muehsame Eingaben zu umgehen
        #tipp = testzahlen.split(' ') 
        tipp = input('Geben Sie 6 eindeutige Zahlen zwischen 1-45 mit Leerzeichen ein: ').split(' ')
        
        #Checks durchführen
        for zahl in tipp:
            #Anpassung, negative Zahlen wurden nicht als Zahlen erkannt
            if zahl.strip('-').isnumeric():
                #Wenn Zahl den Bedingungen entspricht zum Array hinzufügen
                if 1 <= int(zahl) <=45:
                    user_nr.append(int(zahl))
                else:
                    #Fehlerausgabe wenn Zahl nicht im Bereich ist
                    print(zahl)
                    print('Alle Zahlen muessen zwischen 1 und 45 sein!')
                    break
            else:
                #Fehlerausgabe wenn es keine Zahl ist
                print(zahl)
                print('Es wurde keine Zahl eingegeben!')
                break
        if len(set(user_nr))!= 6:
            #Fehlerausgabe, dass es sich nicht um 6 eindeutige Zahlen handelt.
            print(set(user_nr))
            print("Bei Ihrer Eingabe handelt es sich nicht um 6 eindeutige Zahlen.\nBitte nochmals versuchen.")
    #Wenn alle Pruefungen ok, dann gib die Zahlen zurueck
    return user_nr

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
    #Gib die Anzahl der Zahlen in der Schnittmenge zurueck
    return len(matching)

#%%
# Unterprogramm: Ziehungen
def ziehungen(usernum,ziel):
    # Speichere die Zeit, als die Ziehungen begonnen haben
    starttime=time.time()

    ziehungsergebnis = []
    ziehungsCount = 0

    # Endlosschleife bis der gewünschte Gewinn erhalten wird
    while True:
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
            #Extraausgabe wenn Jackpot erreicht wird und beende Schleife
            if ergebnis == 6:
                print("\n\nWahnsinn!!! Jackpot!!!\n\n")
                break  
            #Beende Schleife, wenn das gewuenste Ergebnis erreicht wird
            if ergebnis >= ziel:
                break      
            
    # Berechne die Zeit fuer die Ermittlung der richtigen Zahlen
    deltatime = time.time() - starttime
    # Gib das Ziehungsergebnis und die Zeit zurueck
    return ziehungsergebnis,ziehungsCount,deltatime

#%%
# Unterprogramm: Output
def output(ziehungsergebnis,ziehungsCount,deltatime,ziel):
    # Gib den User nochmal eine Zusammenfassung
    print("\n{}er wurde erreicht!!".format(ziel))
    print("Bei {} Ziehungen mit den Zahlen \"{}\" gab es folgendes Ergebnis: ".format(ziehungsCount,str(usernum)[1:-1]))
    # Wende Counter an, um zu erfahren, wie oft eine Zahl im Array vorkommt
    a = Counter(ziehungsergebnis)
    #print(a)
    # Gehe alle moeglichen Kombinationen durch
    for i in range(0,7):
        if i in a:
            # Wenn ein Treffer ermittelt wurde, gib Anzahl aus
            print("Es gab {} {}er".format(a[i],i))
        else:
            # Wenn kein Treffer ermittelt wurde, gib die Anzahl 0 aus
            print("Es gab 0 {}er".format(i))
    # Gib den User die Zeit fuer die Berechnung aus
    print("Nach {} Sekunden hat der PC die richtigen Zufallszahlen ermittelt.".format(deltatime))
    kosten=ziehungsCount*1.5
    print("Wenn ein Tipp 1,5€ kostet, haetten hier {}€ ausgelegt werden muessen.".format(kosten))
#%%
# Hauptprogramm

# Hier kann gesteuert werden, bis zu welchen Gewinn man spielen will.
ziel = 5
# Einleitung
print("Willkommen bei meinem Lottospiel.\nNach Eingabe Ihrer sechs Glueckszahlen, wird solange eine Ziehung durchgefuehrt bis ein {}er gewonnen wird.".format(ziel))
# Frage den User nach seinen Zahlen mit Hilfe eines Unterprogramms
usernum = user_numbers()
# Fuehre die Ziehungen mit Hilfe eines Unterprogramms durch
ziehungsergebnis,anzahl,deltatime=ziehungen(usernum,ziel)
# Gib den User einen leserlich aufbereiteten Output zurueck
output(ziehungsergebnis,anzahl,deltatime,ziel)
    
