##
#Gowshikrajan Senthilkumar - 60307390
# Lab 11
#Exercise 1

def arithmeticGeometric(index, const, ratio, initial):
    'returns nth (index) term of AGP with given conditions'
    if index == 0:
        return initial
    return ratio*arithmeticGeometric(index-1, const, ratio, initial) + const

