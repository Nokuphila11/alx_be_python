# Main program
if __name__ == "__main__":
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate and print the reminder message
    reminder = generate_reminder(task, priority, time_bound)
    print(f"\nReminder: {reminder}")
