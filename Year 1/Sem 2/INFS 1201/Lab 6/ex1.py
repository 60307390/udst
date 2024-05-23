##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 1

fruits = ["banana","strawberry","kiwi","orange"]

res = ""
for i in fruits:
    res += f'{i}\\'
favourite_fruits = res[:-1]

print(f"Your favourite fruits are: {favourite_fruits}")
