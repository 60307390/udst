##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 6

def grade_2_gp(grade):
    'Converts an integer grade into the grade point acc to UDST standards'
    if grade<60:
        return 0
    for i in range(90,59,-5):
        if grade >= i:
            return (0.1*i)-5

def calculate_weighted_average_with_GP():
    'Calculate and print the average of a list of grades.'
    # Initial Validations
    while True:
        try:
            initial_grade = float(input("Enter your current earned credit points: "))
            assert initial_grade >= 0
            break
        except:
            print("Earned credit points should be a positive number.")
            
    while True:
        try:
            initial_credit = input("Enter your current earned credits: ")
            assert int(initial_credit) >= 0 and '.' not in initial_credit
            initial_credit = int(initial_credit)
            break
        except:
            print("Earned credits should be a positive integer.")

    while True:
        try:
            num_courses = input("Enter the number of courses that you are taking this semester: ")
            assert int(num_courses) >= 0 and '.' not in num_courses
            num_courses = int(num_courses)
            break
        except:
            print("Number of courses should be a positive integer.")


    total_grade = 0
    total_credit = 0
    for i in range(num_courses):

        # Validations
        while True:
            try:
                course_code = input(f"Enter the course code for course #{i+1}: ")
                assert len(course_code) == 8 and course_code[:4].isalpha() and course_code[4:].isdigit()
                break
            except:
                print("Course code should include four letters followed by four digits.")

        while True:
            try:
                credit = input(f"Enter the number of credits of {course_code}: ")
                assert int(credit) >= 0 and '.' not in credit
                credit = int(credit)
                break
            except:
                print("Credit of a course should be a positive integer.")

        while True:
            try:
                grade_i = float(input(f"Enter the grade obtained in {course_code}: "))
                assert 100 >= grade_i >= 0
                break
            except:
                print("grade should be less than or equal to 100!")

        # Calculations
        total_grade += grade_2_gp(grade_i)*credit
        total_credit += credit

    if total_credit == 0 and num_courses != 0:
        print("Cannot compute average with zero total credits.")
    else:
        semester_GP = total_grade/total_credit
        print(f"Your semester GPA is: {semester_GP}")
    cumulative_GP = (total_grade+initial_grade)/(total_credit+initial_credit)
    print(f"Your cumulative GPA is: {cumulative_GP}")



#calculate_weighted_average_with_GP()