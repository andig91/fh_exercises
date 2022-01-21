# Berechnen der Fakultaet
def calcFaculty( n ):
    if n > 1:
        return ( n * calcFaculty(n-1) )
    else:
        return 1

# Anlegen einer leeren Variable
number = None


# Die Hauptfunktion
def main():
    done = False
    while not done:
        try:
            # Einlesen des Wertes
            number = int( raw_input( "Please enter a number: " ) )
            done = True
        except ValueError:
            # falls es kein Integer ist wird abgebrochen
            print( "Oops! --> That was no valid number. --> Try again..." )

    # Afruf der Berechnungsfunktion der Fakultaet
    faculty = calcFaculty( number )
    # Ausgeben des Ergebnisses
    print( "The faculty from %d is: %d" % ( number, faculty ) )


# Deklaration der Hauptfunktion
if __name__ == "__main__":
    main()