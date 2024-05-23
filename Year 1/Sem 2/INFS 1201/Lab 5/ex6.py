##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 6

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'

def hasLower(word):
    'returns true if the word has lower case letters'
    for i in word:
        if i in LOWER:
            return True
    return False
    
def hasUpper(word):
    'returns true if the word has upper case letters'
    for i in word:
        if i in UPPER:
            return True
    return False
    
def hasDigit(word):
    'returns true if the word has digits'
    for i in word:
        if i in DIGITS:
            return True
    return False
    
def hasSpecial(word):
    'returns true if the word has special characters'
    for i in word:
        if i in SPECIAL:
            return True
    return False


assert hasLower("SuperP@55word")==True
assert hasUpper("SuperP@55word")==True
assert hasDigit("SuperP@55word")==True
assert hasSpecial("SuperP@55word")==True
assert hasLower("SUPERP@55WORD")==False
assert hasUpper("superp@55word")==False
assert hasDigit("SuperP@ssword")==False
assert hasSpecial("SuperPa55word")==False
print("Test completed")

    
