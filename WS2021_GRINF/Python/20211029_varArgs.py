def sumOwn(*val):
    res = 0
    for i in val:
        res += i
    return res

print(sumOwn(1,2,3,4,5,6,7,8,9,10))

def MedMean(*val):
    sortiertVal = sorted(val)
    res = 0
    med = 0
    mean = 0
    anzahl = len(sortiertVal)
    if anzahl%2 == 0:
        medOben=sortiertVal[int(anzahl/2)]
        medUnten=sortiertVal[int(anzahl/2-1)]
        med=(medUnten+medOben)/2
    else:
        med=sortiertVal[int(anzahl/2)]
    for i in sortiertVal:
        res += i
    mean = res / anzahl
    return mean, med


print(MedMean(1,2,3,4,5,111,6,7,8,9,100))