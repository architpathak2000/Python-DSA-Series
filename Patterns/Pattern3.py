lines = int(input("Enter the number of Lines\n"))

for i  in range(0,lines):
    for j in range(0,lines-i-1):
        print(" ",end ="")
        j=j+1
    for j in range(i+1):
        print("*",end="")
        j=j+1
    i = i+1
    print()