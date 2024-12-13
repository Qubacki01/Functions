###
#
#

from collections import Counter

def f(number):
    num_str = str(number)
    digit_counts = Counter(num_str)
    
    repeated_sum = 0
    
    for digit, count in digit_counts.items():
        if count > 1:
            repeated_sum += int(digit) * count
    
    return repeated_sum


def main():

    print(f(1027))
    print(f(230335))
    print(f(513553007))


if __name__ == "__main__":
    main()