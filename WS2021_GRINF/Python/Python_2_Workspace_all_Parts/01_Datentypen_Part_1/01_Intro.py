# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Variablen sind grundsaetzlich nichts anderes als reservierte Speicherplaetze zum Speichern von Werten.
# Das bedeutet, wenn man eine Variable anlegt wird zugleich der benoetigte Speicherplatz im Speicher reserviert. 

# Basierend am verwendeten Datentyp der Variable, wird in Python vom Interpreter der entsprechende Speicherplatz 
# angefordert und auch entschieden was dann in diesem reserverten Speicherplatz gespeichert werden kann. 
# Dadurch koennen durch die Zuweisung von verschiedenen Datentypen zu Variablen auch dann:
#   - Integer
#   - Decimals
#   - Characters   
# angelegt weren. 


# *** Zuweisen von Werten zu Variablen

# Python muessen nicht explizit deklariert werden um Speicher anfordern zu koennen. Die declaration passiert 
# automatisch wenn man einen Wert einer Variable zuweist. Mit dem Gleichzeichen (Equal sign) "=" wird die 
# Wertzuweisung tu einer Variable durchgefuehrt. Hierbei ist der Operand auf der linke Seite der Name der 
# Variable und der Operand auf der rechten Seite der Wert der zugewiesen werden soll.

a = 11          # Zuweisung eines Integers
b = 2.5         # Zuweisung eines Floats
c = "Hund"      # Zuweisung eines Strings

# Ausgabe der Variablen --> Kommt dann etwas spaeter.
print( a )
print( b )
print( c )

# *** Mehrfachzuweisungen

# Ebenso erlaubt Python einen Wert zu mehreren Variablen gleichzeitig zuzuordnern:

a = b = c = 4711

print( a )
print( b )
print( c )

# Natuerlich kann man aber 3 Variablen auf einmal 3 verschiedene Werte zuweisen:

a, b, c = 1, 2.0, "Ding"

print( a )
print( b )
print( c )

# *** Standarddatentypen in Python

# Die Daten die gespeichert werden koennen von den verschiedensten Typen sein. Beispielsweise das Alter eine
# Person wird als ein nummaerischer Wert gespeichert wobei hingegen der Name oder die Adresse als ein als 
# alphanummaerische Character gespeichert werden. Python verfuegt ueber verschiedene Standarddatentypen die 
# fuer die Speicherung verwendet werden koennen. Ebenso unterstuetzt jeder Datentyp verschiedene Operationen 
# (kommt spaeter) die angewendet werden koennen.  

# Generell hat Python 5 verschiedene Standarddatentypen:
#   - Numbers       (Werden behandelt in: 01_Datentypen_Part_1)
#   - String        
#   - List          (Werden behandelt in: 08_Datentypen_Part_2)
#   - Tupel         
#   - Dictionary    

# Nur ein Zusatz fuer spaeter
import sys
x = 2
print( sys.getsizeof( x ) )
