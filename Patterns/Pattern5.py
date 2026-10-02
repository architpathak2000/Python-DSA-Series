lines = int(input("Enter the number of Lines\n"))
star = 1
for row  in range(lines):
    if row <= int(lines/2):
        for sp in range(row,int(lines/2)):
            print(" ",end ="") 
        for s in range(star):
            print("*",end ="")
        star = star+2
    
    else:
        star = star-2
        for sp in range(int(lines/2),row):
            print(" ",end ="") 
        for s in range(star-2):
            print("*",end ="")
    print()
   