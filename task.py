def celsius_to_fahrenheit():
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is {fahrenheit}°F.")

def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is {celsius}°C.")

# Call the functions to convert temperatures
celsius_to_fahrenheit()
fahrenheit_to_celsius()
