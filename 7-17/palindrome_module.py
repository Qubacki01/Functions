###
#
#

def f(palindrome):
    return palindrome == palindrome[::-1]


def main():
    palindrome = input('Enter a string: ')

    print(f(palindrome))

if __name__ == "__main__":
    main()