##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 3

def calculate_weighted_average():
    'Calculate and print the average of a list of grades.'
    num_courses = int(input("Enter the number of courses that you are taking this semester: "))

    total_grade = 0
    total_credit = 0
    for i in range(num_courses):
        course_code = input(f"Enter the course code for course #{i+1}: ")
        credit = int(input(f"Enter the number of credits of {course_code}: "))
        grade_i = int(input(f"Enter the grade obtained in {course_code}: "))
        total_grade += grade_i*credit
        total_credit += credit

    if total_credit == 0 and num_courses != 0:
        print("Cannot compute average with zero total credits.")
    else:
        avg_grade = total_grade/total_credit
        print(f"Your average for this semester is: {avg_grade:.2f}")


#calculate_weighted_average()