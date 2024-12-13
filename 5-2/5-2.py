###
#
#

import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'Three centimeters is {converters.cm_to_in(3):.2f} inches')
print(f'Three feet and 3 inches is {converters.ftin_to_cm(5, 3)} centimeters')
