task = input("enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_inbound = input("Is it time-inbound? (yes/no): ").lower()
match priority:
    case "high":
        reminder = f"Your task '{task}' is of high priority."
    case "medium":
        reminder = f"Your task '{task}' is of medium priority."
    case "low":
        reminder = f"Your task '{task}' is of low priority."
    case "_":
        reminder = f"Your task '{task}' is of unkwown priority."
if time_inbound == "yes":
    reminder += " This task requires immediate attention today!"
print(reminder)