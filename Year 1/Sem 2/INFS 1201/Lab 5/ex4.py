##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 4

def stringStats(num):
    lex_max = '0'
    max_length = 0
    for i in range(num):
        x = input(f"Enter word {i+1}: ")
        if i == 0 or min_length > len(x):
            min_length = len(x)
        if max_length < len(x):
            max_length = len(x)

        if i == 0 or lex_min > x:
            lex_min = x
        if lex_max < x:
            lex_max = x

    return max_length, min_length, lex_max, lex_min
        

while True:
    try:
        num_words = int(input("Enter the number of words: "))
        while num_words < 0:
            print("Please enter a valid positive integer.")
            num_words = int(input("Enter the number of words: "))
        break
    except ValueError:
        print("Please enter a valid integer.")
max_len, min_len, lex_max, lex_min = stringStats(num_words)

print(f"The length of the longest word entered was: {max_len} letters")
print(f"The length of the shortest word entered was: {min_len} letters")
print(f"According to lexicographic order, the first word entered was: {lex_min}")
print(f"According to lexicogrpahic order, the last word entered was: {lex_max}")
