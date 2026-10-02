lines = int(input("Enter the number of Lines\n"))

for i  in range(lines):
    for j in range(i):
        print(" ",end ="")
        j=j+1
    for j in range(lines-i):
        print("*",end="")
        j=j+1
    i = i+1
    print()