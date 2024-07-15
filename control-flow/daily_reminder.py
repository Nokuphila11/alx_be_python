def main():
    # Ask user to input task description
    task = input("Enter the task description: ")
    
    # Ask user to input task priority
    priority = input("Enter the task's priority (high, medium, low): ").lower()
    
    # Ask user if task is time-bound
    time_bound = input("Is the task time-bound? (yes or no): ").lower()
    
    # Process the task based on priority and time sensitivity
    if priority == 'high':
        reminder = f"Task '{task}' is high priority"
    elif priority == 'medium':
        reminder = f"Task '{task}' is medium priority"
    elif priority == 'low':
        reminder = f"Task '{task}' is low priority"
    else:
        print("Invalid priority level")
        return
    
    if time_bound == 'yes':
        reminder += ", that requires immediate attention today!"
    elif time_bound == 'no':
        reminder += ", no immediate action needed."
    else:
        print("Invalid time-bound response")
        return
    
    # Print the customized reminder
    print(reminder)
