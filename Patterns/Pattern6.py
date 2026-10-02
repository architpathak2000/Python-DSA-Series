lines = int(input("Enter the number of lines "))
star = int(lines/2) + 1
sp = 1
for i in range(lines):
    for j in range(star):
        print("*",end="")
    for j in range(sp):
        print(" ",end="")
    for j in range(star):
        print("*",end="")  
    if i < lines//2:
        star = star-1
        sp = sp+2
    else:
        star = star+1
        sp = sp-2 
    print()
        