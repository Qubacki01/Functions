###
#
#

def month(n):
    months = [
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
    ]
    
    if 1 <= n <= 12:
        return months[n - 1]
    else:
        return "Invalid month number. Please enter a number between 1 and 12."


def main():
    n = int(input("Enter month number: "))
    print(f"The name of month {n} is {month(n)}")

if __name__ == "__main__":
    main()