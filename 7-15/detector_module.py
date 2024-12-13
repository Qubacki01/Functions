###
#
#

def f(detector):
    people_in_room = 0
    for event in detector:
        if event == '+':
            people_in_room += 1
        elif event == '-':
            people_in_room -= 1
        if people_in_room >= 3:
            return True
    return False



def main():
    detector = input('Enter people: ')

    print(f(detector))

if __name__ == "__main__":
    main()