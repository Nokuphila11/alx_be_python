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
      # Get valid temperature input
      temperature = float(input("Enter the temperature to convert: "))

      # Ensure valid unit input (C or F)
      valid_units = ("C", "F")
      while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit in valid_units:
          break
        else:
          print("Invalid unit. Please enter C or F.")

      # Call appropriate conversion function based on unit
      if unit == "C":
        converted_temp = convert_to_fahrenheit(temperature)
        unit_label = "Celsius"
      else:
        converted_temp = convert_to_celsius(temperature)
        unit_label = "Fahrenheit"

      # Display formatted output
      print(f"{temperature:.2f}°{unit_label} is {converted_temp:.2f}°F" if unit == "C" else f"{temperature:.2f}°{unit_label} is {converted_temp:.2f}°C")

    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()


