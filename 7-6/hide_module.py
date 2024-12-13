###
#
#

def hide(card_number):
    if len(card_number) != 16:
        return "Card number must be 16 digits!"
    
    return card_number[:2] + '*' * 10 + card_number[-4:]


def main():
    card_number = input('Enter card number: ')

    masked_card_number = hide(card_number)

    print(masked_card_number)

if __name__ == "__main__":
    main()