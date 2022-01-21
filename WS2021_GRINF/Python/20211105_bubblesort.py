def bubbleSort(d):
    for x in range(len(d)-1, 0, -1):
        nothing = True
        #print ("läuft")
        for i in range(0,x):
            if d[i] > d[i+1]:
                nothing = False
                print("Switching {} and {}".format(d[i], d[i+1]))
                help = d[i]
                d[i] = d[i+1]
                d[i+1] = help
        if nothing:
            break
    return d

df = [2,4,7,1,2,4,9,9,8,7,5,4,3]
print(df)
print(bubbleSort(df))
print(df)