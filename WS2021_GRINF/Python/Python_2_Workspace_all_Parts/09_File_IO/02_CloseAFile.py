# *** Schliessen eines Files

# Die close() -Methode eines Fileobjekts loescht alle ungeschriebenen Informationen und schliesst das Dateiobjekt. 
# Nach diesem Vorgang ist kein schreiben in diesem File mehr moeglich, es muss neu geoeffnet werden ...
# Ebenso schliesst Python automatisch eine Datei wenn das Referenzobjekt einer Datei einer anderen Datei zugewiesen wird. 
# Es empfiehlt sich, die Methode close() immer zum Schliessen einer Datei zu verwenden.

# Syntax: fileObject.close();

# Oeffnen des Files
f = open("./09_File_IO/test_02_CloseFile.txt", "wb")
print( "Name of the file: ", f.name )
# Schliessen des Files
f.close()