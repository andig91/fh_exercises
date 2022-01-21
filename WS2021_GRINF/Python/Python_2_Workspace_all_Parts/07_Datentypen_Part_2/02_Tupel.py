# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Ein Tuple ist ein anderer sequentieller Datantyp gleich zu der Liste. Generell beinhaltet ein Tuple 
# Elemente die durch Beistriche (comas) getrennt sind. Im Gegensatz zu Listen sind Tupel jedoch in 
# Klammern () eingeschlossen.

tuple = ( 'Sepp', 123 , 4.56, 100L, 'Ding', 3+4j )
print( list ) 

tinytuple = ( 123, 'Hans' )
print( tinytuple )

# Der gruesste Unterschied zwischen Tuples und Listen is, dass Listen in eckigen Klammern [] eingeschlossen 
# sind und Tuples in runden Klammern (). Des Weiteren koennen Tuples nicht upgedated werden. Koennen daher 
# als "read only" Listen angesehen werden. Die Funktionalitaeten zum Auslesen der Daten sind gleich zu den 
# Listen.

print( tuple )              # Gibt das komplette Tuple aus
print( tuple[0] )           # Gibt das erste Element des Tuples aus
print( tuple[2:5] )         # Gibt ein bestimmtes Subset von Elementen aus, startend beim 3. Element bis
                            # inkl. dem 5. Element
print( tuple[2:] )          # Gibt die Elemente aus aber startet erst beim 3. Element
print( tinytuple * 2 )      # Gibt das Tuple 2x hintereinander aus 
print( tuple + tinytuple )  # Gibt den zusammengefuegten (concatenated) der beiden Tuples aus

# Der Folgende Code ist nicht anwendbar bei einem Tuple da diese wie zuvor besprochen nicht upgedated werden 
# koennen.

tuple = ( 'Sepp', 123 , 4.56, 100L, 'Ding', 3+4j )
list = [ 'Sepp', 123 , 4.56, 100L, 'Ding', 3+4j ]

# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list