height = float(input('enter your hight: '))
weight = float(input('Enter your weight: '))

print(height, weight)

def update_bmi(height, weight):
    #BMI Calculation
    bmi = weight / (height ** 2)

    print(height, weight)
    changes = 0
    while bmi >= 25:
        weight -= 1
        bmi = weight / (height ** 2)
        changes += 1
    return bmi, changes

#Main program
if height < 1.5:
    height += 0.05
else:
    height -= 0.02

final_bmi, total_changes = update_bmi(height, weight)

print("Final BMI:", round(final_bmi, 2))
print("Total Changes:", total_changes)
