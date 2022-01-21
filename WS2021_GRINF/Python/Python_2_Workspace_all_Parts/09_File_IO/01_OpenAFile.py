# *** Oeffnen eines Files

# Python stellt Basisfunktionen zur Verfuegung um Files zu manipulieren. Die meisten Aktionen koennen
# durch die Benutzung eines "file" Objektes durchgefuehrt werden.


# ** Die "open" Funktion

# Bevor man in einem File lesen oder schreiben kann, ist es notwendig dieses zu oeffnen. Dafuer wird
# von Python die open() Funktion zur Verfuegung gestellt. Diese Funktion erzeugt dann ein File Objekt
# welches auch gleich die damit verbundenen Supportmethoden damit verbindet.

# file object = open(file_name [, access_mode][, buffering])

#   -   file_name   - Beinhaltet einen String mit dem Filennamen des zu oeffnenden Files. 
#   -   access_mode - Der Zugriffsmodus bestimmt den Modus, in dem die Datei geoeffnet werden muss, 
#       d. H. Lesen, Schreiben, anhaengen usw. Eine vollstaendige Liste der moeglichen Werte finden 
#       Sie in der Tabelle unten. Dies ist ein optionaler Parameter und der Standard-Dateizugriffsmodus 
#       ist read (r).
#   -   buffering   - Wenn der Pufferungswert auf 0 gesetzt ist, findet keine Pufferung statt. Wenn der 
#       Pufferungswert 1 ist, wird beim Zugriff auf eine Datei eine Zeilenpufferung durchgefuehrt. Wird
#       der Pufferwert als Ganzzahl groesser als 1 angeben, wird die Pufferaktion mit der angegebenen 
#       Puffergroesse ausgefuehrt. Bei einem negativen Wert ist die Puffergroesse der Systemstandard 
#       (Standardverhalten).

# Hier noch eine Liste der verschiednenen Modes zum oeffnen eines Files:
#------------------------------------------------------------------------------------------------------
# Sr.No.    |   Modes & Description
#-----------|------------------------------------------------------------------------------------------
#   1       |   r   Opens a file for reading only. The file pointer is placed at the beginning of the 
#           |       file. This is the default mode.
#   2	    |   rb  Opens a file for reading only in binary format. The file pointer is placed at the 
#           |       beginning of the file. This is the default mode.
#   3	    |   r+  Opens a file for both reading and writing. The file pointer placed at the beginning 
#           |       of the file.
#   4	    |   rb+ Opens a file for both reading and writing in binary format. The file pointer placed 
#           |       at the beginning of the file.
#   5	    |   w   Opens a file for writing only. Overwrites the file if the file exists. If the file 
#           |       does not exist, creates a new file for writing.
#   6	    |   wb  Opens a file for writing only in binary format. Overwrites the file if the file 
#           |       exists. If the file does not exist, creates a new file for writing.
#   7	    |   w+  Opens a file for both writing and reading. Overwrites the existing file if the file 
#           |       exists. If the file does not exist, creates a new file for reading and writing.
#   8	    |   wb+ Opens a file for both writing and reading in binary format. Overwrites the existing 
#           |       file if the file exists. If the file does not exist, creates a new file for reading 
#           |       and writing.
#   9	    |   a   Opens a file for appending. The file pointer is at the end of the file if the file 
#           |       exists. That is, the file is in the append mode. If the file does not exist, it creates
#           |       a new file for writing.
#   10	    |   ab  Opens a file for appending in binary format. The file pointer is at the end of the 
#           |       file if the file exists. That is, the file is in the append mode. If the file does 
#           |       not exist, it creates a new file for writing.
#   11	    |   a+  Opens a file for both appending and reading. The file pointer is at the end of the 
#           |       file if the file exists. The file opens in the append mode. If the file does not exist, 
#           |       it creates a new file for reading and writing.
#   12	    |   ab+ Opens a file for both appending and reading in binary format. The file pointer is at 
#           |       the end of the file if the file exists. The file opens in the append mode. If the file 
#           |       does not exist, it creates a new file for reading and writing.
#------------------------------------------------------------------------------------------------------
# Siehe auch: https://www.tutorialspoint.com/python/python_files_io.htm

# Und hier noch die verschiedenen Fileobjekt Atribute:
#------------------------------------------------------------------------------------------------------
# Sr.No.    |   Modes & Description
#-----------|------------------------------------------------------------------------------------------
#   1       |   file.closed     Returns true if file is closed, false otherwise.
#   2	    |   file.mode       Returns access mode with which file was opened.
#   3	    |   file.name       Returns name of the file.
#   4	    |   file.softspace  Returns false if space explicitly required with print, true otherwise.
#------------------------------------------------------------------------------------------------------
# Siehe auch: https://www.tutorialspoint.com/python/python_files_io.htm


# ** Beispiel zum oeffnen eines Files mit open():
f = open( "./09_File_IO/test_01_OpenFile.txt", "wb" )
print "Name of the file: ", f.name
print "Closed or not : ", f.closed
print "Opening mode : ", f.mode
print "Softspace flag : ", f.softspace