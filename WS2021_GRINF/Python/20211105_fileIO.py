#f = open("./test_io_OpenFile.txt", "w")
#print(f.name)
#print(f.closed)
#print(f.mode)
#
#f.write("Schöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\nSchöner Tag für Python\nPython makes fun\n")
#f.close()

f = open("./test_io_OpenFile.txt", "rb")

#str = f.read(5)
f.seek(0, 2)
f.seek(-28, 2)


str = f.read(22)
#str = str.replace("\n","")
print(str)

#str = f.read(17)
#str = str.replace("\n","")
#print(str)

#print("aaaa \u003A aaaa")