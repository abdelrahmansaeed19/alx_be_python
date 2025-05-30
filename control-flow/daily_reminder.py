task_error = True

pirority_error = True

time_bound_error = True

while task_error:
    try:
        task = input("Enter your task: ")
        if not isinstance(task, str) and task.strip():
            raise ValueError("Task Must be Text.")
        elif len(task) > 100 or len(task) < 4:
            raise ValueError("Task must be less than 100 characters and greater than 3.")
        task_error = False
    except ValueError as e:
        print(e)

while pirority_error:
    try:
        priority = input("Priority (high/medium/low): ").lower()
        if priority not in ['high', 'medium', 'low']:
            raise ValueError("Priority must be high, medium, or low.")
        pirority_error = False
    except ValueError as e:
        print(e)

reminder_message = ""

# high['\"]\s*;

while time_bound_error:
    try:
        time_bound = input("Is it time-bound? (yes/no): ")
        if time_bound not in ['yes', 'no']:
            raise ValueError("Time-bound must be yes or no.")
        time_bound_error = False
    except ValueError as e:
        print(e)

priority_message = ""

match priority:
    case "high":
        priority_message = "a high priority task"
    case "medium":
        priority_message = "a medium priority task"
    case "low":
        priority_message = "a low priority task"
    case _:
        priority_message = "an Unknown priority task"

time_bound_message = ""

if time_bound == "yes":
    time_bound_message = " that requires immediate attention today!"
    print(f"Reminder: '{task}' is {priority_message}{time_bound_message}")
else:
    time_bound_message = ". Consider completing it when you have free time."
    print(f"Note: '{task}' is {priority_message}{time_bound_message}")

#print(f"Reminder:
