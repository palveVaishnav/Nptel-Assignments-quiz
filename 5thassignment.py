#SOLUTION BY INSTRUCTOR:


# Statistics will be stored as a dictionary
# Each key is a player name, each value is a list of 6 integers 
# representing 
#   Best of 5 set matches won,
#   Best of 3 set matches won,
#   Sets won
#   Games won
#   Sets lost (store as negative number for comparison)
#   Games lost (store as negative number for comparison)
stats = {}   

# Read a line of input
line = input()
while line:
  # Keep track of sets/games won and lost in this match
  # with respect to winner of the match
  (wsets,lsets,wgames,lgames) = (0,0,0,0)

  # Extract winner, loser and string of setscores
  (winner,loser,setscores) = line.strip().split(':',2)

  # Extract sequence of sets from setscores
  sets = setscores.split(',')

  for set in sets:
    # Process each set
    (winstr,losestr) = set.split('-')
    win = int(winstr)
    lose = int(losestr)
    wgames = wgames + win
    lgames = lgames + lose
    if win > lose:
      wsets = wsets + 1
    else:
      lsets = lsets + 1

  # Update statistics for each of the players

  for player in [winner,loser]:
    try:
      stats[player]
    except KeyError:
      stats[player] = [0,0,0,0,0,0]

  if wsets >= 3:
    stats[winner][0] = stats[winner][0] + 1
  else:
    stats[winner][1] = stats[winner][1] + 1

  stats[winner][2] = stats[winner][2] + wsets
  stats[winner][3] = stats[winner][3] + wgames
  stats[winner][4] = stats[winner][4] - lsets
  stats[winner][5] = stats[winner][5] - lgames

  stats[loser][2] = stats[loser][2] + lsets
  stats[loser][3] = stats[loser][3] + lgames
  stats[loser][4] = stats[loser][4] - wsets
  stats[loser][5] = stats[loser][5] - wgames

  line = input()

# Collect each player's stats as a tuple, name last    
statlist = [(stat[0],stat[1],stat[2],stat[3],stat[4],stat[5],name) for name in stats.keys() for stat in [stats[name]]]

# Sort the statistics in descending order
# Losing games are stored negatively for sorting correctly
statlist.sort(reverse = True)

# Print
for entry in statlist:
    print(entry[6],entry[0],entry[1],entry[2],entry[3], -entry[4], -entry[5])


    
    
    
    
    
    
    
      
#ALTERNATE SOLUTION
data=input()
result={}
while data:
    winner, loser, sets = data.split(':')
    winner_sets, loser_sets = 0, 0
    winner_games, loser_games = 0, 0 
    winner_BO5, winner_BO3 = 0, 0
    
    for i in sets.split(','):
        score = list(map(int, i.split('-')))
        
        if score[0] > score[1]:
            winner_sets += 1
        else:
            loser_sets += 1

        winner_games += score[0]
        loser_games += score[1]

    if winner_sets >= 3:
        winner_BO5 += 1
    else:
        winner_BO3 += 1

    if winner not in result:
      result[winner] = [0, 0, 0, 0, 0, 0]
    if loser not in result:
      result[loser] = [0, 0, 0, 0, 0, 0]
    
    result[winner][0] += winner_BO5
    result[winner][1] += winner_BO3
    result[winner][2] += winner_sets
    result[winner][3] += winner_games
    result[winner][4] += loser_sets
    result[winner][5] += loser_games

    result[loser][2] += loser_sets
    result[loser][3] += loser_games
    result[loser][4] += winner_sets
    result[loser][5] += winner_games

    data=input()   

result = sorted(result.items(), key=lambda t:t[1], reverse=True)

for player in result:
      print(f"{player[0]} {player[1][0]} {player[1][1]} {player[1][2]} {player[1][3]} {player[1][4]} {player[1][5]}")

    
    

