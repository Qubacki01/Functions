###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = str(abs(number))
    sum = 0
    for digit in number:
        sum += int(digit)
    return sum

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')