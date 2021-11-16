##############################
## Name: Raekwon Adams-Rodgers
##############################

import pandas as pd


data = pd.read_csv(r'F:\Projects\Python\venv\shots_data.csv')

df = pd.DataFrame(data, columns= ['team', 'x', 'y', 'fgmade'])


teamStats = df.values.tolist()



team_A = []
team_B = []


for i in range(len(teamStats)):
    if(teamStats[i][0] == 'Team A'):
        team_A.append(teamStats[i])
    elif(teamStats[i][0] == 'Team B'):
        team_B.append(teamStats[i])

def getZoneDistribution(arr):
    team_2PTM = 0
    team_2PTA = 0

    team_C3M = 0
    team_C3A = 0

    team_NC3M = 0
    team_NC3A = 0
    team_totalFGA = 0

    for j in range(len(arr)):
        # Corner 3
        if (abs(arr[j][1]) > 22 and arr[j][2] <= 7.8):
            if arr[j][3] == 1:
                team_C3M += 1
            team_C3A += 1
        # Non-Corner 3
        elif ((abs(arr[j][1]) > 22 and arr[j][2] < 7.8) or arr[j][2] >= 23.75):
            if arr[j][3] == 1:
                team_NC3M += 1
            team_NC3A += 1
        # Inside the arc
        else:
            if arr[j][3] == 1:
                team_2PTM += 1
            team_2PTA += 1
        team_totalFGA += 1

    message = f'''
    The team shot distributions within each zone are as calculated:
    Team: {arr[0][0]}
    2 Point: {round((team_2PTA / team_totalFGA), 4)}
    Corner 3: {round((team_C3A / team_totalFGA) , 4)}
    Non-Corner 3: {round((team_NC3A/ team_totalFGA) , 4)}
    
    The effective field goal percentages within each zone are as calculated:
    2 Point: {effectiveFieldGoal(team_2PTM, 0, team_2PTA)}
    Corner 3: {effectiveFieldGoal(team_C3M, team_C3M, team_C3A)}
    Non-Corner 3: {effectiveFieldGoal(team_NC3M, team_NC3M, team_NC3A)}
    '''
    print(message)

def effectiveFieldGoal(FGM, threePM, FGA):
    return round(((FGM + (0.5 * threePM))/FGA), 4)

getZoneDistribution(team_A)
print('-----------------------------------------------')
getZoneDistribution(team_B)