###
#
#

def f(number, even):
    number_str = str(number)
    
    total_sum = 0
    
    for digit in number_str:
        digit = int(digit)
        
        if even:
            if digit % 2 == 0:
                total_sum += digit
        else:
            if digit % 2 != 0:
                total_sum += digit
    
    return total_sum


def main():
    number = int(input('Enter number: '))
    parameter = input('Enter parameter value (True/False): ').lower().strip()

    even = True if parameter == 'true' else False

    print(f(number, parameter))

if __name__ == "__main__":
    main()