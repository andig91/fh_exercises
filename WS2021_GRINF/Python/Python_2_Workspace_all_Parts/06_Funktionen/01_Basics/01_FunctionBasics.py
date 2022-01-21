# Funktionen sind ein sehr wichtiger Teil von Python. Bis jetzt haben wir immer die Build-in Functions
# in Python verwendet. Wie auch immer, um diverse Problemstellungen loesen zu koennen muss man auch 
# selbst dafuer diverse Funktionen implementieren.

# Funktionen werden verwendet um eine Reihe von Anweisungen zu buendeln die wiederholt verwendet oder 
# aufgerufen werden sollen. Ebenso sind sie auf Grund ihrer Komplexitaet besser in einem eigenstaendigen 
# Unterprogramm aufgehoben und koennen bei Bedarf abgreufen werden. Das bedeutet, dass eine Funktion ein Code 
# ist, der zum Ausfuehren einer bestimmten Aufgabe geschrieben wird. Um diese spezielle Aufgabe auszufuehren, 
# benoetigt die Funktion moeglicherweise mehrere Eingaben. Wenn die Aufgabe ausgefuehrt wird, kann die 
# Funktion einen oder mehrere Werte zurueckgeben.


# *** Es gibt 3 arten von Funktionen in Python: 

#   1.  Eingebaute Funktionen wie help () um Hilfe zu bitten, min () um den Minimalwert zu erhalten, print () um 
#       ein Objekt auf das Terminal zu drucken, ... Uebersicht: https://docs.python.org/3/library/functions.html
#   2.  Benutzerdefinierte Funktionen (User Defined Functions, UDFs), bei denen es sich um Funktionen handelt, 
#       die Benutzer erstellen, um ihnen zu helfen; Und
#   3.  Anonyme Funktionen, die auch als Lambda-Funktionen bezeichnet werden, weil sie nicht mit dem Standard-
#       schluesselwort def deklariert sind.


# *** Functions vs Methods

# Eine Methode verweist auf eine Funktion die Teil einer Klasse ist und wird ueber die instanz oder das Objekt der
# Klasse verwendet. Eine Funktion hat diese Einschraenkungen nicht, es ist einfach eine Stand-allone Funktion. Das
# bedeuztet dass alle Methoden Funktionen sind aber nicht alle Funktionen sind Methoden.

# Hier nun ein Beispiel: zuerst impl. wir die Funktion plus() und dann 2. eine Summationsklasse mit einer sum()-Methode:

# ** 1. Definieren der Funktion "plus()"
def plus( a, b ):
    return a + b

print( plus( 2, 4 ) )
  
# ** 2. Erstelen der "Summation" Klasse
class Summation( object ):
    def sum( self, a, b ):
        self.contents = a + b
        return self.contents 

# Wenn man jetzt aber aus der Summation Klasse das Ergebnis Berechnen lassen moechte muss man wie zuvor eine Instanz 
# davon anlegen:

sumInstance = Summation()
print( sumInstance.sum( 3, 5 ) )


# *** Wie definiert man jetzt eine Funktion

# Die vier Schritte zum Definieren einer Funktion in Python sind die folgenden:

#   1.  Verwenden des Schluesselwortes "def", um die Funktion zu deklarieren, gefolgt vom Funktionsnamen.
#   2.  Hinzufuegen der Funktionsparameter: Diese sollten innerhalb der Klammern der Funktion stehen. Anschliessend 
#       wird die Zeile mit einem Doppelpunkt beendet.
#   3.  Hinzufuegen der Anweisungen die von der Funktion ausgefuehrt werden sollen. Wichtig zu beachten ist hier die 
#       Einrueckung
#   4.  Eine Funktion wird mit einer "return" Anweissung beendet, wenn die Funktion etwas ausgeben soll. Ohne die 
#       return-Anweisung gibt Ihre Funktion ein Objekt None zuruck. Generell kann die "return" Anweisung aber immer 
#       geschrieben werden.

# Definition der Funktion
def helloWorld():
    print( "Hello World" )
    return("Hello")

# Aufruf der Funktion
erg = helloWorld() * 2

# Natuerlich koennen Funktionen viel komplexer sein.

# Wenn man also den Output einer Funktion weiter verwenden moechte muss das return statement verwendet werden um einen Wert
# zurueckzugeben (z.B.: String, Integer, ...). Siehe folgendes Szenario: hello() gibt einen String zurueck, hingegen helloNoReturn()
# returniert None da kein Wert angegeben.

def hello():
    print( "Hello World" ) 
    return( "hello" )

def helloNoReturn():
    print( "Hello World" )
  
# Multiplizieren des Outputs von "hello()" mit 2 
hello() * 2 

# (Versuchen den) Output von "hello_noreturn()" mit 2 zu multiplizieren
#hello_noreturn() * 2       # --> geht nicht da als return None