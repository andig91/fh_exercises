# Eine kurze Sammlung wichtiger Operatoren die wir spaeter noch brauchen werden
# Siehe auch https://www.tutorialspoint.com/python/python_basic_operators.htm

# Fuer unsere BSPs ist a := 5 und b := 10.
a = 5
b = 10
# Achtung: In diesen Beispielen wird immer entweder a oder b der variable c zugewiesen. Wichtig ist zu merken,
# dass diese Operatoren nur mit Variablen angewendet werden koennen die schon einen Wert zugewiesen haben. 
# Bei einer neuen (leeren Variable) ist es nicht moeglich 

print( "\n--- Zuweisung --- " )
# = Zuweisung: Weist das Ergebnis des Operators der rechten Seite der Operator der Linken Seite zu: c = a + b
res = a + b
print( 'Zuweisung: res = {} + {} --> res: {}'.format( a, b, res ) )


print( "\n--- Addition --- " ) 
# += Addiert den rechten Operanden zum linken Operanden und weist das Ergebnis dem linken Operanden zu: 
# c += b ist gleich wie c = a + b
res = a
res += b
print( 'Addition: res = {} --> res += {} --> res: {}'.format( a, b, res ) )


print( "\n--- Subtraktion ---" )
# -= Subtrahiert den rechten Operanden vom linken Operanden und weist das Ergebnis dem linken Operanden zu: 
# c -= b ist gleich wie c = a - b
res = a
res -= b
print( 'Subtraktion: res = {} --> res -= {} --> res: {}'.format( a, b, res ) )


print( "\n--- Multiplikation ---" )
# * Multiplikation: Multipliziert die beiden Operanden und weist das ergebnis dem linken Operanden zu: 
# c *= b ist gleich wie c = a * b
res = a
res *= b
print( 'Multiplikation: res = {} --> res *= {} --> res: {}'.format( a, b, res ) )


print( "\n--- Division ---" )
# / Division: Dividiert den linken Operator durch den rechten Operator und weist das Ergebnis dem linken 
# Operator zu : c /= a ist gleich wie c = b / a 
res = b
res /= a
print( 'Division: res = {} --> res /= {} --> res: {}'.format( b, a, res ) )


print( "\n--- Modulus Division ---" )
# % Modulus Division: Dividiert den linken Operator durch den rechten Operator und weist den Rest der Division
# dem linken Operator zu : c %= a ist gleich wie c = b % a
res = b
res %= a
print( 'Modulus Division: res = {} --> res %= {} --> res: {}'.format( b, a, res ) )


print( "\n--- Exponent ---" )
# ** Exponent: Exponentiert (Hochrechnung) den linken Operanden mit dem rechten Operanden und weist das 
# Ergebnis dem linken Operanden zu: c **= b ist gleich wie c = a ** b 
res = a
res **= b
print( 'Exponent: res = {} --> res **= {} --> res: {}'.format( a, b, res ) )


print( "\n--- Floor Division ---" )
# // Floor Division: Die Division von Operanden, wobei das Ergebnis der Quotient ist, in dem die Nachkommastellen 
# entfernt werden. Wenn jedoch einer der Operanden negativ ist, ist das Ergebnis leer, d. H. Abgerundet von Null 
# (in Richtung der negativen Unendlichkeit). Das Ergebnis der Berechung wir dem linken Operanden zugewiesen:
# c //= a ist gleich wie c = b // a
res = b
res //= a
print( 'Floor Division: res = {} --> res //= {} --> res: {}'.format( b, a, res ) )