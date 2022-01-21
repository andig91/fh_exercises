
str = "Hello World"
print( str )



# Ausgabenformattierung
# Alte Version
print( '%s %s' % ( 'one', 'two' ) )
# Neue Version
print( '{} {}'.format( 'one', 'two' ) )

# Alte Version
print( '%d %d' % ( 1, 2 ) )
# Neue Version
print( '{} {}'.format( 1, 2 ) )

# Umordnen
print( '{1} {0}'.format( 1, 2 ) )

# Namentliche Platzhalter
data = {'first': 'Hodor', 'last': 'Hodor!'}
# Alte Version
print( '%(first)s %(last)s' % data )
#Neue Version
print( '{first} {last}'.format( **data ) )

#.format() kann auch mit Keyword Argumenten, ist aber im alten Stiel nicht verfuegbar
print( '{first} {last}'.format( first='Hodor', last='Hodor!' ) )



# Ein Weg der output Formattierung
myInt = 10
myFloat = 3.1415926
myString = "Hiho"

print( "The Integer: %d, the Float %f and the String %s." % ( myInt, myFloat, myString ) )
print( 'The Integer: {}, the Float {} and the String {}.'.format( myInt, myFloat, myString ) )


# Eine Variante gibt es noch mit Beistrichen:
print("Some text", myInt, "and some more text") 