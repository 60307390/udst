##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 2

def calculate_average():
    'Calculate and print the average of a list of grades.'
    num_courses = int(input("Enter the number of courses that you are taking this semester: "))

    total_grade = 0
    for i in range(num_courses):
        course_code = input(f"Enter the course code for course #{i+1}: ")
        grade_i = int(input(f"Enter the grade obtained in {course_code}: "))
        total_grade += grade_i

    avg_grade = total_grade/num_courses
    print(f"Your average for this semester is: {avg_grade:.2f}")

