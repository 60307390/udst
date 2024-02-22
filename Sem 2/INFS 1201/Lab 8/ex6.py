##
# Gowshikrajan Senthilkumar - 60307390
# Week8 lab
# Exercise 6
import random

def randMatrix(r, c):
    'returns a random matrix with size of r x c, and elements from 1 to r*c'
    x =list(range(1,r*c+1))
    random.shuffle(x)
    res = []
    for i in range(0,len(x),c):
        res.append(x[i:i+c])
    return res
