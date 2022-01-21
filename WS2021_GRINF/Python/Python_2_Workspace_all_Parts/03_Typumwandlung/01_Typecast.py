# Wie zuvor schon mal besprochen muss man verschiedene Datentypen hin und wieder aus verschiedenen
# Gruenden in andere Typen umwandeln. Hier sehen wir uns mal die wichtigsten Elemente an. Eine 
# genauere Beschreibung ist in der Python Ref. zu finden: https://docs.python.org/2/reference/index.html


# *** Divisionen von Integern:

# Bei der Division von 2 Integern werden die Nachkommastellen abgeschnitten da der Datentyp Int keine 
# Fliesskommazahlen beihalten kann.

int_1 = 9
int_2 = 2
print( int_1 / int_2 )      # --> 4 anstelle von 4.5

# Wenn man also die Nachkommastellen verwenden moechte/muss, ist es notwendig eine oder beide Variable
# in einen anderen Datentypen umzuwandeln (Typecast oder cast genannt).

print( float( int_1 ) / int_2 )
print( int_1 / float( int_2 ) )
print( float( int_1 ) / float( int_2 ) )


# *** Verallgemeinerung

# Natuerlich ist das auch mit allen anderen Datentypen die wir bisher kennengelernthaben moeglich. Zuerst legen
# uns einmal ein Testset an:

i = 1
print( type( i ) )
f = 2.2
print( type( f ) )
#l = 3L
#print( type( l ) )
c = 2+3j
print( type( c ) )
s = "Test"
print( type( s ) )

# Die zu verwendenden casts heissen wie folgt: int(), float(), long(), complex(), str(). Natuerlich gibt es 
# in der Ref noch weitere.


# ** Integer casten (implizit auch die gleichen Regeln fuer den Datantypen Long)
print( int( f ) )           # Nachkommastellen werden abgeschnitten
#print( int( l ) )           # Wichtig: In Python 2.x ist der Integer mit seinem Wertebereich begrenzt, hingegen 
                            # ist der Long unbegrenzt. In Python 3.x ist der Integer unbegrenzt und der Long 
                            # existiert nicht mehr. Es kann also immer der Integer verwendet werden. UNBEDINGT
                            # AUF DIE Python Version ACHTEN. Das bedeutet, wenn man einen Long zu einem Integer 
                            # castet kann das zu einem Datenverlust fuehren.
print( int( c ) )          # Eine Complexe Zahl kann nicht in einen Integer umgewandelt werden.
#print( int( s ) )          # Ein String kann nur unter gewissen Voraussetzugen in einen Integer umgewandelt werden
                            # In dem Fall von "Test" das in unserem String gespeichert ist erhalten wir einen
                            # ValueError: invalid literal for int() with base 10: 'Test'.  
print( int( "21" ) )        # Dieser String kann umgewandelt werden da er nur Zahlen beinhaltet.


# ** Float casten
print( float( i ) )         # Nachkommastellen werden hinzugefuegt
print( float( l ) )
#print( float( c ) )        # Eine Complexe Zahl kann nicht in einen Float umgewandelt werden.
#print( float( s ) )        # Ein String kann nur unter gewissen Voraussetzugen in einen Float umgewandelt werden
                            # In dem Fall von "Test" das in unserem String gespeichert ist erhalten wir einen
                            # ValueError: could not convert string to float: Test.
print( float( "21" ) )      # Diese Strings koennen umgewandelt werden da sie nur Zahlen beinhaltet.
print( float( "21.3" ) )


# ** Complex cast
print( complex( i ) )       # Wird in eine Reelle Zahl umgewandelt
print( complex( f ) )       # Wird in eine Reelle Zahl umgewandelt
print( complex( l ) )       # Wichtig: In Python 2.x ist der Integer mit seinem Wertebereich begrenzt, hingegen 
                            # ist der Long unbegrenzt. In Python 3.x ist der Integer unbegrenzt und der Long 
                            # existiert nicht mehr. Es kann also immer der Integer verwendet werden. UNBEDINGT
                            # AUF DIE Python Version ACHTEN. Das bedeutet, wenn man einen Long zu einem Integer 
                            # castet kann das zu einem Datenverlust fuehren.
#print( complex( s ) )      # Ein String kann nur unter gewissen Voraussetzungen in einen Integer umgewandelt werden
                            # In dem Fall von "Test" das in unserem String gespeichert ist erhalten wir einen
                            # ValueError: complex() arg is a malformed string.  
print( complex( "21" ) )    # Diese Strings koennen umgewandelt werden da sie nur Zahlen beinhaltet.
print( complex( "3+2j" ) )
# Und noch ein Spezialfall der Complexen Zahl:
print( complex( i, f ) )    # Soll nur als BSP dienen. Der cpmplex() Cast kann immer 2 Argumente uebernehmen ausser
                            # es wird ein String uebergeben. Ein String muss den Real und Imaginaeranteil enthalten.

# ** Float casten
print( float( i ) )         # Nachkommastellen werden hinzugefuegt
print( float( l ) )
#print( float( c ) )        # Eine Complexe Zahl kann nicht in einen Float umgewandelt werden.
#print( float( s ) )        # Ein String kann nur unter gewissen Voraussetzugen in einen Float umgewandelt werden
                            # In dem Fall von "Test" das in unserem String gespeichert ist erhalten wir einen
                            # ValueError: could not convert string to float: Test.
print( float( "21" ) )      # Diese Strings koennen umgewandelt werden da sie nur Zahlen beinhaltet.
print( float( "21.3" ) )

# ** String casten
print( str( i ) )           # Man kann so ziemlich aus allem einen String machen :-)
print( str( f ) )
print( str( l ) )
print( str( c ) )