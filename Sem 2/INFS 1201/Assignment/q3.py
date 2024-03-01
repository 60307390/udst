def inputMatchData():
    'prints a 2D list based on the input of teams, scores, and scoring players given by the user'
    matchData = []

    numMatches = int(input("Enter the number of matches: "))
    
    for _ in range(numMatches):

        teams = input("Enter the teams playing the matches (separated by a comma): ")
        while ',' not in teams:
            teams = input("Enter the teams playing the matches (separated by a comma): ")
        teams = teams.split(',')

        scores = input("Enter the final scores of the match: ")
        while ' ' not in scores:
            scores = input("Enter the final scores of the match: ")
        scores = scores.split(' ')

        team_data = teams
        for i in scores:
            team_data.append(int(scores))

        for i in range(len(scores)): 
            team_score = []
            for j in range(int(scores[i])):
                team_score.append(input(f"Enter goal #{j+1} for {team_data[i].strip().capitalize()}: "))
            team_data.append(team_score)
        matchData.append(team_data)

    print(matchData)

inputMatchData()