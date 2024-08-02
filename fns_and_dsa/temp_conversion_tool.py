
# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR

def main():
  while True:
    try:
      temperature = float(input("Enter temperature: "))
      unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

      if unit == "C":
        fahrenheit = convert_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")
      elif unit == "F":
        celsius = convert_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
      else:
        print("Invalid unit. Please enter C or F.")
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()


