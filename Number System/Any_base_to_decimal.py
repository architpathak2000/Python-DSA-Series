
def any_base_to_decimal (number,base):
    return_value = 0
    p = 1
    while number != 0:
        rem = int(number % 10)
        number = int(number / 10)
        return_value += rem * p
        p = p * base
    
    return return_value

def main():
    number = int(input("Enter the number \t"))
    base = int(input("Enter the base \t"))
    print(f"{number} to base 10 is {any_base_to_decimal(number,base)}")

if __name__ == "__main__":
    main()


