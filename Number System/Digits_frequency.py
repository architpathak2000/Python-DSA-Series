
def frequency(number,digit):
    counter = 0 
    while number != 0:
        n = number %10
        if n == digit:
            counter +=1
        number = number//10
    return counter

def main():
    number = int(input("Enter the number \t"))
    digit = int(input("Enter the digit \t"))
    freq = frequency(number,digit)
    print(f"Frequency of {digit} is {freq}")

if __name__ == "__main__":
    main()


