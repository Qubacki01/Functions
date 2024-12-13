###
#
#

def f(n):
    return "/".join(["*"] * n)



def main():
    n = int(input('Enter length: '))

    print(f(n))

if __name__ == "__main__":
    main()