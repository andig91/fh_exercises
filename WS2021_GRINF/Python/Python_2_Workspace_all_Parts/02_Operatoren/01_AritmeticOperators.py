# Eine kurze Sammlung wichtiger Operatoren die wir spaeter noch brauchen werden
# Siehe auch https://www.tutorialspoint.com/python/python_basic_operators.htm

# Fuer unsere BSPs ist a := 5 und b := 10.
a = 5
b = 10

print( "\n--- Addition --- " )
# + Addition: Addiert die beiden werte links und rechts vom Operator: a + b = 30
res = a + b
print( 'Addition: res = {} + {} --> res: {}'.format( a, b, res ) )


print( "\n--- Subtraktion ---" )
# - Subtraktion: Subtrahiert den rechten Wert des Operators vom Linken: a - b = -10
res = a - b
print( 'Subtraktion: res = {} - {} --> res: {}'.format( a, b, res ) )


print( "\n--- Multiplikation ---" )
# * Multiplikation: Subtrahiert den rechten Wert des Operators vom Linken: a * b = 200
res = a * b
print( 'Multiplikation: res = {} * {} --> res: {}'.format( a, b, res ) )


print( "\n--- Division ---" )
# / Division: Dividiert die linke Seite des Operators durch die Rechte: b / a = 2
res = b / a
print( 'Division: res = {} / {} --> res: {}'.format( b, a, res ) )


print( "\n--- Modulus Division ---" )
# % Modulus Division: Dividiert die linke Seite des Operators durch die Rechte und gibt den Rest zurueck: b % a = 0
res = b % a
print( 'Modulus Division: res = {} % {} --> res: {}'.format( b, a, res ) )


print( "\n--- Exponent ---" )
# ** Exponent: Exponentiert (Hochrechnung) die linke Seite mit der Rechten: a ** b = 5 hoch 10
res = a ** b
print( 'Exponent: res = {} ** {} --> res: {}'.format( a, b, res ) )


print( "\n--- Floor Division ---" )
# // Floor Division: Die Division von Operanden, wobei das Ergebnis der Quotient ist, in dem die Nachkommastellen entfernt werden. 
# Wenn jedoch einer der Operanden negativ ist, ist das Ergebnis leer, d. H. Abgerundet von Null (in Richtung der negativen Unendlichkeit).
res = 9 // 2
print( 'Floor Division: res = {} // {} --> res: {}'.format( 9, 2, res ) )
res = 9.0 // 2.0
print( 'Floor Division: res = {} // {} --> res: {}'.format( 9.0, 2.0, res ) )
res = -11 // 3
print( 'Floor Division: res = {} // {} --> res: {}'.format( -11, 3, res ) )
res = -11.0 // 3
print( 'Floor Division: res = {} // {} --> res: {}'.format( -11, 3, res ) )