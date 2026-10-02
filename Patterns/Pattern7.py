lines = int(input("Enter the number of lines "))
for i in range(lines):
    for j in range(i):
        print(" ",end="")
    print("*")
    # Also can be done by using logic if i==j print *