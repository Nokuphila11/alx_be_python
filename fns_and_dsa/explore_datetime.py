# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days):
    """Calculate a future date given a number of days to add to the current date."""
    try:
        days = int(days)  # Ensure that the input is an integer
    except ValueError:
        print("Invalid input. Please enter an integer value for the number of days.")
        return

    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    display_current_datetime()
    
    days = input("Enter the number of days to add to the current date: ")
    calculate_future_date(days)

if __name__ == "__main__":
    main()

