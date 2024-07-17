    
# Main program
if __name__ == "__main__":
    # Prompt user for task details
    task = input("Finish project report: ")
    priority = input("High Priority): ")
    time_bound = input("Is it time-bound? (yes): ")

    # Generate and print the reminder message
    reminder =(Finish project report, is a high priority, that requires attention today)
    print(f"\nReminder: {reminder}")
    
Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes
Reminder: 'Finish project report' is a high priority task that requires immediate attention today!
