# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZING_POINT = 32
CELSIUS_FREEZING_POINT = 0

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using global conversion factors."""
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_FREEZING_POINT
    return (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using global conversion factors."""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FAHRENHEIT_FREEZING_POINT
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_FREEZING_POINT

def main():
    try:
        # Prompt user for temperature and unit
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.10f}°C")
        
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


