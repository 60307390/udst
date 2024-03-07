##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 8

def makeChange(amount):
    'returns the smallest amount of denominations for a given amount, interpreted as notes'
    denominations = [500,200,100,50,10,5,1]
    notes = {}
    for i in denominations:
        if amount//i > 0:
            notes[i] = amount//i
        amount %= i
    return notes

amount_of_QAR = int(input("Enter an amount: "))
print(makeChange(amount_of_QAR))