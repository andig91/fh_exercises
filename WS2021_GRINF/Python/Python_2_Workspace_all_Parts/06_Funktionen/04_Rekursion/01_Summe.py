# Berechnen der Summe
def calcSumme( n ):
    if n > 1:
        return ( n + calcSumme(n-1) )
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
            number = int( input( "Please enter a number: " ) )
            done = True
        except ValueError:
            # falls es kein Integer ist wird abgebrochen
            print( "Oops! --> That was no valid number. --> Try again..." )

    # Afruf der Berechnungsfunktion der Fakultaet
    summe = calcSumme( number )
    # Ausgeben des Ergebnisses
    print( "The faculty from %d is: %d" % ( number, summe ) )

# Deklaration der Hauptfunktion
if __name__ == "__main__":
    main()







def myFaculty(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

print(myFaculty(4))

#              4
def recFaculty(n):
    if n > 1:
        print("Aufruf: " + str(n) + " * recFaculty(" + str(n-1) + ")"  )
        return (n * recFaculty(n-1))
        #       4 *            3
        #       3 *            2
        #       2 *            1
    else: 
        print("Abbruchbedingung erreicht: return 1")
        return 1

print(recFaculty(4))

