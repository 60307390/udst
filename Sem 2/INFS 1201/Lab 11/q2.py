##
#Gowshikrajan Senthilkumar - 60307390
# Lab 11
#Exercise 2

def collatz_func(n):
    'piecewise function to be used recursively in Collatz sequence'
    if n == 1:
        return 1
    if n % 2:
        return 3*n + 1
    else:
        return n//2

def collatz(init):
    'returns a list consisting of Collatz sequence of a_0 (init) until for some i : a_i = 1'
    if init == 1:
        return [1]
    else:
        return [init] + collatz(collatz_func(init))
    
    
    
