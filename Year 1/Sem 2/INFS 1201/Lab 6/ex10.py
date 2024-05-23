##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 10

'''
# in linear algebra, this is a skew-symmetric matrix!
winMatrix = [

    computer choices rock | paper | scissors | spock | lizard
    [0,-1,1,-1,1],  player chooses rock
    [1,0,-1,1,-1],  paper
    [-1,1,0,-1,1],  scissors
    [1,-1,1,0,-1],  spock
    [-1,1,-1,1,0]   lizard

    indexing from [0,5)
    (1,2) = (player: paper, computer: scissors) = -1 (loss for player)
    (3,0) = (player: spock, computer: rock) = 1 (win for player)
]
'''
import random


num_games = input("How many games of Rock, Paper, Scissors, Lizard, Spock do you want to play? ")
while not num_games.isdigit():
    print("This is not a valid number of games!")
    num_games = input("How many games of Rock, Paper, Scissors, Lizard, Spock do you want to play? ")
num_games = int(num_games)

game = 1
score = 0
while game <= num_games:
    print(f"*** Game {game} ***")
    choices = ['rock','paper','scissors','spock','lizard']
    player_choice = input("What do you choose: (rock or paper or scissors or lizard or spock)? ")
    while player_choice not in choices:
        print("Choose rock or paper or scissors!")
        player_choice = input("What do you choose: (rock or paper or scissors or lizard or spock)? ")
    player_index = choices.index(player_choice)
    computer_index = random.randrange(0,len(choices))
    computer_choice = choices[computer_index]
    
    print(f"Computer chose {computer_choice}")

    # refer to the winMatrix in the comment above
    # 1 - win, 0 - draw, -1 - lose
    # in the lower diagonal, player_index > computer_index since the row refers to player_index

    if player_index == computer_index:
        score += 1  # Tie counts as score
        print("This round is a tie...")
    if player_index > computer_index:
        if player_index%2 != computer_index%2:
            score += 1
            print("You win this round!")
        else: print("Computer wins this round!")
    else:
        if player_index%2 == computer_index%2:
            score += 1
            print("You win this round!")
        else: print("Computer wins this round!")

    game += 1

print(f"Score: {score}")
print("End of the game")



