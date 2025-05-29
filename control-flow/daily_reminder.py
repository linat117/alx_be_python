task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound> (yes/no): ")
match priority:
    case "high":
        if time_bound == "yes":
            Reminder = f"'{task}' is a high priority task that requires immediate attention today!"
            print(Reminder)
    case "low":
        if time_bound == "no":
            Note = f"'{task}' is a low priority task. Consider completing it when you have free time."
            print(Note)
    