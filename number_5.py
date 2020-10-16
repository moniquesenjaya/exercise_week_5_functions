def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit: "))
    celcius = convert_to_celsius(fahrenheit)
    kelvin = convert_to_kelvin(celcius)
    print("\nThe temperature in Fahrenheit is: ", fahrenheit)
    print("The temperature in Celsius is: ", celcius)
    print("The temperature in Kelvin is: ", kelvin)

def convert_to_celsius(fahrenheit):
    celcius = 5 / 9 *(fahrenheit - 32)
    return celcius

def convert_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

convert_temp()
