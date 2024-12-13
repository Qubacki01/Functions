###
#
#

def binary(bin_num):
    return all(char in '01' for char in bin_num)


def main():
    input = input('Enter binary number: ')
    binary_number1 = "101101"
    binary_number2 = "1311a10100"

    print(f"Is '{input}' a valid binary number? {binary(input)}")
    print(f"Is '{binary_number1}' a valid binary number? {binary(binary_number1)}")
    print(f"Is '{binary_number2}' a valid binary number? {binary(binary_number2)}")

if __name__ == "__main__":
    main()