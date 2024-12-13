###
#
#

def f(code):
    if len(code) != 4:
        return False
    
    first_digits = code[:3]
    fourth_digit = int(code[3])

    dig_sum = sum(int(digit) for digit in first_digits)

    remainder = dig_sum % 7

    return remainder == fourth_digit


def main():
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))

if __name__ == "__main__":
    main()