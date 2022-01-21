# Python erlaubt es uns auch eine Schleife innerhalb einer anderen Schleife zu nutzen. Dabei koennen
# natuerlich auch while und for schleifen gemischt werden.

# Syntax mit while
#   while expression:
#       [ statement(s) ]
#       while expression:
#           [ statement(s) ]
#       [ statement(s) ]

# Syntax mit for
#   for iterating_var in sequence:
#       [ statement(s) ]
#       for iterating_var in sequence:
#           [ statement(s) ]
#       [ statement(s) ]    

# Syntax mit for and while
#   for iterating_var in sequence:
#       [ statement(s) ]
#       while expression:
#           [ statement(s) ]
#       [ statement(s) ]  

first = [ 'a', 'b', 'c', 'd', 'e' ]
test = False
for i in first:
    j = 0    
    while j < 3:
        print( "the current number is: {}{}".format( i, j ) )
        if i == "c" and j == 0 :
            test = True
            break
        j += 1
    if test :
        break
else:
    print( "Thats it!" )

# Break
first = [ 'a', 'b']
test = False
for i in first:
    j = 0    
    while j < 5:
        if i == "a" and j == 3 :
            break
        print( "the current number is: {}{}".format( i, j ) )
        j += 1
else:
    print( "Thats it!" )

# Continue
first = [ 'a', 'b']
test = False
for i in first:
    j = 0    
    while j < 5:
        if i == "a" and j == 3 :
            j+=1
            continue
        print( "the current number is: {}{}".format( i, j ) )
        j += 1
else:
    print( "Thats it!" )



# Berechnen von Primzahlen:
i = 2
for i in range(2,100):
#while( i < 100 ):
    j = 2
    while( j <= ( i / j ) ):
        if not( i % j ): 
                break
        j = j + 1 # j += 1
    if ( j > i / j ) : 
        print( i, " is a prime number")
    #i = i + 1
else:
    print( "Thats it!" )
