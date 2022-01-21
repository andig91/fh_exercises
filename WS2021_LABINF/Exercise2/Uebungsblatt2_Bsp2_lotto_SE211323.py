"""
Lotto spielen mit Guthaben (CLI-Version)
"""
from collections import Counter
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
    #Gib die Schnittmenge und die Anzahl der Zahlen in der Schnittmenge zurueck
    return matching, len(matching)

#%%
# Unterprogramm: Ziehungen
def ziehungen(guthaben,tippkosten,detail):
    ziehungsergebnis = []
    ziehungsCount = 0
    #Wiederhole die Ziehung so oft, bis das Guthaben verbraucht ist
    while guthaben >= tippkosten:
        #Wenn gewuenscht, gib Details zu dieser Ziehung aus
        if detail.lower() in ("y","j"):
                print("Aktuelles Guthaben: {}".format(guthaben))
        #Buche pro Tipp etwas vom Guthaben ab
        guthaben -= tippkosten
        # Zaehlen der Ziehungen
        ziehungsCount += 1
        #Erzeuge Lottozahlen im Unterprogramm
        cpu_numbers = computer_numbers()
        #Vergleiche Userzahlen mit dem Lottozahlen im Unterprogramm
        treffer, ergebnis = compare(usernum,cpu_numbers)
        #Frage ab, wenn das Set leer ist (Extra, weil leeres Set anders verhaelt)
        if ergebnis==0:
            #Wenn gewuenscht, gib Details zu dieser Ziehung aus
            if detail.lower() in ("y","j"):
                print("{} => Kein Treffer".format(cpu_numbers))
            #Schreibe eine 0 ins Array
            ziehungsergebnis.append(0)
        else:
            #Wenn gewuenscht, gib Details zu dieser Ziehung aus
            if detail.lower() in ("y","j"):
                print("{} => {}".format(cpu_numbers,treffer))
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
                guthaben += 1000000
                # Extra Text, wenn ein 6er!!
                print("\n\nWahnsinn!!! Jackpot!!!\n\n")
                # Steige aus Schleife aus
                break  

    #Gib alle notwendigen Infos zurueck
    return ziehungsergebnis,ziehungsCount,guthaben

#%%
# Unterprogramm: Output
def output(ziehungsCount,ziehungsergebnis):
    # Gib den User nochmal eine Zusammenfassung
    print("\nBei {} Ziehungen mit den Zahlen \"{}\" gab es folgendes Ergebnis: ".format(ziehungsCount,str(usernum)[1:-1]))
    # Wende Counter an, um zu erfahren, wie oft eine Zahl im Array vorkommt
    a = Counter(ziehungsergebnis)
    #print(a)
    # Gehe alle moeglichen Kombinationen durch
    for i in range(0,7):
        # Wenn ein Treffer ermittelt wurde, gib Anzahl aus
        if i in a:
            print("Es gab {} {}er".format(a[i],i))
        # Wenn kein Treffer ermittelt wurde, gib die Anzahl 0 aus
        else:
            print("Es gab 0 {}er".format(i))
    # Gib den User sein uebergebliebenes Guthaben aus
    print("Restliches Guthaben {}".format(guthaben))

#%%
# Hauptprogramm

# Einleitung
print("Willkommen bei meinem Lottospiel.\nSie erhalten 3500€ Starguthaben, ein Tipp kostet 1,5€.\nNach Eingabe Ihrer sechs Glueckszahlen, wird solange gezogen bis das Guthaben verbraucht ist oder Sie einen 6er im Lotto haben.")
# Vorraussetzungen: Startkapital und Tippkosten
guthaben = 3500
tippkosten = 1.5
# Frage den User nach seinen Zahlen mit Hilfe eines Unterprogramms
usernum = user_numbers()
# Frage den User, ob er die Details pro Ziehung angezeigt werden sollen
detail=input("Möchten Sie jede Ziehung anzeigt bekommen? [ja = y oder j, nein = beliebige Eingabe]:  ")
# Fuehre die Ziehungen mit Hilfe eines Unterprogramms durch
ergebnis,anzahl,guthaben=ziehungen(guthaben,tippkosten,detail)
# Gib den User einen leserlich aufbereiteten Output zurueck
output(anzahl,ergebnis)


