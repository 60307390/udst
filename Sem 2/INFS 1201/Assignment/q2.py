def predictMatchWinner(team1, team2, data):
    '''predicts the winner between two given teams based on historical data
    
    paramaters: 
    team1 -- name of first team
    team2 -- name of second team
    data  -- historical data used to predict the winner

    returns
    predicted winner based on list
    '''
    for stat in data:
        if team1.capitalize() in stat and team2.capitalize() in stat:
            if stat[2][1] > stat[2][3]:
                return stat[0]
            elif stat[2][1] < stat[2][3]:
                return stat[1]
            return None
    return None
