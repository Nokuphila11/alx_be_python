# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
        # Prompt the user to enter a temperature and specify the unit
        temp = float(input("Enter the temperature: "))
        unit = input("Is the temperature in (C)elsius or (F)ahrenheit? ").strip().upper()
        
        if unit == 'C':
            # Convert Celsius to Fahrenheit
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please specify 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()


def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == "C":
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature:.2f}°C is {fahrenheit:.2f}°F")
      elif unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature:.2f}°F is {celsius:.2f}°C")
      else:
        print("Invalid unit. Please enter C or F.")
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()
