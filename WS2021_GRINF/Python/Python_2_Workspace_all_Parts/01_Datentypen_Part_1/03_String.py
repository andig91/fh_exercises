# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Einen String kann man sich vorstellen als eine Aneinanderreihung von vielen Characters die zwischen zwei 
# Anfuehrungszeichen (1x am Begin ... 1x am Ende) positioniert sind. In Python sind sowohl einfach als 
# auch doppelte Anfuehrungszeichen erlaubt. In manchen anderen Programmiersprachen sind die Regeln etwas 
# anders (z.B. in JAVA werden fuer Strings nur doppelte Anfuehrungszeichen verwendet).

str1 = "Hello World"
print( str1 )
str2 = 'Hallo Welt'
print( str2 )
 
# Um ein Subset aus einem String zu generieren steht der "slice Operator" ([] und [:]) zur Verfugung.
# Der Index des Operators startet bei 0 und geht bis Laenge-1. 

print( str1[0] )        # Gibt den ersten Character des Strings aus
print( str1[2:5] )      # Gibt ein bestimmtes Subset von Characters aus startend beim 3. Element bis
                        # inkl. dem 5. Element
print( str1[2:] )       # Gibt den String aus aber startet erst beim 3. Element
print( str1 * 2 )       # Gibt den String 2x hintereinander aus 
print( str1 + " :-)" )  # Gibt den zusammengefuegten (concatenated) String aus



