###
#
#

def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100
def cm_to_in(n):
    return n/2.54
def ftin_to_cm(ft, inch):          # 1ft = 30.48cm | 1in = 2.54 cm
    return (ft * 30.48) + (inch * 2.54)

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'200cm = {cm_to_in(200):.2f} inches')
    print(f'5ft 3in = {ftin_to_cm(5, 3)}cm')
