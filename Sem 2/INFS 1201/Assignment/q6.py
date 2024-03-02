from q4 import calculateTeamPoints

def highestScoringTeam(matchData):
    '''gets the highest scoring teams from given match data
    
    parameters:
    matchData -- a 1D list consist of 4-tuples in the form of (team1, team2, goal1, goal2)

    returns:
    max_score    -- highest points throughout each team's total scores
    highestTeams -- teams who have scored the respective max_score
    '''
    scores = calculateTeamPoints(matchData)
    max_score = 0
    for i in scores:
        if i[1] > max_score:
            max_score = i[1]
    
    highestTeams = []
    for i in scores:
        if i[1] == max_score:
            highestTeams.append(i[0])
    return max_score, highestTeams




'''
#Test cases 1  
matchData = [
 ('Qatar', 'Iraq', 3, 2),
 ('Jordan', 'Qatar', 1, 1)
]

print(highestScoringTeam(matchData))
# Expected output: (4, ['Qatar'])
#Test cases 2
# Sample Run
matchData = [
 ('Qatar', 'Iraq', 3, 2),
 ('Jordan', 'Qatar', 1, 1),
 ('Jordan', 'Palestine', 3, 1)
]

result = highestScoringTeam(matchData)
print(result)
# Expected output: (4, ['Qatar', 'Jordan']) 
'''