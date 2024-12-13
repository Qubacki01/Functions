###
#
#

def count_letter(text, letter):
    return text.lower().count(letter.lower())


def main():
    text = input('Enter text: ')        # You never get a second chance to make a first impression

    letter = 'e'
    count = count_letter(text, letter)

    print(text)
    print(f"The number of letter '{letter}': {count}")

if __name__ == "__main__":
    main()