def calculateTeamPoints(matchData):
    '''calculates the points for each football team from given match data
    
    paramaters:
    matchData -- a 2-dimensional list consisting of goal data where each row is in format of [team1, team2, goal1, goal2]

    returns:
    team_points -- a 2-dimensional list consisting the team name and the total points accumulated through games using the match data
    '''
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
    
    #print(teams, points)

    team_points = []
    for i in range(len(teams)):
        team_points.append([teams[i],points[i]])

    return team_points



'''
#Test cases
# Sample Run
matchData = [
    ['Qatar', 'Iraq', 3, 2],
    ['Jordan', 'Qatar', 1, 1],
    ['Jordan', 'Palestine', 1, 2]
]

team_points = calculateTeamPoints(matchData)
print(team_points)
# Expected output: [['Qatar', 4], ['Iraq', 0], ['Jordan', 1], ['Palestine', 3]]

'''