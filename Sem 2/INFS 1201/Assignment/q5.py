def topGoalScorers(goalData):
    top_scorers = []

    max_goal = 0

    for i in range(0,len(goalData),3):
        if goalData[i+2] > max_goal:
            max_goal = goalData[i+2]

    for i in range(0,len(goalData),3):
        country = goalData[i]
        player = goalData[i+1]
        goal = goalData[i+2]

        if goal == max_goal:
            top_scorers.append((country, player, goal))

    return top_scorers




'''
#Test cases
# Sample Run
goalData = ['Qatar', 'Hassan Al-Haydos', 3, 'Qatar', 'Akram Afif', 1, 'Iraq', 'Amir Al-Ammari', 2, 'Iraq', 'Hussein Ali', 1, 'Jordan', 'Mahmoud Al-Mardi', 2, 'Jordan', 'Musa Al-Taamari', 1, 'Palestine', 'Oday Dabbagh', 3, 'Palestine', 'Bader Nasser', 1]

print(topGoalScorers(goalData))
# Expected output: [('Qatar', 'Hassan Al-Haydos', 3), ('Palestine', 'Oday Dabbagh', 3)]
'''