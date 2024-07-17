def process_task(task, priority, time_bound):
    # React differently based on priority using match case
    match priority:
        case 'high':
            reminder = f"'{task}' is a high priority task"
        case 'medium':
            reminder = f"'{task}' is a medium priority task"
        case 'low':
            reminder = f"'{task}' is a low priority task"
        case _:
            return "Error: Invalid priority"

    # Modify reminder if the task is time-bound
    if time_bound.lower() == 'yes':
        reminder += " that requires immediate attention today!"

    return reminder

# Main program
if __name__ == "__main__":
    # Input task details from the user
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()  # Convert to lowercase for case insensitivity
    time_bound = input("Is it time-bound? (yes/no): ").lower()  # Convert to lowercase for case insensitivity

    # Process the task and get the reminder
    reminder = process_task(task, priority, time_bound)

    # Display the reminder
    print(f"\nReminder: {reminder}")


