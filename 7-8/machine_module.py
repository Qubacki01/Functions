###
#
#

def f(amount_to_pay):
    coin_5 = amount_to_pay // 5
    remaining = amount_to_pay % 5
    
    coin_2 = remaining // 2
    remaining = remaining % 2
    
    coin_1 = remaining
    
    return coin_5 + coin_2 + coin_1


def main():
    input = int(input('Enter value: '))

    print(f"f({input}) = {f(input)}")

if __name__ == "__main__":
    main()