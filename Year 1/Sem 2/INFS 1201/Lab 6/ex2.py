##
# Gowshikrajan Senthilkumar - 60307390
# Week6 lab
# Exercise 2

def cardinal(num):
    num = str(num)
    suffix = 'th'

    if num[-2:] == '11' or num[-2:] == '12' or num[-2:] == '13':
        suffix = 'th'
    elif num[-1] == '1':
        suffix = 'st'
    elif num[-1] == '2':
        suffix = 'nd'
    elif num[-1] == '3':
        suffix = 'rd'
    
    return suffix
num_list = []

for i in range(10):
    num_list.append(int(input("Enter an integer: ")))

print(f"We just built the following list {num_list}")

for i in range(len(num_list)):
    print(f"The {str(i+1)+cardinal(i+1)} element in your list is: {num_list[i]}")

