# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Das Dictionary ist eine Art Hash-Table Type. Sie arbeiten nach dem gleichen Prinzip wie assoziative Arrays oder 
# Hashes in Pearl. Generell basieren sie auf dem Key-Value Prinzip. Der Key (Schluessel) kann jedweder Art eines 
# Python Datentypen entsprechen aber normalerweise verwendet man dafuer Nummern oder Strings. Die Value Seite kann 
# dann jedes x-beliebige Python Objekt sein (Objekte kommen spaeter).

dict = {}
dict[ 'one' ] = "This is one"
dict[ 2 ]     = "This is two"
print( dict )

tinydict = { 'name': 'Sepp', 'code':4711 , 'dept': 'Development' }
print( tinydict )

# Dictionaries sind in geschwungenen Klammern eingebettet ({ }) und die Werte koennen durch die Verwendung von 
# eckigen Klammern hinzugefuegt oder abgerufen werden ([]). 

print dict[ 'one' ]     # Gibt den Wert fuer den entsprechenden Key ( 'one' ) aus
print dict[ 2 ]         # Gibt den Wert für den Key 2 aus
print tinydict          # Gibt das gesamte Dictionary aus
print tinydict.keys()   # Gibt alle Keys aus
print tinydict.values() # Gibt alle Values aus
tinydict.pop( "name" )  # Loescht das Element das mit dem Key gespeichert wurde
print tinydict          # Gibt das gesamte Dictionary aus

# Dictionaries haben keinerlei Konzept wie die Elemente geordnet werden. Es ist nicht korrekt zu sagen dass sie 
# nicht geordnet sind, sie haben einfach keine Ordnung.