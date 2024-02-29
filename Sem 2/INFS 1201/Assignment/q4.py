def calculateTeamPoints(matchData):
    teams = []
    points = []

    for i in range(len(matchData)):
        team1 = matchData[i][0]
        team2 = matchData[i][1]
        goal1 = matchData[i][2]
        goal2 = matchData[i][3]

        if team1 not in teams:
            teams.append(team1)
            points.insert(teams.index(team1),0)
        if team2 not in teams:
            teams.append(team2)
            points.insert(teams.index(team2),0)
        
        if goal1 > goal2:
            points[teams.index(team1)] += 3
        if goal1 == goal2:
            points[teams.index(team1)] += 1
            points[teams.index(team2)] += 1
        if goal1 < goal2:
            points[teams.index(team2)] += 3
    
    print(teams, points)

    team_points = []
    for i in range(len(teams)):
        team_points.append([teams[i],points[i]])

    return team_points



'''
matchData = [
    ['Qatar', 'Iraq', 3, 2],
    ['Jordan', 'Qatar', 1, 1],
    ['Jordan', 'Palestine', 1, 2]
]

team_points = calculateTeamPoints(matchData)
print(team_points)
'''