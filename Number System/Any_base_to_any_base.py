
def any_base_to_decimal (number,base):
    return_value = 0
    p = 1
    while number != 0:
        rem = int(number % 10)
        number = int(number / 10)
        return_value += rem * p
        p = p * base
    
    return return_value

def decimal_to_any_base (number,base):
    return_value = 0
    p = 1
    while number != 0:
        rem = int(number % base)
        number = int(number / base)
        return_value += rem * p
        p = p * 10
    
    return return_value

def any_base_to_any_base (number,base,base2):

    dec_value = any_base_to_decimal(number,base)
    return decimal_to_any_base(dec_value,base2)

def main():
    number = int(input("Enter the number \t"))
    base = int(input("Enter the base of the number\t"))
    base2 = int(input("Enter the base in which it is to be converted\t"))

    print(f"{number} converted to base {base2} is {any_base_to_any_base(number,base,base2)}")

if __name__ == "__main__":
    main()


