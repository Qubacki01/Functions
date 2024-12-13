###
# Functions to read any data type from the keyboard
#
def input_string(message):
    return input(message)

def input_integer(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("! INVALID INPUT !")

def input_real(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("! INVALID INPUT !")

def input_boolean(message):
    while True:
        user_input = input(message).strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('! INVALID INPUT !')