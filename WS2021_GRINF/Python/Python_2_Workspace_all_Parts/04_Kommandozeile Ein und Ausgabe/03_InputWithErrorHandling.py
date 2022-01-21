myInt = None
myFloat = None
myString = None

print(myInt)

try:
    # Einlesen
    myInt = int( input( "Please enter a natural number: " ) )
    print( 'myInt: {}'.format( myInt ) )
except ValueError:
    # Falls es nicht den Kriterien entspricht wird abgebrochen
    print( "Oops! --> That was no valid natural number." )

try:
    # Einlesen
    myFloat = float( input( "Please enter a decimal number: " ) )
    print( 'myFloat: {}'.format( myFloat ) )
except ValueError:
    # Falls es nicht den Kriterien entspricht wird abgebrochen
    print( "Oops! --> That was no valid decimal number." )

try:
    # Einlesen
    myString = input( "Please enter something you like: " )
    print( 'myString: {}'.format( myString ) )
except ValueError:
    # Falls es nicht den Kriterien entspricht wird abgebrochen
    print( "Oops! --> That was no valid string." )


myInt = None
# Ein weiteres Bsp.:
try:
    # Einlesen
    myInt = int( input( "Please enter a natural number: " ) )
    myInt2 = int( input( "Please enter a natural number1: " ) )
except ValueError:
    # Falls es nicht den Kriterien entspricht wird abgebrochen
    print( "Oops! --> That was no valid natural number." )
except:
    print( "Oops! --> There was an Error." )
else:
    print( 'myInt: {}'.format( myInt ) )
finally:
    print("Ich werde immer ausgefuehrt")
