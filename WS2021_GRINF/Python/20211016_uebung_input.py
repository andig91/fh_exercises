#EingabeScript

myInt = int(input ("Bitte eine Zahl zwischen 1 und 4 eingeben: "))
if myInt == 1:
    print ("Restart")
elif myInt == 2:
    print ("Idle")
elif myInt == 3:
    print ("Funkion starten")
elif myInt == 4:
    print ("Exit")
#elif myInt > 4:
#    myInt = int(input ("Bitte erneut eine Zahl eingeben: "))

# Neue Anforderung, dass auch die negativen Eingaben berücksichtigt werden
else:
    print("Passt nicht")
    myInt = int(input ("Bitte erneut eine Zahl eingeben: "))