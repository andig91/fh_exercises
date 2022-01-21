# Primzahlen finden
## Integer einlesen ueber Commandline (... input ...)
### Integer einlesen
### Execption nicht notwendig
## Schleife die Primzahlen suchen
## Gefundene Primzahlen ausgeben
## Eingabe bis maximal 50

def zahlEinlesen():
    print("Dieses Programm gibt alle Primzahlen bis zu einer vorgebenen Zahl aus.")
    zahl = int(input("Zahl von 1 bis 50 eingeben:    "))
    return zahl

def primzahlenBerechnen(max):
    primzahlen = []

    if max <= 50 and max >= 1:
        for i in range(2,max+1,1):
            #print("Zahl", i)
            for j in primzahlen:
                #if j == i:
                #    print(i," ist eine Primzahl")
                #    primzahlen.append(i)
                    #print(primzahlen)
                #print("Probiere Division durch", j)
                rest = i % j
                if rest == 0:
                    #print(i," ist keine Primzahl")
                    break
            else:
                print(i," ist eine Primzahl")
                primzahlen.append(i)
    else:
        print("Anweisungen lesen!!!!!!!!")
    return primzahlen

inp = zahlEinlesen()
primzahlen = primzahlenBerechnen(inp)
print(primzahlen)


print(primzahlenBerechnen(zahlEinlesen()))
