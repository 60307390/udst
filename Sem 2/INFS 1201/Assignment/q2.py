def predictMatchWinner(team1, team2, data):
    'returns the predicted match winner between the given two teams based on the previous historical data with the parameter `data`.'
    for stat in data:
        if team1.capitalize() in stat and team2.capitalize() in stat:
            if stat[2][1] > stat[2][3]:
                return stat[0]
            elif stat[2][1] < stat[2][3]:
                return stat[1]
            return None
    return None
