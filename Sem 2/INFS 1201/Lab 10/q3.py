##
# Gowshikrajan Senthilkumar - 60307390
# Week13 Lab10
# Exercise 3

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
        weighted_grades = 0
        total_credit = 0
        for line in grade_csv.readlines():
            data = parse_line(line)
            if data is not None:
                course, credit, grade = data
                weighted_grades += credit*letter_to_grade(grade)
                total_credit += credit
    gpa = weighted_grades/total_credit
    return gpa
