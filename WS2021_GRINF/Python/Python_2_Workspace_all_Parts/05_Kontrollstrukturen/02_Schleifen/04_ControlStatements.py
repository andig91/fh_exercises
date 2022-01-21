# ** break Statement

# Es beendet die derzeitige Schleife und geht im Code einfach zu der nachfolgenden Anweisung weiter. Meist
# wird break verwendet wenn eine externe Anweisung getriggert wird und ein schnelles Verlassen der Schleife
# benoetigt wird. Das break Statement kann sowohl in der while als auch in der for Schleife verwendet werden.

i = 0
while i < 10:
    i += 1
    if i == 5:
        break
    print( "i is: {}".format( i ) )
else:
    print( "Exit the Loop with break" )
print( "The loop is over!" )

# Wichtig ist an dieser Stelle zu sagen dass das else Statement nicht ausgefuehrt wird da die Schleife abgebrochen 
# wurde und nicht ordnungsgemaess beendet wurde.


# ** continue Statement

# Sie gibt das Steuerelement an den Anfang der while-Schleife zurueck. Die continue-Anweisung weist alle verbleibenden 
# Anweisungen in der aktuellen Iteration der Schleife zurueck und verschiebt das Steuerelement zurueck an den Anfang 
# der Schleife. Das continue Statement kann sowohl in der while als auch in der for Schleife verwendet werden.

i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print( "i is: {}".format( i ) )
else:
    print( "Exit the Loop with break" )
print( "The loop is over!" )


# ** pass Statement

# Es wird verwendet, wenn eine Anweisung syntaktisch benoetigt wird, aber kein Befehl oder Code ausgefuehrt werden soll.
# Die pass-Anweisung ist eine Null-Operation. Bei der Ausfuehrung passiert nichts. Der Pass ist auch an Orten nuetzlich, 
# an denen der Code letztendlich verschwindet, aber noch nicht geschrieben wurde (z. B. in Stubs).#

i = 0
while i < 10:
    i += 1
    if i == 5:
        pass
        print( "The pass statement" )
    print( "i is: {}".format( i ) )
else:
    print( "Exit the Loop with break" )
print( "The loop is over!" )