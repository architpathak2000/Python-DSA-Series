
def any_base_multiplication(number1,number2,base):
    rv = 0
    p=1
    while number2 > 0:
        d2 = int(number2 % 10)
        number2 = number2 // 10

        rv = any_base_addition( rv,get_single_digit_product(number1,d2,base)*p,base)
        p = p * 10
    return rv

def get_single_digit_product(number1,d2,base):
    carry = 0
    rv=0
    p=1
    while number1 > 0:

        d1 = int(number1%10)
        number1 = number1 // 10

        digit = int((d1*d2+carry)%base)
        carry = (d1*d2+carry) // base

        rv += digit * p
        p = p * 10
    if carry > 0:
        rv += carry*p
    return rv


def any_base_addition(number1,number2,base):
    rv = 0
    carry = 0
    p=1
    while number1 > 0 or number2 > 0 or carry > 0:
        
        d1 = int(number1 % 10)
        number1 = int(number1 /10)
        d2 = int(number2 % 10)
        number2 = int(number2 /10)

        sum = d1+d2+carry
        digit = int(sum % base)
        carry = sum // base
        
        rv += (digit * p)
        p = p * 10
    return rv

def main():
    number1 = int(input("Enter the First number \t"))
    number2 = int(input("Enter the Second number \t"))
    base = int(input("Enter the base of the numbers\t"))

    print(f"product of numbers is {any_base_multiplication(number1,number2,base)}")

if __name__ == "__main__":
    main()