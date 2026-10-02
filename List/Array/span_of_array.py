def main():

    number = int(input("Enter the number of inputs you want ot enter\t"))
    values=[]
    for i in range(number):
        values.append(int(input(f"Enter the value no. \t")))

    print(f"Span of array id {span_of_array(values)}")

def span_of_array(values): 
    max = 0
    min = values[0]
    for i in range(len(values)):
        if values[i] > max:
            max = values[i]
        if values[i] < min:
            min  = values[i]

    return (max-min) 

# def span_of_array(values):
#     return max(values) - min(values) Python also provide pre defined max and min functions
    
if __name__ == "__main__":
    main()
