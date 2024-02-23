##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 10
import random

def guessNumber(minRange, maxRange, difficulty):
    SCORE_FACTOR = 2.718281828459*10**(1.618033988749)
    secret_guess = random.randint(minRange, maxRange)
    user_guess = int(input("Guess the secret number!: "))

    attempts = 1
    while user_guess != secret_guess:
        # for an arbitary number N, let difficulty be d. given 0 <= N <= 100
        # probability of N <= d is P(N<=d) = d/100, where the program offers no hints
        # probability of N > d is P(N>d) = (100-d)/100, where the program offers hints
        if difficulty > random.randint(0, 99):
            print("Incorrect guess!")
        else:
            if user_guess > secret_guess:
                print("Your guess was too high!")
            else:
                print("Your guess was too low!")

        attempts += 1
        user_guess = int(input("Guess the secret number!: "))

    # According to the question, for a proportionality factor k, the score s is
    # s = k * (d*|range|)/(attempts)
        
    score = SCORE_FACTOR * difficulty * (maxRange-minRange) / attempts
    
    print(f"You found the secret number: {secret_guess}")
    print(f"Number of attempts are: {attempts}")
    print(f"Your score: {int(score)}")

print("***Guess a number game***")
smallest_num = int(input("Enter the smallest number that the computer can select: "))
largest_num = int(input("Enter the largest number that the computer can enter: "))
difficulty = int(input("Enter the game difficulty (0-100): "))

guessNumber(smallest_num, largest_num, difficulty)
