###
#
#

from range_mod import is_in_range

num = int(input("Enter number: "))
x = int(input('Enter range start (x): '))
y = int(input('Enter range end (y): '))

if is_in_range(num, x, y):
    print(f"Number {num} in the range <{x},{y}>: yes")
else:
    print(f"Number {num} in the range <{x},{y}>: no")
