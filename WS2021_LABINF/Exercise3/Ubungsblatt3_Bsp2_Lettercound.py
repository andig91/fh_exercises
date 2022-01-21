##################################################################################################################################
# Uebungblatt 3
# Beispiel 1
# 
# Gegeben ist folgender Satz als String:
# sentence = 'Jim quickly realized that the beautiful gowns are expensive'
#
# a) Erstellen Sie ein Dictionary count_letters mit Keys für Buchstaben im Satz. 
# Die Werte der Keys sollen die Häufigkeit des Vorkommens (int) darstellen (z.B {'J': 1, 'i': 5, 'm': 1, …}
# 
# b) Geben Sie anschließend das Dictionary aus - print(count_letters)
# 
# Tipp:
# Durchlaufen Sie mit einer Schleife alle Buchstaben und überprüfen Sie ob dieser bereits als Key im Dictionary vorkommt 
# (z.B.: if buchstabe in count_letters.keys(): … ). 
# Wenn ja erhöhen sie den Wert des Keys, ansonsten setzen Sie den Wert auf 1.
# 
#
# Eigenfestlegung, weil nicht in der Anleitung beschrieben und der Beispielsatz diese Anforderung nicht hat:
# Im Programm wird nur der Buchstabe unterschieden, die Groß- oder Kleinschreibung ist daher unerheblich.
# Jeder Key im Dictionary stellt also den Buchstaben in großer und kleiner Ausfuehrung im Satz dar.
#
#
##################################################################################################################################


# Vorgegebener Satz
sentence = 'Jim quickly realized that the beautiful gowns are expensive'
# Eigener Satz
#sentence = 'Jim quickly realized that the 1 3 444 beautiful 55564gowns are expensive'

# Erzeuge leeres Dictionary
count_letters = {}

# Arbeite jedes Zeichen im Satz durch
for letter in sentence:
    # Nur Buchstaben werden gesucht, keine Leerzeichen oder Zahlen
    if not ((letter == " ") or letter.isnumeric()):
        # Es wird alles in Kleinbuchstaben umgewandelt und so im Dictionary gespeichert
        # Ueberpruefe ob Buchstabe schon vorhanden
        if letter.lower() in count_letters.keys():
            # Wenn Key schon vorhanden, dann erhoehe um 1
            count_letters[letter.lower()]+=1
        else:
            # Wenn Key nicht vorhanden, dann erstelle es mit 1
            count_letters[letter.lower()]=1

# Ausgabe des kompletten Dictionary
print(count_letters)
