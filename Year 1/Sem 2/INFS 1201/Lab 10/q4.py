##
# Gowshikrajan Senthilkumar - 60307390
# Week13 Lab10
# Exercise 4

def letter_to_grade(letter):
    grade_conv = {'A': 4,
                  'B+': 3.5, 'B': 3,
                  'C+': 2.5, 'C': 2,
                  'D+': 1.5, 'D': 1,
                  'F': 0}
    return grade_conv[letter]

def parse_line(line):
    data = line.split(',')
    if len(data)==3:
        return data[0], int(data[1]), data[2].strip()
    return None

def computeGPA(fileName):
    with open(fileName, 'r') as grade_csv:
        grades = {}
        total_credit = 0
        for line in grade_csv.readlines():
            data = parse_line(line)
            if data is not None and data[2] != 'W':
                course, credit, grade = data
                grade_i = credit*letter_to_grade(grade)
                if course not in grades:
                    grades[course] = grade_i
                    total_credit += credit
                elif grades[course] < grade_i:
                    grades[course] = grade_i
    gpa = sum(grades.values())/total_credit
    return gpa
