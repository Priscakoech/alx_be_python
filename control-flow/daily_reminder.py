task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level.")
# Print the customized reminder
print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
print(f"Reminder: '{task}' is a high priority task. Consider completing it soon.")
print(f"Reminder: '{task}' is a medium priority task. Consider completing it when possible.")
print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
