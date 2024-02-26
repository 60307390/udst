##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 7


def grade_2_gp(grade):
    'Converts an integer grade into the grade point acc to UDST standards'
    if grade<60:
        return 0
    for i in range(90,59,-5):
        if grade >= i:
            return (0.1*i)-5

def calculate_weighted_average_with_GP():
    'Calculate and print the average of a list of grades.'
    # Initial Lists
    courses=["Past", "COMM1020", "INFS1201", "INFT1201", "MATH1030"]
    credits=[12, 3, 4, 4, 3]
    grades=[36.5, 92, 78, 96, 86]

    weighted_grades = []
    for i in range(len(grades)):
        if i != 0:
            weighted_grades.append(grade_2_gp(grades[i])*credits[i])
    
    # Calculations
    total_grade = sum(weighted_grades)
    total_credit = sum(credits)-credits[0]

    semester_GP = total_grade/total_credit
    print(f"Your semester GPA is: {semester_GP}")
    cumulative_GP = (total_grade+grades[0])/(total_credit+credits[0])
    print(f"Your cumulative GPA is: {cumulative_GP}")


calculate_weighted_average_with_GP()