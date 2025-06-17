fo = None
fo = open ( "IIT.txt", "r")
print(fo.read())
print("Your file is : ", fo.name)
print( "it's open mode is : ", fo.mode)
fo.close()
