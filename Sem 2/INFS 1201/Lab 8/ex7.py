##
# Gowshikrajan Senthilkumar - 60307390
# Week8 lab
# Exercise 7

size = int(input("What size of multiplication table do you want? "))

justify_length = len(str(size**2))+1 

# first row
print(' |', end='')
for i in range(1,size+1):
    print(str(i).rjust(justify_length), end='')

# seperator
print('\n-+'+'-'*(size*(justify_length)),end='')

# table part
for i in range(1,size+1):
    print(f'\n{i}|',end='')
    for j in range(1,size+1):
       print(str(i*j).rjust(justify_length), end='') 
