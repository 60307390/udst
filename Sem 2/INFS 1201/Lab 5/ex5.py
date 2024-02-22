##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 5

def shawarmaCost(numShawarma, priceShawarma):
    return (numShawarma-numShawarma//7)*priceShawarma

assert shawarmaCost(5, 11) == 55
assert shawarmaCost(6, 11) == 66
assert shawarmaCost(7, 11) == 66
assert shawarmaCost(8, 11) == 77
for i in range(1,20,4):
    assert shawarmaCost(0, i) == 0
    assert shawarmaCost(5, i) == 5 * i
    assert shawarmaCost(6, i) == 6 * i
    assert shawarmaCost(7, i) == 6 * i
    assert shawarmaCost(20, i) == 18 * i
    assert shawarmaCost(21, i) == 18 * i
    assert shawarmaCost(22, i) == 19 * i
assert shawarmaCost(8088083060, 10) == 69326426230 # the cost to buy shawarma for the entire world's current population at the price of udst shawarma
print("All good")

