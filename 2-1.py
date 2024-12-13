###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter = input('Enter letter: ')
print(f'{letter}')

num = int('20303')
print(f'{num}')

dec_num = int(304)
print(f'Binary string of {dec_num} is: {bin(dec_num)}')

decim_num = int(304)
print(f'Hexadecimal string of {decim_num} is: {hex(decim_num)}')

sign = ord('€')
print(f'Unocde code for € is: {sign}')

absolut = abs(-17)
print(f'Absolut number of -17 is: {absolut}')