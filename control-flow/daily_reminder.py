def process_task():
  """Prompts the user for task details and provides a reminder."""

  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ")
  time_bound = input("Is it time-bound? (yes/no): ")

  reminder_base = "high priority" if priority == "high" else "medium priority" if priority == "medium" else "low priority"

  if time_bound.lower() == "yes":
    reminder = f"'{task}' is a {reminder_base} task that requires immediate attention today!"
  else:
    reminder = f"'{task}' is a {reminder_base} task."

  print(reminder)

if __name__ == "__main__":
  process_task()


