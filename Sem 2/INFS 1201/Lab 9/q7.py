##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 7
import random

def roll_random_dice(rolls):
    'Generates N random dice rolls for given number of rolls N, outputs frequency of dice rolls'
    P_space = []
    P_frequency = {}
    for i in range(1,7):
        P_frequency[i] = 0

    for i in range(rolls):
        roll_i = random.randint(1,6)
        P_space.append(roll_i)
        P_frequency[roll_i] += 1

    print(f"Output of dice rolls: {P_space}")
    print(f"Frequency of dice rolls: {P_frequency}")

number_of_rolls = int(input("How many times do you want to roll the dice? "))
roll_random_dice(number_of_rolls)