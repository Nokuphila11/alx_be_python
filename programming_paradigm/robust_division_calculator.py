import sys
from robust_division_calculator import safe_divide

def main():
  """Handles command-line arguments and performs safe division."""
  if len(sys.argv) != 3:
    print("Usage: python main.py <numerator> <denominator>")
    sys.exit(1)

  try:
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    result = safe_divide(numerator, denominator)
    print(result)
  except:  # Catch any unexpected errors
    print("An unexpected error occurred. Please try again with valid numeric inputs.")

if __name__ == "__main__":
  main()
