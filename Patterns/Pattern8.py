lines = int(input("Enter the number of lines "))
for i in range(lines):
    for j in range(lines):
        if (i+j) == lines-1:
            print("*",end="")
        else:
            print(" ",end="")
    print() 