##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 9

from ex7 import isLeapYear

def isValidDate(year, month, day):
    '''
    Takes year,month, and day as parameters
    Returns if it is a valid date.
    '''
    try:
        yearValid = 0 < year
        monthValid = 0 < month <= 12
        maxDay = 0
    except:
        return False

    if not (yearValid and monthValid):
        return False
    
    if month <= 6:
        if month%2 == 0:
            maxDay = 30
        else:
            maxDay = 31
    else:
        if month%2 == 0:
            maxDay = 31
        else:
            maxDay = 30
    
    #Checking for febuary
    if month == 2:
        if isLeapYear(year): maxDay = 29
        else: maxDay = 28
    
    dayValid = 0 < day <= maxDay
    #Here, month and year is valid
    return dayValid

assert isValidDate(1999, 12, 31) == True
assert isValidDate(2000, 2, 29) == True
assert isValidDate(2001, 2, 29) == False
assert isValidDate(2029, 13, 1) == False
assert isValidDate(1000000, 1, 1) == True
assert isValidDate(2015, 4, 31) == False
assert isValidDate(1970, 5, 99) == False
assert isValidDate(1981, 0, 3) == False
assert isValidDate(1666, 4, 0) == False
assert isValidDate(1999, "twelve", 31) == False

print("Function has passed all tests for ex9 module")