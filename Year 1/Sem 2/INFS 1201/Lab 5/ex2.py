##
# Gowshikrajan Senthilkumar - 60307390
# Week5 lab
# Exercise 2


days = input("Number of days for the experiment: ")
while not days.isdecimal() or int(days) < 0:
    print("Invalid input.")
    days = input("Number of days for the experiment: ")
days = int(days)

total_temp = 0

max_temp = -273.15

for i in range(days):
    while True:
        try:
            temp_i = float(input(f"Enter temperature for day {i+1}: "))
            while temp_i < -273.15:
                print("Be careful, you entered an incorrect value for the temperature.")
                temp_i = float(input(f"Enter temperature for day {i+1}: "))
            break
        except ValueError:
            print("Be careful, you entered an incorrect value for the temperature.")
    
    if max_temp < temp_i:
        max_temp = temp_i
        max_temp_day = i+1
        
    if i == 0 or min_temp > temp_i:
        min_temp = temp_i
        min_temp_day = i+1

    total_temp += temp_i

if days > 0:
    avg_temp = total_temp/days

    print(f"The average temperature over these {days} days is {avg_temp}")
    print(f"The maximum temperature over these {days} days was {max_temp} which was recorded on day {max_temp_day}")
    print(f"The minimum temperature over these {days} days was {min_temp} which was recorded on day {min_temp_day}")
else:
    print(f"There is no value of temperature as experiment lasted zero days.")
print("End of experiment.")
        
