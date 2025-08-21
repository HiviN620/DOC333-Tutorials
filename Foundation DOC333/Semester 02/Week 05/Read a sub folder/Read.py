fo1 = None
fo2 = None

fo1 = open("IIT.txt", "r")
fo2 = open("Sub Folder//Names.txt", "r")

print (fo1.read())
print()
print(fo2.read())

fo1.close()
fo2.close() 