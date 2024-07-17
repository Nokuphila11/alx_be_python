# Example interaction and output as specified
task = "Finish project report"
priority = "high"
time_bound = "yes"

# Determine priority level text
if priority == "high":
    priority_text = "high priority"
elif priority == "medium":
    priority_text = "medium priority"
elif priority == "low":
    priority_text = "low priority"
else:
    priority_text = "unknown priority"

# Determine if task requires immediate attention text
if time_bound == "yes":
    attention_text = "that requires immediate attention today!"
else:
    attention_text = ""

# Construct reminder message
reminder = f"Reminder: '{task}' is a {priority_text} task {attention_text}"
print(reminder)
