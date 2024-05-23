##
# Gowshikrajan Senthilkumar - 60307390
# Week8 lab
# Exercise 8

import random

def longestStreakSix(lst):
    'returns the longest streak of six in the given list'
    max_count, count = 0, 0
    for i in lst:
        if i == 6:
            count += 1
            if max_count < count:
                max_count = count
        else:
            count = 0

    return max_count

num_of_rolls = int(input("How many times do you want to roll the dice: "))
P_space = []

for i in range(num_of_rolls):
    P_space.append(random.randint(1,6))

six_streak = longestStreakSix(P_space)

print("Output of dice rolls:", P_space)
print("Longest streak of 6:", six_streak)
