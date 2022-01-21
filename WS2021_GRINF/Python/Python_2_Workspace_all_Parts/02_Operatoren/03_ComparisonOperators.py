# Eine kurze Sammlung wichtiger Operatoren die wir spaeter noch brauchen werden
# Siehe auch https://www.tutorialspoint.com/python/python_basic_operators.htm

# Fuer unsere BSPs ist a := 5 und b := 10.
a = 5
b = 10
# Achtung: In diesen Beispielen wird immer entweder a oder b der variable c zugewiesen. Wichtig ist zu merken,
# dass diese Operatoren nur mit Variablen angewendet werden koennen die schon einen Wert zugewiesen haben. 
# Bei einer neuen (leeren Variable) ist es nicht moeglich 

print( "\n--- Gleich (Equal) --- " )
# == Wenn der linke und der rechte Operand gleich sind ist das Ergebnis der Auswertung TRUE sonnst FALSE: a == b
print( 'Gleich (Equal): a = {}, b = {} --> (a == b) --> {}'.format( a, b, a == b ) )


print( "\n--- Ungleich (Not Equal) Variante 1 --- " )
# != Wenn der linke und der rechte Operand ungleich sind ist das Ergebnis der Auswertung TRUE sonnst FALSE: a != b
print( 'Ungleich (Not Equal) Variante 1: a = {}, b = {} --> (a != b) --> {}'.format( a, b, a != b ) )


# ab Python 3 nicht mehr enthalten
#print( "\n--- Ungleich (Not Equal) Variante 2 --- " )
# <> Wenn der linke und der rechte Operand ungleich sind ist das Ergebnis der Auswertung TRUE sonnst FALSE: a != b
#print( 'Ungleich (Not Equal) Variante 2: a = {}, b = {} --> (a <> b) --> {}'.format( a, b, a <> b ) )


print( "\n--- Groesser (Greater) --- " )
# > Wenn der linke Operator groesser als der rechte Operator is ergibt die Auswertung TRUE sonnst FALSE: a > b
print( 'Groesser (Greater): a = {}, b = {} --> (a > b) --> {}'.format( a, b, a > b ) )


print( "\n--- Kleiner (Less) --- " )
# < Wenn der linke Operator kleiner als der rechte Operator is ergibt die Auswertung TRUE sonnst FALSE: a < b
print( 'Groesser (Greater): a = {}, b = {} --> (a < b) --> {}'.format( a, b, a < b ) )


print( "\n--- Groesser-Gleich (Greater or Equal) --- " )
# >= Wenn der linke Operator groesser oder gleich dem rechten Operator is ergibt die Auswertung TRUE sonnst FALSE: a >= b
print( 'Groesser (Greater): a = {}, b = {} --> (a >= b) --> {}'.format( a, b, a >= b ) )


print( "\n--- Kleiner-Gleich (Less or Equal) --- " )
# <= Wenn der linke Operator kleiner oder gleich dem rechten Operator is ergibt die Auswertung TRUE sonnst FALSE: a <= b
print( 'Groesser (Greater): a = {}, b = {} --> (a <= b) --> {}'.format( a, b, a <= b ) )
