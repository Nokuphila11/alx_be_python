import datetime

def display_current_datetime():
  """Displays the current date and time in the format YYYY-MM-DD HH:MM:SS."""
  current_date_time = datetime.datetime.now()
  formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
  print("Current date and time:", formatted_date_time)

def calculate_future_date():
  """Calculates the future date based on the user's input."""
  days_to_add = int(input("Enter the number of days to add: "))
  current_date = datetime.datetime.now()
  future_date = current_date + datetime.timedelta(days=days_to_add)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print("Future date:", formatted_future_date)

if __name__ == "__main__":
  display_current_datetime()
  calculate_future_date()
