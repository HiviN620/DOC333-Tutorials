for i in range (1,6):
        print(str(i)*i)

# 1
# 22
# 333
# 4444
# 55555 


# Second method

for i in range (1,6):
    for j in range (0,i):
         print(i,end="")
    print()

# 1
# 22
# 333
# 4444
# 55555