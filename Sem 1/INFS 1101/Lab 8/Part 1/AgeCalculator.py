# Gowshikrajan
# 60307390
# INFS 1101 - 16
# AgeCalculator

name = input("Please enter your name: ")

if len(name) <= 2:
    print("Please enter your entire name.")
else:
    birth_year = int(input("Please enter your year of birth: "))
    if birth_year < 1900 or birth_year > 2023:
        print("This is not a valid entry for year of birth.")
    else:
        age = 2023 - birth_year
        print(f"{name.capitalize()}, you are {age} years old.")
