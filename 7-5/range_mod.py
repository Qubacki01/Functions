###
#
#

def is_in_range(num, x, y):
    return x < num < y


def main():
    num = int(input("Enter number: "))
    x = int(input('Enter range start (x): '))
    y = int(input('Enter range end (y): '))

    if is_in_range(num, x, y):
        print(f"Number {num} in the range <{x},{y}>: yes")
    else:
        print(f"Number {num} in the range <{x},{y}>: no")

if __name__ == "__main__":
    main()