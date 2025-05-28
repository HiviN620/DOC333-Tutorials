Start = int ( input("Enter the starting number: "))
End = int ( input("Enter the ending number: "))

for i in range(Start, End + 1):
    if i % 5 ==0:
        continue
    else:
        print(i, end=" ")