# *** Anonyme (oder Lambda) Funktionen

# Diese Art der Funktionen werden anonym aufgerufen, da sie nicht standardmaessig mit dem Schluesselwort "def" 
# deklariert werden. Natuerlich kann dafuer dann das Schluesselwort "lambda" verwenden, um kleine anonyme 
# Funktionen zu erstellen.

#   -   Lambda-Funktionen koennen in Form eines Ausdrucks verwendet werden. Sie koennen keine Befehle oder 
#       mehrere Ausdruecke enthalten.
#   -   Anonyme Funktion kann kein direkter Aufruf zum Ausgeben sein, da Lambda einen Ausdruck erfordert.
#   -   Lambda-Funktionen haben ihren eigenen lokalen Namespace. Sie koennen nur die eigenen Variablen von 
#       der Parameterliste und diejenigen in ihrem globalen Namespace benutzen.
#   -   Obwohl es scheint, dass Lambdas eine einzeilige Version einer Funktion sind, sind sie nicht gleichwertig 
#       zu In-Line-Anweisungen in C oder C ++, deren Zweck darin besteht, die Funktionsstapelzuordnung waehrend 
#       des Aufrufs aus Leistungsgruenden zu uebergeben.


# ** Syntax von Lamda-Funktionen

# Lamda-Funktionen bestehen aus einem einzigem Statement welches wie folgt aussieht:
# lambda [ arg1 [ , arg2 [ , ..., argN ] ] ] : Anweisung


# Dadurch sieht die Funktionsweise einer Lambda-Funktion wie folgt aus:

# Definieren der summe() Lambda-Funktion
summe = lambda arg1, arg2 : arg1 + arg2

# Aufrufen der Lambda-Funktion:
print( "The sum is: " + str( summe( 10, 30 ) ) )


# ** Weitere Bsp zu Lambda Funktionen

# Natuerlich koennen Lambda Funktionen auch auf Datenstrukturen angewendet werden um bspw. schneller zu einem
# gefiltertem Ergebnis zu kommen.

myList = [ 1, 5, 4, 7, 6, 2, 9, 8, 10, 3 ]
# Wichtig ist hier zu wissen dass die filter() Funktion 2 Argumente bekommen muss:
#   1.  Die zu verwendende Funktion (der None). --> In unserem Fall die Lambda-Function
#   2.  Die Datenstruktur auf der die Operation ausgefuehrt werden soll. --> Die Liste die wir erzeugt haben
resList = list( filter( lambda x : ( x%2 == 0 ), myList ) )
print( resList )

# Natuerlich kann man das auch gleich mit anderen Schritten kombinieren:
resList = list( filter( lambda x : ( x%2 == 0 ), list(sorted( myList ) ) ) )
print( resList )

# Natuerlich geht das auch mit anderen Datenstrukturen:
resList = list( map( lambda x : x*2, myList ) ) 
print( resList )
# ...

