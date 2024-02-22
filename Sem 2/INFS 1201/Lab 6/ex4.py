##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 4

def drawBorder(width, height):
    'Draws the borders of a rectangle using ASCII art. '
    w,h = width, height     # easier to use while keeping docstring consistent
    if width < 2 or height < 2:
        print("Incorrect parameters, cannot draw such a rectangle!")
    else:
        for j in range(height):
            for i in range(width):
                char = ' '
                #corners in {(0,0),(w-1,0),(0,h-1),(w-1,h-1)}
                if [i,j] in [[0,0], [w-1,0], [0,h-1], [w-1,h-1]]:
                    char = '+'
                elif i in [0,w-1]:
                    char = '|'
                elif j in [0,h-1]:
                    char = '-'
                print(char,end='')
            print('',end='\n')
