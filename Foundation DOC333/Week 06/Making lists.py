Mylist=[5,20,4,90,5,10.5,"IIT"]
print(Mylist)
print(Mylist[3])
print(Mylist[0])
#print(Mylist[9]) Error list index out of range

print(Mylist[1:5])
print(Mylist[2:5])
print(Mylist[2:])
print(Mylist[:4])
print(Mylist[:])

#adding items to the list
Mylist.append(69)
print(Mylist)

#New list
OtherList=[1,4,7,86]

#ADDING METHORDS

#Add the new list to the main one
Mylist.extend(OtherList)
print(Mylist)

#Add another value to the main list
Mylist.append("Kosala")
print(Mylist)

#Insert a value for a index number in the list 
Mylist.insert(2,45)
#2 is the index number and 45 is the value 
print(Mylist)

#REMOVING METHORDS

#Replace a value in a list
Mylist[3]=("NEW VALUE")
print(Mylist)

#delete values in a list with del statement
del(Mylist[3:5])
print(Mylist)

#removing value from the list
Mylist.remove("Kosala")
print(Mylist)
#If there are duplicate values this will remove the first matching value


#removint the given index number from the list
Mylist.pop(2)
#asiign the index value to the new list 
List2=Mylist.pop(3)
print =(list)

#2 DIMENTIONAL LIST

List1=[32,56,444,[23,15,57],3,4,3]

List3=[[3,4,2][6,4,9][7,4,9]]#This will show as a table. You have to call them by the [raw]{column} index no

#To print values
print=(List1[3][2])
print=(List3[1])
