##
# Gowshikrajan Senthilkumar - 60307390
# Week8 lab
# Exercise 9

import random

def longestStreak(lst,N):
    'returns the longest streak of an integer N in the given list.'
    max_count, count = 0, 0
    for i in lst:
        if i == N:
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

longest_streaks = []
for i in range(1,7):
    longest_streak_i = longestStreak(P_space, i)
    print(f"Longest streak of {i}: {longest_streak_i}")
    longest_streaks.append(longest_streak_i)

print("Output of dice rolls:", P_space)
print(f"The longest streak is for {longest_streaks.index(max(longest_streaks))+1}")
