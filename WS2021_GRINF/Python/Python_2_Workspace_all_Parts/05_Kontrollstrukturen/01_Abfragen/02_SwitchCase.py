# Das Konstrukt der Switch Case Anweisung die es bspw in JAVA, C, C++ usw gibt, ist in Python nicht direkt implementiert.
# In Python wird dieses Abfragekonstrukt mit Hilfe des Dictionaries das in einer Funktion eingebettet ist umgesetzt. Das
# Dictionary ist ein assoziative Arrays, das einfache Eins-zu-eins-Schluesselwertzuordnungen bereitstellen (key, value).

# *** Erste bekanntschaft mit dem Switch-Case Prinzip

# Hier nun die Python-Implementierung einer switch-Anweisung. Im folgenden Beispiel erstellen wir ein Woerterbuch namens 
# switcher, in dem alle schalteraehnlichen Faelle gespeichert werden.

# Die switch Funktion
def switch_month( key ):        # Das Argument nach dem gesucht werden soll --> also der schluessel
    switcher = {
#     key: value
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    print( switcher.get( key, "Invalid month" ) )

# Aufruf der Funktion --> gibt das Monat August aus
switch_month( 3 )


# Aufruf der Funktion --> gibt den Defaultstring aus da kein key:value Paar im Dictionary vorhanden ist.
switch_month( 13 )


# *** Anpassungen um die Werte auch dann weiter verwenden zu koennen

# Um das Ergebnis einer Switch-Case oder in unserem Fall einer Funktion mit einem Dictionary und einem Default Value 
# auch weiter verwenden zu koennen, ist es notwendit ein paar kleine Anpassungen durchzufuehren:

def switch_something( key ):
    switcher = {
        "CT" : "Zementestrich",
        "CE" : "Calciumsulfatestrich",
        "AS" : "Gussasphaltestrich",
        "MA" : "Magnesiaestrich",
        "SR" : "Kunstharzestrich",
    }
    return switcher.get( key, "Keys are: CT, CE, AS, MA, SR" )

print( switch_something( "CE" ) )
print( switch_something( "??" ) )