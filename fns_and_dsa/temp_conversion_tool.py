def convert_temperature(temperature, unit):
  """Converts temperature between Celsius and Fahrenheit.

  Args:
    temperature: The temperature value to convert.
    unit: The unit of the input temperature ('C' for Celsius, 'F' for Fahrenheit).

  Returns:
    The converted temperature.
  """

  if unit == 'C':
    converted_temperature = (temperature * 9/5) + 32
    return f"{temperature:.1f}°C is {converted_temperature:.1f}°F"
  elif unit == 'F':
    converted_temperature = (temperature - 32) * 5/9
    return f"{temperature:.1f}°F is {converted_temperature:.1f}°C"
  else:
    return "Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit."

if __name__ == "__main__":
  temperature = float(input("Enter the temperature to convert: "))
  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
  result = convert_temperature(temperature, unit)
  print(result)
