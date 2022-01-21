# *** Die Main-Funktion

# Eine wichtige Funktion die wir unbedingt noch behandeln muessen ist die Main-Funktion. In sprachen wie 
# C, C++, C# oder JAVA ist sie bspw. der einspringspunkt an dem das Programm startet.
# In Python koennen wir die Main-Funktion verwenden, muessen aber nicht. Wenn man die main() nicht verwendet
# dann startet das Programm in der 1. Zeile und wird Zeile fuer Zeile (linear) abgearbeitet. Natuerlich werden
# wie Funktionen die dazwischen definiert wurden nur dann abgearbetet wenn sie aufgerugen werden ...
# Hingegen bei der Verwendung der main() kann man dem Programm eine klarere Struktur verpassen und hat auch
# definierten einspriungspunkt fuer den Start. Eine gute Struktur ist bspw:

#   1.  Beschreibung des Programms
#   2.  Diverse Imports
#   3.  Anlegen der globalen Variablem
#   4.  Definieren der verschiedenen Funktionen
#   5.  Definieren der main() Funktion, gefolgt vom Aufruf.

# ** Initiales BSP (muss einkommentiert werden)
"""
def main():
    print( "Hello World" )
print( "However" )
"""

# Wir bekommen hier nur die Ausgabe "However" da die Funktion main() nirgends aufgerufen wird.

# Dass passiert weil wir die call Funktion dafuer nicht definiert haben. Hierfuer gibt es ein paar wichtige 
# Punkte zu beachten:
#   1.  Wenn Python ein Sourcefile liest, dann soll jede Zeile darin ausgefuehrt werden.
#   2.  Wenn Python das Sourcefile als Hauptprogramm (main program) ausfuehrt dann wird die Variable __name__
#       gesetzt und geprueft ob diese mit __main__ uebereinstimmt.
#   3.  Wenn man also die Main Funktion ausfuehrt dann wird ein "if" statement gelesen und gecheckt wo __name__
#       mit __main__ uebereinstimmt
#   4.  Das Statement "if__name__=__main__" erlaubt es uns das Python Programm einerseits als wiederverwendbares 
#       Modul und andererseits als standallone Programm zu verwenden (auszufuehren).

# Wie wir wissen nutzt Python == fuer vergleiche und = fuer Zuweisungen
#   -   Import: __name__=Filename des Moduls
#       if Statement = FALSE --> Das Skript in main() wird nicht ausgefuehrt
#   -   Direct run: __name__=__main__
#       if Statement = TRUE --> das Skript in main() wird ausgefuehrt
#   -   Das bedeutet wenn der Code ausgefuehrt wird, dann wird geprueft ob der Modulname vorhanden ist mit "if"

# Wichtig ist noch dass unmittelbar nach der definition der main() der check fuer die main() sein muss.

def main():
    print( "Hello World" )


if __name__=="__main__":    # wuerde natuerlich auch ohne dem gehen aber wegen der wiederverwendbarkeit
    main()


print( "However" )