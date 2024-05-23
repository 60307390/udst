# Gowshikrajan
# 60307390
# INFS1101 - 16
# StudyHours


name = input("What is your name? ")
totalHours = 0
monthNum = 1

name = name.capitalize()

# Default values for avgMin and avgMax because:
avgMin = 168    # Since 168 is the upper limit, for all numbers n, n <= 168. So, minimum number will be n.
avgMax = 0      # Since 0 is the lower limit, for all numbers n, n >= 0. So, maximum number will be n.

maxMonth = 1
minMonth = 1

newMonth = input("Do you want to enter data for a new month? (yes/no) ").lower()

if newMonth == 'no':
    print("bye")
else:
    while newMonth == 'yes':
        print(f"--Entering data for month {monthNum}--")
        weekN = 1
        
        hoursPrev = 0
        totalHours_i = 0    # Not to be confused with totalHours. This variable is applied only in this loop.
        
        while weekN <= 4:
            hours_i = int(input(f"How many hours did you spend studying in week {weekN}? "))
            
            totalHours += hours_i
            totalHours_i += hours_i     # SEPARATE from totalHours
            
            weekN += 1
            
            if hoursPrev == 0:  #0 is the default state, therefore this runs everytime a user enters the first hour
                print(f"Good effort, {name}!")
            elif hours_i > hoursPrev:
                print(f"Great job, {name}! You've increased your study hours!")
            elif hours_i < hoursPrev:
                print(f"You've studied less this week compared to the last, {name}. Try to keep your hours up!")
            else:               # Here, hours_i == hoursPrev
                print(f"Good consistency, {name}! Keep it up!")
            hoursPrev = hours_i # Setting hoursPrev to the current i-th hour to be refernced in the next loop (i+1)

        avg_i = totalHours_i / 4
        if avg_i < avgMin:
            avgMin = avg_i    # New minimum, similar to hoursPrev
            minMonth = monthNum
        if avg_i > avgMax:
            avgMax = avg_i    # New maximum, similar to hoursPrev
            maxMonth = monthNum
            
        monthNum += 1
        newMonth = input("Do you want to enter data for a new month? (yes/no) ")

    print("Calculating total and average...")

    avgHours = totalHours / ((monthNum-1) * 4)

    print(f"{name}, the total hours you spent studying during these months is: {totalHours} hours.")
    print(f"The overall average per week is: {avgHours} hours.")

    print(f"{name}, during these months you have studied the most in Month {maxMonth} with an average of {avgMax} hours.")
    print(f"Your lowest study hours were in Month {minMonth} with an average of {avgMin} hours.")
