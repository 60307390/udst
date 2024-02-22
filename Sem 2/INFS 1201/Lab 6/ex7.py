##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 7
import random

def shuffleString(text):
    used = []
    new_text = ""
    for i in range(len(text)):
        k = random.randrange(0,len(text))
        while k in used:
            k = random.randrange(0,len(text))
        new_text += text[k]
        used.append(k)
    return new_text
