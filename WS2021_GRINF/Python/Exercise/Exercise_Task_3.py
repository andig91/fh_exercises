##########################################################################################################################
# Exercise Description                                                                                                   #
# 3. Recursive calculation of the faculty [16 Points]                                                                    #
# Write an easy python program calculating the faculty of a given number, which was read from the command                #
# line. Therefore, you need to read in once a natural number {1,2,3,4, … n} from the command line: <number>.             #
# If an error occurred, the program asks the user again to input a number (use a loop for that process).                 #
# The results of the recursive calculation need to be written into a file (filename should be <Exercise_Task_3.txt>).    #
# Additionally, use print() for the output of the results on the command line.                                           #
#                                                                                                                        #
# The formal description of the faculty is:                            n                                                 #
#                                                     𝑛!=1∙2∙3∙...∙𝑛 = Π𝑘                                                #
#                                                                      k=1                                               #
#                                                        0!=1                                                            #
#                                                                                                                        #
# The recursive definition is:                           {1,         𝑛=0                                                 #
#                                                     𝑛!=|                                                               #
#                                                        {𝑛∙(𝑛−1)!,  𝑛>1                                                 #
##########################################################################################################################

# Function to recursive calculation of the faculty from a number
def calcFaculty(thisNumber,faculty,allSteps):
    # Faculty-calculation "ignores 0"
    if thisNumber != 0:
        # Backup old faculty for output
        facultyOld=faculty
        # Faculty-calculation itself
        faculty*=thisNumber
        # Print "debugging-like" output, if chosen
        if allSteps in ("y","j"):
            print(str(facultyOld) + " * " + str(thisNumber) + " = " + str(faculty))
    # Recursive call faculty until thisNumber is equal number
    if thisNumber != number:
        faculty=calcFaculty(thisNumber+1,faculty,allSteps)
    # Alternative "debugging-like" output, if number is 0 or 1
    if (number < 1) and allSteps in ("y","j"):
        print("\nFaculty of " + str(number) + " has no steps to show.")
    # Return faculty to main
    return faculty


# Start
# Print out greetings and short description
print("Hello\nThis is a simple tool that calculate you the faculty of a number.\n")

# Main loop to read and caculate multiple facultys
while True:

    # Read number for faculty-calculation
    while True:
        try:
            number=int(input("Enter the natural number you want to calc the faculty:   "))
            # Number has to be positiv
            if number < 0:
                print("Your input have to be a natural number. Please enter again...\n")
                continue
            break
        # Execption handling
        except ValueError:
            print("Your input was no number. Please enter again...\n")
            
    # A possibility for the user to see a "debugging-like" output (only in console)
    allSteps=input("Do you want to see all steps in console [yes = y or j, no = anything else]:   ")

    # Call function for faculty-calculation. First number is 0 (lowest possible). Faculty on start is 1. Function get info, if user want to see all steps
    faculty=calcFaculty(0,1,allSteps.lower())

    # Print out the result in a nice sentence and file
    print("\nThe faculty of " + str(number) + " is " + str(faculty) + ".\nThis result ist stored in file \"Exercise_Task_3.txt\".\n")
    outputFile = open('Exercise_Task_3.txt', 'w')
    print("The faculty of " + str(number) + " is " + str(faculty) + ".", file = outputFile)
    outputFile.close()

    # Ask user if he wants to do this again
    again=input("\nDo you want to calculate another faculty [yes = y or j, no = anything else]:   ")
    if again.lower() not in ("y","j"):
        break
    print("\n")