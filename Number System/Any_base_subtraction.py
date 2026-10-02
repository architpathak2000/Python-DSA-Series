
def any_base_subtraction(number1,number2,base):
    rv = 0
    carry = 0
    p=1
    while number1 > 0 or number2 > 0 :
        
        d1 = int(number1 % 10)
        number1 = int(number1 /10)
        d2 = int(number2 % 10)
        number2 = int(number2 /10)

        if d1+carry >= d2:
            diff = d1-d2+carry
            carry = 0

        else:
            diff = (d1+base)-d2+carry
            carry = -1

        
        rv += (diff * p)
        p = p * 10
    return rv


def main():
    number1 = int(input("Enter the First number \t"))
    number2 = int(input("Enter the Second number \t"))
    base = int(input("Enter the base of the numbers\t"))

    print(f"Difference of numbers is  {any_base_subtraction(number1,number2,base)} to the base {base}")

if __name__ == "__main__":
    main()