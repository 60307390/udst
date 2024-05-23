# Gowshikrajan
# 60307390
# INFS 1101 - 16
# NumberGuesser

name = input("What is your name? ").capitalize()

GUESS_N = 33
print(f"Hello, {name}! I've chosen a number from 1 to 100. Try to guess it!")

tries = 1
guess = int(input("Enter your guess: "))

while guess != GUESS_N:
    if not (0 <= guess <= 100):
        print("Please enter an umber between 1 and 100")
    if guess < GUESS_N:
        print("Too low!")
    elif guess > GUESS_N:
        print("Too high!")
    guess = int(input("Enter your guess: "))
    tries += 1

print("Correct!")
print(f"{name}, it took you {tries} tries to guess the right number.")

if 1 <= tries <= 3:
    print(f"Amazing guessing skills, {name}! Would you like to try again?")
elif 4 <= tries <= 6:
    print(f"Nice persistence, {name}! You've got it after a few tries. Would you like to play again?")
else:
    print(f"You can do better, {name}! Try playing again.")

