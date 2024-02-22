##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 8

import random


num_games = input("How many games of Rock, Paper, Scissors do you want to play? ")
while not num_games.isdigit():
    print("This is not a valid number of games!")
    num_games = input("How many games of Rock, Paper, Scissors do you want to play? ")
num_games = int(num_games)

game = 1
score = 0
while game <= num_games:
    print(f"*** Game {game} ***")
    choices = ['rock','paper','scissors']
    player_choice = input("What do you choose: (rock or paper or scissors)? ")
    while player_choice not in choices:
        print("Choose rock or paper or scissors!")
        player_choice = input("What do you choose: (rock or paper or scissors)? ")
    random_index = random.randrange(0,len(choices))
    computer_choice = choices[random_index]
    
    print(f"Computer chose {computer_choice}")

    # rock is 2 away from scissors, paper is 2 away from rock (from the right), similar for scissors
    # the losing condition in this list is always 2 away from the given choice
    # checks if player choice is the losing condition for a given computer's choice
    if (player_choice == choices[random_index-2]):
        score += 1
        print("You win this round!")
    elif player_choice == computer_choice:
        score += 1  # Tie counts as score
        print("This round is a tie...")
    else:
        print("Computer wins this round!")
    game += 1

print(f"Score: {score}")
print("End of the game")
