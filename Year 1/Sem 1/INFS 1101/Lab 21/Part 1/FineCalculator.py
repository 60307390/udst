def calculate_fine(days_late):
    fine = 0
    if days_late <= 5:
        fine = days_late * 2
    else:
        fine = 5 * 2 + (days_late - 5) * 5
    return fine

# Main Program
days_late = int(input("Enter the number of days late: "))

# Calculate Fine
total_fine = calculate_fine(days_late)

# Output
print(f"Total Fine: ${total_fine}")
