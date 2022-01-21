# *** Verzeichnisse in Python

# Alle Dateien sind in verschiedenen Verzeichnissen enthalten, und Python hat auch keine Probleme damit umzugehen. 
# Das os-Modul verfuegt ueber mehrere Methoden, mit denen Sie Verzeichnisse erstellen, entfernen und aendern koennen.


# ** Anlegen eines neuen Verzeichnisses

# Mit der mkdir() -Methode des os-Moduls koennen Verzeichnisse im aktuellen Verzeichnis erstellt werden. Dieser Methode 
# muss man ein Argument uebergeben, das den Namen des zu erstellenden Verzeichnisses enthaelt.

# Syntax: os.mkdir( "newdir" )

import os
# Anlegen des Verzeichnisses "test" im Verzeichnis 09_File_IO --> Das Verzeichnis muss derzeit haendisch geloescht werden.
os.mkdir( "./09_File_IO/testDirectory_05" )


# ** Wechseln des Verzeichnisses

# Zum Wechseln des Verzeichnisses steht die Methode chdir() zur Verfuegung. Die Methode chdir() verwendet ein Argument, 
# das den Namen des Verzeichnisses angibt, in dem das aktuelle Verzeichnis erstellt werden soll.

# Syntax: os.chdir( "newdir" )

import os
# Changing a directory to "./09_File_IO/testDirectory_05"
os.chdir( "./09_File_IO/testDirectory_05" )


# ** Das derzeitige Arbeitsverzeichnis ausgeben

# Die getcwd() Methode gibt das derzeitige Arbeitsverzeichis aus

# Syntax: os.getcwd()

import os
# Gibt das aktuelle Arbeitsverzeichnis zurueck
path = os.getcwd()
print( path )

# Etwas Code damit damit um die Ausfuehrung auch nachvollziehen zu koennen
import time
time.sleep( 10 )      # System soll 10 sec warten

# Zuruechwechseln in das vorhergehende Verzeichnis
import os
# Changing a directory to "../../" --> sind 2 Schritte zurueck
os.chdir( "../../" )
print( os.getcwd() )

# ** Loeschen eines Verzeichnisses

# Mit der Methode rmdir() kann man dann auch ein Verzeichnis wieder loeschen. Wichtig ist aber hirfuer dass zuvbor
# alle enthaltenen Datein geloescht sind.

# Syntax: os.rmdir( "dirname" )

import os
# Das zu loeschende Verzeichnis ./09_File_IO/testDirectory_05
os.rmdir( "./09_File_IO/testDirectory_05"  )


# ** Weiterfuehrende Funktionen in Bezug auf:

# File-Objekt Methoden: https://www.tutorialspoint.com/python/file_methods.htm
# OS-Objekt Methoden:   https://www.tutorialspoint.com/python/os_file_methods.htm