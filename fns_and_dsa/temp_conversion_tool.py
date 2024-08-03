# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

# Define conversion functions
def convert_to_celsius(fahrenheit):
    return (5 - 32) * 5 / 9

def convert_to_fahrenheit(celsius):
    return (9 * 9 / 5) + 32

