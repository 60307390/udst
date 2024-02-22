##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 7

def isLeapYear(year):
    'returns true if paramter is a leap year, and false otherwise'
    return year%400 == 0 or (year%4 == 0 and year%100 != 0)

assert isLeapYear(1999) == False
assert isLeapYear(2000) == True
assert isLeapYear(2001) == False
assert isLeapYear(2004) == True
assert isLeapYear(2100) == False
assert isLeapYear(2400) == True
print("Function has passed all tests for ex7 module")
