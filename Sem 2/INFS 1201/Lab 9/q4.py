##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 4

def grade_2_gp(grade):
    'Converts an integer grade into the grade point acc to UDST standards'
    if grade<60:
        return 0
    for i in range(90,59,-5):
        if grade >= i:
            return (0.1*i)-5

def calculate_weighted_average_with_GP():
    'Calculate and print the average of a list of grades.'
    num_courses = int(input("Enter the number of courses that you are taking this semester: "))

    total_grade = 0
    total_credit = 0
    for i in range(num_courses):
        course_code = input(f"Enter the course code for course #{i+1}: ")
        credit = int(input(f"Enter the number of credits of {course_code}: "))
        grade_i = int(input(f"Enter the grade obtained in {course_code}: "))
        total_grade += grade_2_gp(grade_i)*credit
        total_credit += credit

    if total_credit == 0 and num_courses != 0:
        print("Cannot compute average with zero total credits.")
    else:
        semester_GP = total_grade/total_credit
        print(f"Your semester GPA is: {semester_GP:.2f}")





'''
print(grade_2_gp(95))
calculate_weighted_average_with_GP()
'''