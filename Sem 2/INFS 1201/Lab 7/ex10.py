##
# Gowshikrajan Senthilkumar - 60307390
# Week8 lab
# Exercise 10

def getNumDigits(n):
    return len(str(n))

size = int(input("What size of multiplication table do you want? "))

justify_length = getNumDigits(size**2)+1 

# first row
print('|'.rjust(getNumDigits(size)+1), end='')
for i in range(1,size+1):
    print(str(i).rjust(justify_length), end='')

# seperator
print('\n'+ '-'*getNumDigits(size) +'+'+'-'*(size*justify_length),end='')

# table part
for i in range(1,size+1):
    print('\n' + f'{i}|'.rjust(getNumDigits(size)+1),end='')
    for j in range(1,size+1):
       print(str(i*j).rjust(justify_length), end='') 
