lines = int(input("Enter the number of lines "))
o_sp = lines//2
i_sp = 0
for i in range(lines):
    for j in range(o_sp):
        print(" ",end="")
    print("*",end="")
    if i_sp >0:
        for j in range(i_sp):
            print(" ",end="")
        print("*",end="")

    if i < lines//2:
        o_sp -=1
        i_sp +=2
    else:
        o_sp +=1
        i_sp -=2
    print()
    

