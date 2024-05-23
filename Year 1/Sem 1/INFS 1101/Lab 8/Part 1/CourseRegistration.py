# Gowshikrajan
# 60307390
# INFS 1101 - 16
# CourseRegistration

stdID = int(input("Please enter your student ID: "))

if stdID < 60000000 or stdID > 69999999: # or not(60000000 < stdID < 69999999)
    print(f'{stdID} is not a valid entry for student ID. It must be between 60000000 – 69999999.')
else:
    code = input("Please enter your course code: ")
    if len(code) != 8:
        print(f"{code} is not a valid entry for course code. It must be 8 characters long.")
    else:
        print(f"Thank you for your entry, {stdID}. You are now registered in {code}.")
