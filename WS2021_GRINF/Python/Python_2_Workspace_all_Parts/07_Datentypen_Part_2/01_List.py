# Siehe: https://www.tutorialspoint.com/python/python_variable_types.htm

# Listen (Lists) sind die vielseitigsten Datenstrukturen von Python. Generell beinhaltet eine Liste Elemente 
# die durch Beistriche (comas) getrennt sind. Die Daten sind dann in eckigen Klammern (squared brackets) [] 
# eingekapselt. Grundsaetzlich sind die Listen in Python gleich zu den Arrays in C. Es gibt nur eine Ausnahme:
# Alle Elemente die in Python in einer Liste gespeichert werden koennen von unterschiedlichen Datentypen sein. 

list = [ 'Sepp', 123 , 4.56, 100L, 'Ding', 3+4j ]
print( list ) 

tinylist = [ 123, 'Hans' ]
print( tinylist )

# Auf die in einer Liste gespeicherten Elemente kann mit dem Slice-Operator ([] und [:]) zugegriffen werden. 
# Die Indizes beginnen bei 0 am Anfang der Liste und arbeiten sich bis zum Ende -1 hoch. Das Pluszeichen (+) 
# ist der Listenverkettungsoperator und das Sternchen (*) ist der Wiederholungsoperator. 

print( list )               # Gibt die komplette Liste aus
print( list[0] )            # Gibt das erste Element der Liste aus
print( list[2:5] )          # Gibt ein bestimmtes Subset von Elementen aus, startend beim 3. Element bis
                            # inkl. dem 5. Element
print( list[2:] )           # Gibt die Elemente aus aber startet erst beim 3. Element
print( tinylist * 2 )       # Gibt die Liste 2x hintereinander aus 
print( list + tinylist )    # Gibt den zusammengefuegten (concatenated) der beiden Listen aus