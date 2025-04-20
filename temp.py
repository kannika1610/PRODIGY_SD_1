def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def temperature_converter():
    print("Welcome to the Temperature Converter!")
    temp = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C, F, or K): ").upper()

    if unit == 'C':
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
        print(f"\n{temp}°C is equal to:")
        print(f"{f:.2f}°F")
        print(f"{k:.2f}K")

    elif unit == 'F':
        c = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(temp)
        print(f"\n{temp}°F is equal to:")
        print(f"{c:.2f}°C")
        print(f"{k:.2f}K")

    elif unit == 'K':
        c = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(temp)
        print(f"\n{temp}K is equal to:")
        print(f"{c:.2f}°C")
        print(f"{f:.2f}°F")

    else:
        print("Invalid unit entered. Please use 'C', 'F', or 'K'.")

# Run the program
temperature_converter()