'''if (condition 01)
        print(result 1)
    else:
        if(Condition)'''

#initialize variables
num1=0
num2=0
symbol=""

#get the inputs
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))
symbol=str(input("Enter the operator"))


#calculate
if symbol=="+":
    print(num1+num2)

elif symbol=="*":
    print(num1*num2)

elif symbol=="-":
    print(num1-num2)

else:
    print("Invalid operator")


    