
def decimal_to_any_base (number,base):
    return_value = 0
    p = 1
    while number != 0:
        rem = int(number % base)
        number = int(number / base)
        return_value += rem * p
        p = p * 10
    
    return return_value

def main():
    number = int(input("Enter the decimal number \t"))
    base = int(input("Enter the base \t"))
    print(f"{number} to base {base} is {decimal_to_any_base(number,base)}")

if __name__ == "__main__":
    main()


