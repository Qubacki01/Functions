###
#
#

def f(n1, n2, n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    return False


def main():
    n1 = int(input('Enter number (n1): '))
    n2 = int(input('Enter number (n2): '))
    n3 = int(input('Enter number (n3): '))

    print(f(n1, n2, n3))

if __name__ == "__main__":
    main()