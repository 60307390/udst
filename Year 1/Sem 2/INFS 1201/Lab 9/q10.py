##
# Gowshikrajan Senthilkumar - 60307390
# Week11 lab
# Exercise 10

from q3 import randomLetter

def randomLetterFreq(N):
    'generates N random letters for a given N and outputs the frequency and mode of the result of N trials'
    freq_letters = {}
    max_freq = 0

    # To put random letter frequencies in unsorted dictionary
    for i in range(N):
        random_letter = randomLetter()
        if random_letter not in freq_letters:
            freq_letters[random_letter] = 0
        freq_letters[random_letter] += 1

        if max_freq < freq_letters[random_letter]:
            max_freq = freq_letters[random_letter]

    sorted_letters = sorted(list(freq_letters))
    sorted_freq_letters = {}
    max_freq_letters = ""

    # Handles making the sorted dictionary AND to make the list of the mode(s)
    for i in sorted_letters:
        sorted_freq_letters[i] = freq_letters[i]
        if sorted_freq_letters[i] == max_freq:
            max_freq_letters += i + ' '
    
    print(f"Frequency of letters: {sorted_freq_letters}")
    print(f"Most frequent letter(s): {max_freq_letters}")


num_of_letters = int(input("How many letters do you want at random? "))
randomLetterFreq(num_of_letters)