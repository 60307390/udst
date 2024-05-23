
height =float(input('Enter your hight:'))
weight =float(input('Enter your weight:'))

def update_bmi(height, weight):
    # BMI calculation
    bmi = weight / (height ** 2)
    
    
    changes = 0
    while bmi >= 25:  # Loop if BMI is in overweight range
        weight -= 1   # Losing weight
        bmi = weight / (height ** 2)  # Recalculate BMI
        changes += 1
    return bmi, changes

# Main program
if height < 1.5:
    height += 0.05  # Slight increase in height for shorter individuals
else:
    height -= 0.02  # Slight decrease in height for taller individuals

final_bmi, total_changes = update_bmi(height, weight)

print("Final BMI:", round(final_bmi, 2))
print("Total Changes:", total_changes)
