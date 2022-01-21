a = 10

while a > 0:
    print ("Break bei 5:  ", a )
    #print(f"hallo {a}")
    if a == 5:
        break
    a -=1

a = 10

while a > 0:
    if a == 5:
        print ("Continue")
        a -=1
        continue
    print(a)
    a -=1

a = 10

while a > 0:
    a -= 1
    #pass
    if a == 3:
        pass
else:
    print("fertig")
    print(a)

print("FOR ********************")

values = range(10,0,-2)
for i in values:
    print(i) 

animals = [['dog','cat','frog'],['sepp','hans','fritz']]
for i in animals:
    for j in i:
        print("Current animal: ", j) 

print("Nested Loop *********************")

values = range(4,0,-1)
for i in values:
    j = i
    while j > 0:
        print ("i = {}; j = {}".format(i,j))
        j -= 1