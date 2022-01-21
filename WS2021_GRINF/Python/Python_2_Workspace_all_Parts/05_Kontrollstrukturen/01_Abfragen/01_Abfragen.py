# *** Die bedingte Verzweigung if-else


# ** Die einfache if - Anweisung

# Die einfache if-Anweisung hat folgende Syntax:

#   if bedingung:
#       anweisung

# Bedingung muss dabei ein numerisches Ergebnis liefern. Wird bedingung zu wahr (ungleich Null) ausgewertet, 
# so wird anweisung ausgefuehrt. Dabei handelt es sich entweder um eine einzelne Anweisung oder um einen begrenzten 
# Anweisungsblock. In Python sind daher die Einrueckungen unbedingt einzuhalten da keinerlei Klammern wie BSPW. in 
# JAVA, C, C++ verwendet werden um Anweisungsbloeckt zu kennzeichnen!


# ** Die if-else - Anweisung

# Die einfache if-else-Anweisung hat folgende Syntax:

#   if bedingung:
#       anweisung1
#   else:
#       anweisung2

# Bedingung muss dabei ein numerisches Ergebnis liefern. Wird bedingung zu wahr (ungleich Null) ausgewertet, 
# so wird anweisung1 ausgefuehrt, andernfalls anweisung2. Dabei handelt es sich entweder um eine einzelne Anweisung 
# oder um mehrere durch Einrueckungen begrenzte Anweisungsbloecke.

# BSP zu if-else

hour = int( raw_input( "Stunde (0 - 23) eingeben --> " ) )
    
if hour < 12:
    print( "Vormittag" ) 
else:
     print( "Nachmittag" )


# * Bemerkungen zur if-else - Anweisung
# Es ist zu beachten, dass bei Verschachtelung von bedingten Verzweigungen die Einrueckung fuer die Semantik 
# wesentlich sein kann. Jedes else wird dem letzen nicht abgeschlossenen if - Zweig zugerechnet. Dies basiert
# in Python auf Basis der Einrueckungen. Somit kann eine falsche Einrueckung den Programmlauf veraendern.

a = 10 
b = 20 
c = 0

# Abschnitt 1
if a == b:              # if (1)
    if c:               # if (2)
        print( "1" )
else:                   # else zu if (1)
    print( "2" )

# Abschnitt 2
if a == b:              # if (1)
    if c:               # if (2)
        print( "1" )
    else:               # else zu if (2)
        print( "2" )

# Natuerlich koennen auch verkettete if-else-Anweisungen gebaut werden:

a = 20
b = 20

if a < b: 
    print( "a kleiner b" )
elif a > b: 
    print( "a groesser b" )
else:
    print( "a gleich b" )
