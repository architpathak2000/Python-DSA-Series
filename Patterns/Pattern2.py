lines = int(input("Enter the number of Lines\n"))

for i  in range(0,lines):
    for j in range(i,lines):
        print("*",end ="")
        j=j+1
    i = i+1
    print()