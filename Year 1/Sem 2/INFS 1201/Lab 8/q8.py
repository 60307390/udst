##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 8


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
    data=["Past", 12, 36.5, "COMM1020", 3, 92, "INFS1201", 4, 78, "INFT1201", 4, 96, "MATH1030", 3, 86]

    weighted_grades = [data[2]]
    credits = [data[1]]
    for i in range(3,len(data)):
        if (i+1)%3 == 0:
            weighted_grades.append(grade_2_gp(data[i])*data[i-1])
            credits.append(data[i-1])
    print(weighted_grades, credits)
    
    # Calculations
    total_grade = sum(weighted_grades)-weighted_grades[0]
    total_credit = sum(credits)-credits[0]

    semester_GP = total_grade/total_credit
    print(f"Your semester GPA is: {semester_GP}")
    cumulative_GP = (total_grade+weighted_grades[0])/(total_credit+credits[0])
    print(f"Your cumulative GPA is: {cumulative_GP}")


#calculate_weighted_average_with_GP()