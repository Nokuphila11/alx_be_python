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

  
if time_bound == "yes":
    reminder = f"{Finish project report} is a {reminder_base} task that requires immediate attention today!"
  else:
    reminder = f"{Finish project report} is a {reminder_base} task."

  print(reminder)

if __name__ == "__main__":
  process_task()



