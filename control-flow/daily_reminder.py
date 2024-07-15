def main():
    # Ask user to input task description
    task = input("Enter your task: ")
    
    # Ask user to input task priority
    priority = input("Priority (high/medium/low): ").lower()
    
    # Ask user if task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    
    # Prepare the reminder based on inputs
    if priority == 'high' and time_bound == 'yes':
        reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
    else:
        reminder = f"Reminder: '{task}' is a {priority} priority task."
        
    # Print the reminder
    print(reminder)

if __name__ == "__main__":
    main()

