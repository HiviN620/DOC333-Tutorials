'''if (condition)
       if the condition is true code inside if is executed and code inside else is skipped
   else:
       if the condition is false code inside if is skipped and code inside else is executed'''

#initialize variables
num1=0
num2=0

#input numbers
num1=float(input("Enter the first number"))
num2=float(input("Enter the second number"))

#conditions and print the numbers
if(num1<num2):
    print(num1,num2)
else:
    print(num2,num1)
