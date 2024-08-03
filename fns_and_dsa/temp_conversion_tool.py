def convert_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
  return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
  while True:
    try:
      temperature = float(input("Enter the temperature to convert: "))
      unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

      if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is {converted_temp} degrees Fahrenheit")
      elif unit == "F":
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is {converted_temp} degrees Celsius")
      else:
        print("Invalid unit. Please enter C or F.")
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()
