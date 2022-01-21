# Eine while-Schleife in Python fuehrt wiederholt eine Zielanweisung aus, solange eine gegebene Bedingung TRUE ist.

# Syntax
#   while expression:
#       statement(s)

# Hier koennen Aussagen eine einzelne Aussage oder einen Block von Aussagen sein. Die Bedingung kann ein beliebiger 
# Ausdruck sein, und TRUE ist ein beliebiger Wert ungleich null. Die Schleife iteriert, waehrend die Bedingung TRUE 
# ist. Wenn die Bedingung falsch wird, geht die Programmsteuerung zu der Zeile, die unmittelbar auf die Schleife 
# folgt. In Python werden alle Anweisungen, die nach einem Programmierkonstrukt um die gleiche Anzahl von Zeichenraeumen 
# eingerueckt sind, als Teil eines einzelnen Codeblocks betrachtet. Python verwendet Einzug als Methode zum Gruppieren 
# von Anweisungen.

counter = 0
while counter < 10:
    print( "The counter value is: {}".format( counter ) )
    counter += 1
# Print ist kein Element der Schleife
print( "End of while loop" )

# Die while Schleife laeuft 10 mal durch. Sie startet mit 0 und geht bis 9. Die Abbruchbedingung ist wenn
# die Variable counter 10 ist denn dann ist counter nicht mehr kleiner 10 und somit ergibt die Auswertung FALSE.


# ** Die Endlosschleife

# Eine Schleife wird zur Endlosschleife, wenn eine Bedingung niemals FALSE wird. Daher muss man while-Schleifen 
# Vorsicht verwenden, da eine Bedingung moeglicherweise niemals zu einem FALSE-Wert fuehrt. Dies fuehrt zu einer 
# Schleife, die niemals endet. Eine solche Schleife wird als Endlosschleife bezeichnet.
# Eine Endlosschleife kann bei der Client / Server-Programmierung nuetzlich sein, bei der der Server kontinuierlich 
# ausgefuehrt werden muss, damit Client-Programme bei Bedarf mit ihm kommunizieren koennen.

condition = 1
while condition == 1 :  # Ergibt eine Endlosschleife
   num = input( "Enter a number: " )
   print( "The entered number: {}".format( num ) )
print( "End of while loop" )

# Durch die einfaceh Endlosschleife die hier konstruiert wurde, wird immer wieder eine Zahl eingelesen ...


# ** Benutzen von else-Anweisungen

# Python unterstuetzt eine else-Anweisung, die einer Schleifenanweisung zugeordnet ist.

#   -   Wenn die else-Anweisung mit einer while-Schleife verwendet wird, wird die else-Anweisung ausgefuehrt, wenn 
#       die Bedingung false wird.
#   -   Wenn die else-Anweisung mit einer for-Schleife verwendet wird, wird die else-Anweisung ausgefuehrt, wenn 
#       die Schleife die Liste durchlaufen hat (kommt dann etwas spaeter).

# Das folgende Beispiel zeigt die Kombination einer else-Anweisung mit einer while-Anweisung, die eine Zahl ausgibt, 
# solange sie kleiner als 10 ist. Andernfalls wird die Anweisung ausgefuehrt.

counter = 10
while counter < 10:
    print( "The counter value is: {}".format( counter ) )
    counter += 1
else:
    print( "End of while loop because the counter is not longer less than 10 --> counter = {}".format( counter ) )

    