from fractions import Fraction

def calc_new_height():
    width = eval(input("Enter the current width: "))
    height = eval(input("Enter the current height: "))
    new_width = eval(input("Enter the desired width: "))
    value = width/height
    ratio = Fraction(value).limit_denominator()
    numbers = [int(i) for i in str(ratio).split('/')]
    new_height = new_width/int(numbers[0]) * int(numbers[1])
    print("\nThe corresponding height is: ", new_height)
    return new_height

print(calc_new_height())
