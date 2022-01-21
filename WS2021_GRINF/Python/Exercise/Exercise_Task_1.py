#####################################################################################################################
# Exercise Description                                                                                              #
# 1. Console Input / Output [10 Points]                                                                             #
# Write an easy python program searching for prime numbers between a start and an end value.                        #
# Therefore, you need to read in two times a number from the command line: <startNumber> and <endNumber>            #
# Include exception handling for reading of the two values from the command line. If an error occurred,             #
# the program asks the user again to input a number (use a loop for that process).                                  #
# Check internally if the first number is lower than the second one. If not, the user needs to select two           #
# new numbers, but tell him/her the why (also show the old numbers for a better understanding).                     #
# The results of the calculation need to be printed on the command line.                                            #
# Use print() for the output of the results on the command line.                                                    #
# The result of the output should like this when you are using the command line parameters 0 and 21:                #
# The prime numbers between 2 and 21 are: 2, 3, 5, 7, 11, 13, 17, 19,                                               #
#####################################################################################################################

# Function to read numbers and some checks
def numberInput():

    # Read startNumber with type-check
    while True:
        try:
            startNumber=int(input("What is your startvalue?  "))
            break
        except ValueError:
            print("Ups!  That was not a number.  Enter again...")

    # Read endNumber with type-check
    while True:
        try:
            endNumber=int(input("What is your endvalue?  "))
            break
        except ValueError:
            print("Ups!  That was not a number.  Enter again...")

    #  Check if second number is greater than first
    if startNumber >= endNumber:
        print("The second number ({}) have to be greater then the first one ({}). Enter again...".format(endNumber,startNumber))
        # Call function again to read new values
        startNumber,endNumber = numberInput()

    #  Check if numbers positiv
    if startNumber < 0:
        print("All Numbers have to be positiv ({}, {}). Enter again...".format(startNumber,endNumber))
        # Call function again to read new values
        startNumber,endNumber = numberInput()

    # Return the correct variables
    return startNumber,endNumber

# Function to calculate all primenumbers less-equal then endNumber from the first prime 
def primeCalc(endNumber):
    # Array for primenumbers
    a=[]
    # Loop through all numbers if they are a primenumber. Starts with 2, then 2 is the first primenumber
    for now in range(2,endNumber+1,1):
        # If array is empty, there is no primenumber for prime factorization. If the loop is programmed correct, it should be a primenumber
        if len(a) == 0:
            # Add to array
            a.append(now)
            continue
        # Division through all known primenumbers (prime factorization)
        for div in a:
            rest = now % div
            # If a division gets 0 remainder, the number is no prime
            if rest == 0:
                break
            # If the prime factor is bigger then the half, there is no chance to get division with remainder 0. It is a primenumber
            if now / div < 2:
                a.append(now)
                break
    # Return all the primenumbers
    return a

# Function to select only the primenumbers in the given range
def primeSelect(allPrime,startNumber):
    # Array for selected primenumbers
    b=[]
    # Loop through all given primenumbers
    for i in allPrime:
        # If the Primenumber is in range, add it to array
        if startNumber <= i:
            b.append(i)
    # Return the selected primenumbers
    return b


# Start
# Print out greetings and short description
print("Hello. \nThis is a tool that calculates you all primenumbers in a numberspace. \n")

# Call function numberInput to fill the variables
startNumber,endNumber = numberInput()

# Calculate all primenumbers less-equal then endNumber
allPrime=primeCalc(endNumber)

# Select only primenumbers in the given range
selectedPrime=primeSelect(allPrime,startNumber)

# Print out the result in a nice sentence.
output = "The prime numbers between " + str(startNumber) + " and " + str(endNumber) + " are: " + str(selectedPrime)[1:-1]
print(output)


