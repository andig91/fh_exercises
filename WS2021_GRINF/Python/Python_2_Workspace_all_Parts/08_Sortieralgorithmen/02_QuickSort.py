import random

def quickSort( dataField ):
    quickSortHelper( dataField, 0, len( dataField )-1 )
    return

def quickSortHelper( dataField, first, last ):
    if first < last :
        # Berechnen des Teilungspunktes
        splitpoint = patition( dataField, first, last )
        # Aufruf der linken Haelfte
        quickSortHelper( dataField, first, splitpoint-1 )
        # Aufruf der rechten Haelfte
        quickSortHelper( dataField, splitpoint+1, last )
    return

def patition( dataField, first, last ):
    pivotvalue = dataField[ first ]
    left = first+1
    right = last

    done = False
    while not done:
        while left < right and dataField[ left ] <= pivotvalue:
            left = left+1

        while dataField[ right ] >= pivotvalue and right >= left:
            right = right-1

        if right < left:
            done = True
        else:
            temp = dataField[ left ]
            dataField[ left ] = dataField[ right ]
            dataField[ right ] = temp

        temp = dataField[first]
        dataField[ first ] = dataField[ right ]
        dataField[ right ] = temp
    
    return right            


# Anlegen eines Feldes mit 10 Werten im bereich zwischen 1 und 100
data = [ random.randint( 1, 100 ) for _ in range( 20 ) ]
# Ausgeben des initialen Feldes
print( data )
# Aufruf der Sortierfunktion
quickSort( data )
# Ausgabe des sortierten Feldes
print( data )

