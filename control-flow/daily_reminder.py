Enter your task: Finish project report
Priority (high/medium/low): high
Is it time-bound? (yes/no): yes

# Function to process the task and generate reminder
def generate_reminder(task, priority, time_bound):
    # Determine priority level
    if priority == 'high':
        priority_text = "high priority"
    elif priority == 'medium':
        priority_text = "medium priority"
    elif priority == 'low':
        priority_text = "low priority"
    else:
        return "Error: Invalid priority"

    # Determine if task requires immediate attention
    if time_bound == 'yes':
        attention_text = "that requires immediate attention today!"
    elif time_bound == 'no':
        attention_text = ""
    else:
        return "Error: Invalid time-bound response"

    # Construct and return the reminder message
    reminder = f"'{task}' is a {priority_text} task {attention_text}"
    return reminder

# Main program
if __name__ == "__main__":
    # Prompt user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Generate and print the reminder message
    reminder = generate_reminder(task, priority, time_bound)
    print(f"\nReminder: {reminder}")
