
def process_task():
  task = input("Enter your task: ")
  priority = input("Priority (high/medium/low): ")
  time_bound = input("Is it time-bound? (yes/no): ")

  match priority:
    case "high":
      reminder_base = "high priority"
    case "medium":
      reminder_base = "medium priority"
    case "low":
      reminder_base = "low priority"
    case _:
      print("Invalid priority")
      return

  if time_bound.lower() == "yes":
    reminder = f"{task} is a {reminder_base} task that requires immediate attention today!"
  else:
    reminder = f"{task} is a {reminder_base} task."

  print(reminder)

if __name__ == "__main__":
  process_task()

