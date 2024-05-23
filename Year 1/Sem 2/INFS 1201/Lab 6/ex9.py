##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 9
import random
import ex7

UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER = 'abcdefghijklmnopqrstuvwxyz'
DIGITS = '1234567890'
SPECIAL = '~!@#$%^&*()_+'
COMBINED = UPPER + LOWER + DIGITS + SPECIAL

def generatePassword(length=12):
    try:
        if length < 8: 
            print("Invalid length paramter!\nLength has been defaulted to 12")
            length = 12
    except TypeError or ValueError: 
        print("Invalid length paramter!\nLength has been defaulted to 12")
        length = 12

    i = 0
    pw = ""
    count = [0]*4
    while i < length:
        if count[0] == 0:
            pw += UPPER[random.randrange(0,len(UPPER))]
            count[0] += 1
        elif count[1] == 0:
            pw += LOWER[random.randrange(0,len(LOWER))]
            count[1] += 1
        elif count[2] == 0:
            pw += DIGITS[random.randrange(0,len(DIGITS))]
            count[2] += 1
        elif count[3] == 0:
            pw += SPECIAL[random.randrange(0,len(SPECIAL))]
            count[3] += 1
        else:
            pw += COMBINED[random.randrange(0,len(COMBINED))]
        i += 1
    return ex7.shuffleString(pw)


assert len(generatePassword(7)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
for character in pw:
    if character in LOWER:
        hasLowercase = True
    if character in UPPER:
        hasUppercase = True
    if character in DIGITS:
        hasNumber = True
    if character in SPECIAL:
        hasSpecial = True
assert hasLowercase and hasUppercase and hasNumber and hasSpecial

print("All good")