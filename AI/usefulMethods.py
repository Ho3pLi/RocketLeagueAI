def calculatePlayerScore(data):
    goals = data['goals']
    shots = data['shots']
    if (shots > 0).any():
        shooting_percentage = goals / shots
    else:
        shooting_percentage = 0

    saves = data['saves']
    assists = data['assists']
    boostAmount = data['avg boost amount']
    supersonicTime = data['amount used while supersonic']
    demosInflicted = data['demos inflicted']
    demosTaken = data['demos taken']

    score = (shooting_percentage * 100) + (saves * 20) + (assists * 30) + (boostAmount * 5) + (supersonicTime * 0.01) + (demosInflicted * 50) - (demosTaken * 30)

    print(data['player name'])
    return score