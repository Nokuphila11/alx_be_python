def celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
  """Converts Fahrenheit to Celsius."""
  return (fahrenheit - 32) * 5/9

def main():
  while True:
    try:
      temperature = float(input("Enter temperature: "))
      unit = input("Enter unit (C for Celsius, F for Fahrenheit): ").upper()

      if unit == "C":
        fahrenheit = celsius_to_fahrenheit(temperature)
        print(f"{temperature} degrees Celsius is {fahrenheit:.2f} degrees Fahrenheit.")
      elif unit == "F":
        celsius = fahrenheit_to_celsius(temperature)
        print(f"{temperature} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
      else:
        print("Invalid unit. Please enter C or F.")
    except ValueError:
      print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
  main()




