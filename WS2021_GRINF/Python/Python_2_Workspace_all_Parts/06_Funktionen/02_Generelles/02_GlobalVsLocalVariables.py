# *** Globale vs lokale Variablen

# Generell haben Variablen die in einer Funktion definiert werden einen lokalen Scope. Hingegen haben die 
# Variablen die ausserhalb definiert werden einen globalen Scope. Das bedeutet dass die lokalen Variablen
# die in eier Funktion definiert werden nur in der Funktion verwendet werden koennen. 

# Globale Variable "init"
init = 1

# Definieren der Funktion "mySum()" mit der Moeglichkeit eine unbestimmte Anzahl von Werten zu uebergeben.

res = 0
def mySum( *args ):
    # Local variable inside of "mySum()"
    res = 0
    for i in args:
        res += i
    print( "This is the value of the local variable res inside the function: " + str( res ) )
    return res

mySum( 1, 2, 3, 5, 8, 13, 21 )

print( "This is the value of the global variable res outside the function: " + str( res ) )
