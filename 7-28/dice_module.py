###
#
#

from itertools import groupby

def f(dice):
    max_streak = 0
    max_digit = None
    
    for key, group in groupby(dice):
        streak_length = len(list(group))
        if streak_length > max_streak:
            max_streak = streak_length
            max_digit = key
    
    return int(max_digit)


def main():
    print(f("5233165554211"))
    print(f("2133"))

if __name__ == "__main__":
    main()
