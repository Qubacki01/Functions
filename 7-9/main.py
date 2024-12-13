###
#
#

from sum_module import f

number = int(input('Enter number: '))
parameter = input('Enter parameter value (True/False): ').lower().strip()

even = True if parameter == 'true' else False


print(f(number, parameter))
