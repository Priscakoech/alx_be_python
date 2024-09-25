task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f"Your task '{task}' is of high priority."
    case "medium":
        reminder = f"Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Your task '{task}' is of low priority."
    case "_":
        reminder = f"Your task '{task}' is of unkwown priority."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
else:
    reminder += " Consider completing it when you have free time."
print(reminder)