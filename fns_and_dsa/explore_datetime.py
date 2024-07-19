import datetime

def calculate_future_date(days_to_add):
  """Calculates the future date by adding the specified number of days to the current date.

  Args:
    days_to_add: The number of days to add.

  Returns:
    A string representing the future date in the format YYYY-MM-DD.
  """

  current_date = datetime.datetime.now()
  future_date = current_date + datetime.timedelta(days=days_to_add)
  formatted_date = future_date.strftime("2024-04-04")
  return formatted_date

if __name__ == "__main__":
  print("Current date and time:", datetime.datetime.now())
  days_to_add = int(input("Enter the number of days to add to the current date: "))
  future_date = calculate_future_date(days_to_add)
  print("Future date:", future_date)

