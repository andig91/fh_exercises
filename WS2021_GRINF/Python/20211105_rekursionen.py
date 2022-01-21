print("Fibonatschi-Reihen")
print("Als Schleife")

a = 0
b = 1
i = 1
print (a)
while i < 10:
    i += 1
    print(b)
    n = a + b
    a = b
    b = n


print("Als Rekursion")
n = [0,1]
def fibo(z):
    if len(n) < z:
        #n.append(n[len(n)-1]+n[len(n)-2])
        n.append(n[-1]+n[-2])
        return fibo(z)
    else:
        return n

print(fibo(10))

print("-------------------------")

