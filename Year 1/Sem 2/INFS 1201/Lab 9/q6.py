##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 6

def grade_2_gp(grade):
    'Converts an integer grade into the grade point acc to UDST standards'
    if grade<60:
        return 0
    for i in range(90,59,-5):
        if grade >= i:
            return (0.1*i)-5

def compute_semester_GPA(grades):
    'Computes the semester GPA using a given list of grades and credits for respective courses'
    total_grades = 0
    total_credits = 0
    for k, v in grades.items():
        total_grades += grade_2_gp(v)*k[1]
        total_credits += k[1]
    semester_GPA = total_grades/total_credits
    print(f"Your semester GPA is {semester_GPA}")

grades={('COMM1020',3):92, ('INFS1201',4):78,
        ('INFT1201',4):96, ('MATH1030',3):86}
compute_semester_GPA(grades)