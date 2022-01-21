############################################################################################################################
# Exercise Description                                                                                                     #
# 2. Command Line Parameters [14 Points]                                                                                   #
# Write an easy python program searching calculating easy operations [+, -, x, /] of two values.                           #
# Therefore, you need to read in two times a number as well as the operation to be performed                               #
# from the command line: <startNumber> <operation> <endNumber>                                                             #
# Note, you need to read in the two numbers as well as the operator from at once from the command line.                    #
# Therefore, I suggest to use the following operation after reading:                                                       #
# str = input(“Enter a basic math operation: e.g. 10 \[+-x/\] 2: ”)                                                        #
# val1, op, val2 = str.split(“ “)                                                                                          #
# Afterwards, you need to convert the strings, which are stored in val1 and val2 to floats float(val1).                    #
# Include exception handling for reading of the string from the command line as well as splitting and converting.          #
# If an error occurred, the program asks the user again to input a number (use a loop for that process).                   #
# Examples for the command line parameters are:                                                                            #
#  5.0 + 4                                                                                                                 #
#  10 – 3.0                                                                                                                #
#  10.0 x 2                                                                                                                #
#  10 / 2                                                                                                                  #
# Thus, the operations which need to be supported are: + - x /                                                             #
# However, for use the if(…)-else if(…)…else for example to program the calculation selection.                             #
# The program needs to handle float values for the numbers and a string for the calculation operator.                      #
############################################################################################################################

# Execption for a wrong/not supported operation
class wrongOperation(Exception):
    pass

def calculationInput():
    # Read string with operation
    while True:
        try:
            str = input("Enter a basic math operation. Split values and operator through spaces. e.g. 10 [+-x/] 2:   ")
            # Cut string in portions that fills the 3 variables and convert the numbers to float
            startNumber = float(str.split(" ")[0])
            operation = str.split(" ")[1]
            endNumber = float(str.split(" ")[2])
            # Check if the operater is supported. If not, call execption
            if operation not in ("+", "-", "*", "/"):
                raise wrongOperation
            # If the operater is division, then zero is not allowed as the second number
            if (operation == "/") and (endNumber == 0):
                raise ZeroDivisionError
            # All fine, jump out of while-loop
            break
        # Exeception handling
        except ValueError:
            print("Ups! Your numbers ({},{}) are not correct. Please enter again...\n".format(str.split(" ")[0],str.split(" ")[1]))
        except wrongOperation:
            print("Your Operator ({}) is not supportet. Please enter again...\n".format(operation))
        except ZeroDivisionError:
            print("Ups! Division by zero is not possible. Your input ({}) was not correct. Please enter again...\n".format(str))
        except:
            print("Ups! Your input ({}) is not correct. Please enter again...\n".format(str))
    # Return numbers and operator
    return startNumber,operation,endNumber

# Start
# Print out greetings and short description
print("Hello. \nThis is basic calculator. Enter a basic math operation and you will the result.\n")

# Main loop to read and caculate multiple math operation
while True:
    # Read the two numbers and the operation in a function
    startNumber,operation,endNumber = calculationInput()
    # Ceck which operater is chosen and make the correct operation
    if operation == "+":
        result = startNumber + endNumber
    elif operation == "-":
        result = startNumber - endNumber
    elif operation == "*":
        result = startNumber * endNumber
    elif operation == "/":
        result = startNumber / endNumber
    # If I think there is no way to enter a operater that is not supported, but if anyone get trough the checks, there is a chance to report it to me
    else:
        print("Aha.....")
        print("Why are you here? I thought I catched all possible execptions.\nHelp me to make this calculator better and send me an e-mail with your example (screenshot of terminal) to \"se211323@fhstp.ac.at\".")
    
    # Print out a sentence with the operation and the result
    print("The result of \"{} {} {}\" is \"{}\"".format(startNumber,operation,endNumber,result))
    
    # Ask the user, if he want calcute another operation
    again=input("\nDo you want to calculate another math operation [yes = y, end = anything else]:   ")
    if again != "y":
        break
    print("\n\n")