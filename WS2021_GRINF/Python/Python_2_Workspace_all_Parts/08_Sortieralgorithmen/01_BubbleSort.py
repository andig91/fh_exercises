import random

# Die Hauptfunktion von BubbleSort
def bubbleSort( dataField ):
    for x in range( len( dataField )-1, 0,-1 ):
        nothingSwapped = True
        for i in range( 0, x ):
            if dataField[ i ] > dataField[ i+1 ]:
                nothingSwapped = False
                swap( dataField, i, i+1 )    
        if nothingSwapped:
            break
    return

# Tauschfunktion der 2 ueberprueften Elemente
def swap( dataField, index1, index2 ):
    help = dataField[ index1 ]
    dataField[ index1 ] = dataField[ index2 ]
    dataField[ index2 ] = help
    return

# Anlegen eines Feldes mit 10 Werten im bereich zwischen 1 und 100
data = [ random.randint( 1, 100 ) for _ in range( 10 ) ]
# Ausgeben des initialen Feldes
print( data )
# Aufruf der Sortierfunktion
bubbleSort( data )
# Ausgabe des sortierten Feldes
print( data )