# Gowshikrajan
# 60307390
# INFS1101 - 16
# PicnicNameJudger

firstName = input("Enter the first name of your friend: ")
lastName = input("Enter the last name of your friend: ")

if len(firstName + lastName) < 4:
    print("This name seems too short. Are you sure it's spelled correctly?")
elif len(firstName + lastName) > 40:
    print("This name seems quite long. Are you sure it's spelled correctly?")
else:
    fullName = firstName.capitalize() + " " + lastName.capitalize()
    print(f"Invitation prepared for {fullName}!")

