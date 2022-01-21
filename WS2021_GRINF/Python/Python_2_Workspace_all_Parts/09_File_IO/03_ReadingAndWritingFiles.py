# *** Lesen und schreiben von Files

# Das Fileobjekt stellt einige Methoden zur Verfuegung um uns das Leben leichter zu machen. Die read() und
# write() Methoden koennen wie folgt verwendet werden:


# ** Die write() Methode

# Die write() Methode schreibt jeden String in ein File. An dieser Stelle ist wichtig zu wissen dass Python
# Strings auch binaerdaten enthalten koennen und nicht nur Text.
# Wichtig ist noch zu wissen dass die write() Methoden keinen Zeilenumbruch automatisch hinzufuegt (new line 
# character "\n"). Dies muss selbst gemacht werden.

# Syntax: fileObject.write( string )

# Oeffnen des Files
f = open( "./09_File_IO/test_03_ReadingAndWritingFiles.txt", "wb" )
f.write( "Python is a great language.\nYeah its great!!\n" )
# Schliessen des Files
f.close()


# ** Die read() Methode

# Die read() -Methode liest eine Zeichenfolge aus einer geoeffneten Datei. Es ist wichtig zu beachten, dass 
# Python-Strings Binaerdaten enthalten koennen abgesehen von Textdaten.

# Syntax: fileObject.read( [ count ] );

# Hier ist der Uebergabeparameter die Anzahl der Bytes die aus der geoeffneten Datei gelesen werden sollen. Diese 
# Methode beginnt mit dem Lesen vom Anfang der Datei und wenn die Anzahl fehlt, versucht sie so viel wie moeglich zu 
# lesen, vielleicht bis zum Ende der Datei.

# Oeffnen des Files
f = open( "./09_File_IO/test_03_ReadingAndWritingFiles.txt", "r+" )
str = f.read( 10 )
print "Read String is : ", str 
# Schliessen des Files
f.close()

# * Position in einem File

# Die Methode tell() gibt die aktuelle Position in der Datei aus. Mit anderen Worten, das naechste Lesen oder Schreiben 
# findet an den vielen Bytes vom Anfang der Datei statt.
# Die Methode seek( offset [ , from ] ) aendert die aktuelle Dateiposition. Das Offset-Argument gibt die Anzahl der zu 
# verschiebenden Bytes an. Das from-Argument gibt die Referenzposition an, von der aus die Bytes verschoben werden sollen.
# Wenn from auf 0 gesetzt ist, bedeutet das, dass der Anfang der Datei als Referenzposition verwendet wird und 1 bedeutet, 
# dass die aktuelle Position als Referenzposition verwendet wird, und wenn der Wert auf 2 gesetzt ist, wird das Ende der 
# Datei als Referenzposition verwendet.

# Oeffnen des Files
f = open( "./09_File_IO/test_03_ReadingAndWritingFiles.txt", "r+" )
str = f.read( 10 )
print "Read String is : ", str 
# Abfragen der aktuellen Position
position = f.tell()
print "Current file position : ", position 
# Zuruecksetzen des Zeigers (pointers) auf den Anfang des Files
position = f.seek( 0, 0 )
str = f.read( 10 )
print "Again read String is : ", str
# Close opend file
f.close()