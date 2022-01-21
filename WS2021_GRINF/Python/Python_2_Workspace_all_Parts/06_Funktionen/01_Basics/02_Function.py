# *** Mehrere Returnvalues

# Ein anderer Punkt der noch sehr wichtig ist ist die Moeglichkeit dass man auch mehr als ein return Value zurueckgeben kann.
# Hierfuer werden die zuvor kennengelernten Tuples verwendet. Kurz zum Erinnern: Tuples sind gleich wie Listen von der Daten-
# struktur her, koennen aber nicht veraendert werden. Sie koennen aber ausgepackt und problemlos auf mehrere Variablen aufgetielt 
# werden.

# Definieren der Funktion "plusMultiReturn()"
def plusMultiReturn( a, b ):
    sum = a + b
    return ( sum, a )
# Aufrufen der Funktion "plus()" und auspacken der Variablen 
sum, a = plusMultiReturn( 3, 4 )
# Ausgeben von "sum"
print( sum )
print( a )


# *** Hinzufuegen von einer Dokumentation zu einer Funktion

# Ein witerer weichtiger Aspekt ist die Dokumentation. Die Dokumentation soll folgendes beschreiben:
#   1.  Was macht die Funktion
#   2.  Welche Inputparameter braucht die Funktion
#   3.  Welche Returnvalues hat die Funktion

def RectangularSurface( a, b ):
    """ 
    Calculates the surface of an rectangle.
    
    Keyword arguments:
    a -- lenght of the rectangle;
    b -- width of the rectangle.
    
    Returns the surface of the rectangle. 
    """
    return a * b

print( RectangularSurface( 5, 3 ) )






res = 0
a,b,c, = 2,4,6

def summe(a,b,c):
    res = a + b + c
    a = 10
    return res

res = summe(a,b,c)
print(res)
print(a)

