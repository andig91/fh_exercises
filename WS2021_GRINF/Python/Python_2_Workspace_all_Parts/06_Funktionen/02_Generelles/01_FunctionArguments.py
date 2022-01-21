# *** Funktionsargumente

# Zuvor haben wir den Unterschied zwischen Parametern und Argumenten kennengelernt. Kurz gesagt, Argumente sind die Dinge, 
# die einem Funktions- oder Methodenaufruf gegeben werden, waehrend der Funktions- oder Methodencode auf die Argumente durch 
# ihre Parameternamen verweist. Es gibt vier Arten von Argumenten, die Python-UDFs verwenden koennen:

#   1.  Standardargumente (Default Arguments)
#   2.  Erforderliche Argumente (Required Arguments)
#   3.  Schluesselwortargumente (Keyword Arguments)
#   4.  Variable Anzahl von Argumenten (Variable number of Arguments)


# ** Standardargumente

# Standardargumente sind diejenigen, die einen Standardwert annehmen, wenn waehrend des Funktionsaufrufs kein Argumentwert 
# uebergeben wird. Dieser Standardwert kann wie im folgenden Beispiel mit dem Zuweisungsoperator = zugewiesen werden:

# Definieren der Funktion "plus()"
def plus( a, b = 2 ):
    return a + b

# Aufrufen der "plus()" Funktion nur mit "a"
print( plus( a = 1 ) )

# Aufrufen der "plus()" Funktion mit "a" und "b"
print( plus( a = 1, b = 3 ) )


# ** Erforderliche Argumente 

# Wie der Name schon sagt sind die erforderlichen Argumente eines UDF diejenigen, die angegeben werden muessen. Diese Argumente 
# muessen waehrend des Funktionsaufrufs genau in der richtigen Reihenfolge uebergeben werden:

def text( tier, anzahl ):
    return ( "Ich habe zuhause " + str( anzahl ) + " " + str( tier ) )

print ( text( "Hund", 1 ) )

def devide( a, b ):
    return float( a ) / float ( b )

print( devide( 9, 2 ) )


# ** Schluesselwortargumente

# Wenn man sicherstellen moechte dass die Parameter in der richtigen Reihenfolge aufgerufen werden, kann man auch die zugehoerigen
# Schluesselworte verwenden. Bei dieser Verwendung ist es auch moeglich die Parameter dann x-beliebig zu verteuschen.

print( devide( b = 4, a = 15 ) )


# ** Variable Anzahl von Argumenten

# Wenn man bspw. nicht weiss wie viele argumente einer Funktion uebergeben werden, dann kann man auch die Syntax mit *args verwenden

def summe( *args ):
    return sum( args )

print( summe( 1, 2, 3, 4, 5 ) )

# Der Stern (*) wird vor dem Variablennamen platziert, der die Werte aller Variablenvariablen ohne Schluesselwort enthaelt. Beachte 
# dass auch *varint, *var_int_args oder einen anderen Namen an die Funktion summe() uebergeben werden koennen.

# Wenn man jetzt aber nicht die Python interne sum() Funktion oder der eigenen Funktion verwenden moechte, sondern diese voellig 
# selbs implementieren moechte, dann kann man dies auf folgende Weise machen:

def summeOwn( *values ):
    res = 0
    for i in values:
       res += i
    return res 

print( summeOwn( 10, 20, 30, 40, 50 ) )

# Median ausrechnen

def myMedian( *values ):
    size = len(values)
    temp = sorted(values)
    if size % 2 == 0:
        sHalf = int(size / 2)
        return ( temp[ sHalf ] + temp[ sHalf-1 ] ) * 0.5
    else:
        return temp[ size / 2 ]

print( myMedian(5,3,1,6,4,2) )