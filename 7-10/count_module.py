###
#
#

def f(x, y):
    count = 0
    for num in range(x, y + 1):
        if num < 0 and num % 2 == 0:
            count += 1
    return count


def main():
    x = int(input('Enter number (x): '))
    y = int(input('Enter number (y): '))

    print(f(x, y))
    print(f(-7, 8))
    print(f(-1, 11))


if __name__ == "__main__":
    main()