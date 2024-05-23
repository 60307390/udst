##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 8


def drawTriangle(size, character='*', direction='l'):
    '''
    draws an ascii triangle.
    
    Parameters:
        size (int): size of the triangle legs
        character (string): character corresponding to the unit drawing
        direction (string): l for lower triangle, u for upper triangle
    Returns:
        none
    '''
    if direction == 'l':
        for i in range(size):
            print(character*(i+1))
    else:
        for i in range(size,0,-1):
            print(' '*(size-i)+character*i)

            
