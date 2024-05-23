##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 3

def wordParity(text):
    'returns True if the length of text is even, False otherwise'
    return len(text)%2 == 0

num_words = int(input("Enter the number of words to be checked: "))

num_even = 0
for i in range(num_words):
    word = input(f"Enter word {i+1}: ")
    if wordParity(word):
        num_even += 1

print(f"You entered {num_even} words of even length")
