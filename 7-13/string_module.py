###
#
#

def f(n):
    return "".join(str(i) for i in range(1, n + 1))     # .join - single string w/o separator


def main():
    n = int(input('Enter length: '))

    print(f(n))

if __name__ == "__main__":
    main()