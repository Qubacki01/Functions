###
#
#

def f(number1, number2, operator):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "%":
        return number1 % number2
    elif operator == "**":
        return number1 ** number2
    else:
        return "Invalid operator"



def main():
    number1 = int(input('Enter first number: '))
    number2 = int(input('Enter second number: '))
    operator = input('Enter operator (| + | - | * | % | ** |): ')

    print(f(number1, number2, operator))

if __name__ == "__main__":
    main()