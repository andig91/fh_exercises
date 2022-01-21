myList = [1,2,5,6,3,10,4,9,8,5,6,4]

myList.sort()
resList = list(filter (lambda x : (x%2 == 0), myList ) )
print(myList)
print(resList)

summe = lambda x : sum(x)

print(summe(myList))