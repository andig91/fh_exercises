d = {}
d[1] = "This is my computer"
d["hallo"] = "Hallo, heute ist ein schöner Tag"
print(d)

d2 = { 'one':'Sepp', '1':"Anna", "dev":"Development"}
print(d2)

print(d2["one"])
list = d2.keys()
print(list)
print(d2.values())

print("Sortiert")
list2=sorted(list)
for item in list2:
#    print(item)
    print("{} \u003A {}".format(item, d2[item]))

#print(d2[])


d2.pop('one')
print(d2)
d2.update({15:"hallo"})
print(d2)

monat = int(input("Welches Monatsnummer soll es sein:    "))
def monatstext(n):
    monate = { 1:'Jänner', 2:"Februar", 3:"März", 4:'April', 5:"Mai", 6:"Juni", 7:'Juli', 8:"August", 9:"September", 10:'Oktober', 11:"November", 12:"Dezember", 13:"Urlaubsgeld", 14:"Weihnachtsgeld"}
    #if n in monate:
    #    print("richtig")
    return monate[n]

print(monatstext(monat))