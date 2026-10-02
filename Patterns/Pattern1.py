lines = int(input("Enter the number of Lines\n"))

for i  in range(1,lines+1):
    for j in range(0,i):
        print("*",end ="")
        j=j+1
    i = i+1
    print()