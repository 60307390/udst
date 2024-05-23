def calculate_calories(activity, duration):
    # Calorie burn rates per minute for different activities
    if activity == "running":
        return duration * 10  # 10 calories per minute
    elif activity == "cycling":
        return duration * 8   # 8 calories per minute
    elif activity == "swimming":
        return duration * 7   # 7 calories per minute
    else:
        return duration * 5   # default: 5 calories per minute for other activities

# Main Program
total_calories_burned = 0
continue_logging = True

while continue_logging:
    activity = input("Enter the activity (running, cycling, swimming, other): ").lower()
    duration = int(input("Enter the duration in minutes: "))

    calories_burned = calculate_calories(activity, duration)
    total_calories_burned += calories_burned

    print(f"Calories burned in this session: {calories_burned}")

    continue_choice = input("Do you want to log another activity? (yes/no): ").lower()
    if continue_choice == 'no':
        continue_logging = False

# Output
print(f"Total calories burned: {total_calories_burned}")
