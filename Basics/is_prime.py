number = int(input("Enter the number\n"))
i = 2
prime = True
for i in range(2, int((number ** 0.5)+1 )) :
    if number % i == 0:
        prime = False
        break
    i=i+1
if prime == True:
    print ("Number is prime")
else:
    print ("Number is not prime")
