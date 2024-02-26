##
# Gowshikrajan Senthilkumar - 60307390
# Week9 lab
# Exercise 1
import random

def randomNumbers(upTo, num):
    '''Function to generate `num` random integers each between 1 and `upTo` and return the count of unique numbers.'''
    nums = set()
    for i in range(num):
        nums.add(random.randint(1,upTo))
    return len(nums)

'''
for i in range(10,200,25):
    randomNum = randomNumbers(365,i)
    collisions = i-randomNum
    print(f"While drawing {i} random numbers between 1 and 365, we obtained {randomNum} different numbers, and {collisions} collisions.")
'''

