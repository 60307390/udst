##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 1

maleCount = 0
femaleCount = 0

i = 1
while True:
    gender = input(f"Enter the gender of guest number {i}: ").lower()
    while gender != 'm' and gender != 'f' and gender != 'q':
        print("Invalid entry, please try again")
        gender = input(f"Enter the gender of guest number {i}: ").lower()
    if gender == 'm':
        maleCount += 1
    elif gender == 'f':
        femaleCount += 1
    else:
        break
    i += 1


if femaleCount == 0:
    print("There were no female guests today.")
elif femaleCount == 1:
    print("There was one female guest today.")
else:
    print(f"There were {femaleCount} female guests today.")

if maleCount == 0:
    print("There were no male guests today.")
elif maleCount == 1:
    print("There was one male guest today.")
else:
    print(f"There were {maleCount} male guests today.")

print("Thank you!")
