##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 3

def stringManipulation(s):
    sarcastic_string = ""
    num_vowels = 0

    if len(s)%2 == 0:
        middle_char = s[(len(s)//2)-1]+s[len(s)//2]
    else:
        middle_char = s[len(s)//2]

    for i in range(len(s)):
        if i%2==0:
            sarcastic_string += s[i].upper()
        else:
            sarcastic_string += s[i].lower()

        if s[i] in 'aeiou':
            num_vowels += 1
    return sarcastic_string, num_vowels, middle_char

something = input("Enter something: ")
manipulated_str, vowel_count, middle_character = stringManipulation(something)
print(f"Modified text: {manipulated_str}")
print(f"It includes: {vowel_count} vowels.")
print(f"Mid character: {middle_character}")
    

    
