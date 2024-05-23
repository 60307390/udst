def checkMatchUpDistance(prize, fan):
    '''calculates the match-up distance between the prize ticket number and a given fan\'s ticket number
    
    paramaters: 
    prize   -- the ticket number used for the prize (must be same length as fan)
    fan     -- the ticket number of the respective fan (must be same length as prize)

    returns: 
    4-tuple of match-up distance, fan's ticket, difference of string, and a statement of the result
    '''
    if len(fan) != len(prize):
        return None
    diff_str = ""
    match_distance = 0

    for i in range(len(fan)):
        if fan[i] != prize[i]:
            match_distance += 1
            diff_str += prize[i]
        else:
            diff_str += "*"

    prize_statement = f"Your ticket number has a match-up distance of {match_distance}! "
    if match_distance == 0:
        prize_statement += "Congratulations, you are the winner of the Grand Prize: A VIP pass to enjoy the Qatar Asia Cups from the best seats in the stadium!"
    elif match_distance > 2:
        prize_statement += "Better luck next time!"
    else:
        prize_statement += "Congratulations, you win a small prize: An exclusive Qatar Asia Cups-themed football jersey."
    return match_distance, fan, diff_str, prize_statement