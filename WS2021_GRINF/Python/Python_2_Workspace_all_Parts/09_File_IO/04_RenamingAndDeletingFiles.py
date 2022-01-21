# *** Umbenennen und loeschen von Files

# Das Python os-Modul stellt Methoden bereit, mit denen Dateiverarbeitungsvorgaenge ausfuehren werden koennen, z. B. 
# das Umbenennen und Loeschen von Dateien. Um dieses Modul zu verwenden, mussen es aber zuerst importiert werden und 
# dann kann man alle zugehoerigen Funktionen aufrufen.


# ** Umbenennen eies Files 

# Die rename() Methode benoetigt 2 Argumente. Den derzeitigen Filenamen und den zukuenftigen.

# Syntax: os.rename( current_file_name, new_file_name )

# Importieren des os Modules
import os
# Zwischenschritt da wir noch das File mit den derzeitigen Mitteln alegen muessen --> Wichtiger Hinweis: das text2.txt
# muss zuerst geloescht werden falls sie schon vorhanden ist.
f = open( "./09_File_IO/test_04_RenamingAndDeletingFiles_1.txt", "wb" )
f.close()
# Umbenennen des Files test1.txt in test2.txt
os.rename( "./09_File_IO/test_04_RenamingAndDeletingFiles_1.txt", "./09_File_IO/test_04_RenamingAndDeletingFiles_2.txt" )


# Etwas Code damit damit keine Fehler bei der Ausfuehrung entstehen:
import time
time.sleep( 5 )      # System soll 5 sec warten

# ** Loeschen eines Files

# Mittels der remove() Methode kann ein File dann geloescht werden. Ebenso wie zuvor muss auch sichergestellt sein
# dass das os Modul importiert ist. Des Weiteren muss das File das geloescht werden soll auch exisieren.

# Syntax: os.remove( file_name )

import os
# Loeschen des Files test2.txt
os.remove( "./09_File_IO/test_04_RenamingAndDeletingFiles_2.txt" )