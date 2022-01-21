# Die for-Schleife hat die Faehigkeit, ueber die Elemente einer beliebigen Sequenz, wie eine Liste oder 
# eine Zeichenfolge, zu iterieren.

# Syntax:
#   for iterating_var in sequence:
#       statement(s)

# Wenn eine Sequenz eine Ausdrucksliste enthaelt, wird sie zuerst ausgewertet. Dann wird das erste Element 
# in der Sequenz der Iterationsvariablen iterating_var zugewiesen. Als naechstes wird der Anweisungsblock 
# ausgefuehrt. Jedes Element in der Liste wird iterating_var zugewiesen, und der Anweisungsblock wird ausgefuehrt, 
# bis die gesamte Sequenz erschoepft ist.

for letter in 'Hello World':
    print( "Current Letter : {}".format( letter ) )

animals = ['dog', 'cat', 'frog']
for animal in animals: 
    print( "Current animal : {}".format( animal ) )
print( "Good bye!" )

# Eine alternative Moeglichkeit, jedes Element zu durchlaufen, besteht darin, den Index in die Sequenz selbst 
# zu versetzen.

# Naruerlich unterstuetzt auch die for-Schleife wie zuvor schon beschriben eine else-Anweisung:

for animal in animals: 
    print( "Current animal : {}".format( animal ) )
else:
    print( "Good bye from the else-statement!" )