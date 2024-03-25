##
# Gowshikrajan Senthilkumar - 60307390
# Week13 Lab10
# Exercise 2

def updateTranscript(fileName):
    sem = input("Which semester are you adding? ")
    num_courses = int(input(f"How many courses did you take in {sem}? "))

    csv_f = open(fileName, 'a')

    csv_f.write('*'*60+'\n')
    csv_f.write(f'\t{sem}\n')

    for i in range(num_courses):
        course = input(f"Course code #{i+1}: ")
        credit = input(f"Number of credits of {course}: ")
        grade = input(f"Grade in {course}: ")

        csv_f.write(f"{course},{credit}, {grade}\n")

    csv_f.write('\n')
    csv_f.close()
