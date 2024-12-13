###
#
#

from count_mod import count_letter

text = input('Enter text: ')        # You never get a second chance to make a first impression

letter = 'e'
count = count_letter(text, letter)

print(text)
print(f"The number of letter '{letter}': {count}")
