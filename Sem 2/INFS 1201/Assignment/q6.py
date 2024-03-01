from q4 import calculateTeamPoints

def highestScoringTeam(data):
    scores = calculateTeamPoints(data)
    max_score = 0
    for i in scores:
        if i[1] > max_score:
            max_score = i[1]
    
    highestTeams = [max_score, []]
    for i in scores:
        if i[1] == max_score:
            highestTeams[1].append(i[0])
    return highestTeams




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