# Dictionary Comprehension

nba_players = {'Durant':37, "Steph":34,"Luka":25, "Edwards":5}

veterans = {k:v for (k,v) in nba_players.items() if v > 30}

print(veterans)