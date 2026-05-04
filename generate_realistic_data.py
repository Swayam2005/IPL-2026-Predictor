import pandas as pd
import random
import os

# Team weights based on the user-provided IPL 2026 points table image:
# PBKS: 75%
# RCB: 66.6%
# SRH: 60%
# RR: 60%
# GT: 60%
# CSK: 44.4%
# DC: 44.4%
# KKR: 37.5%
# LSG: 25%
# MI: 22.2%

team_strengths = {
    "Punjab Kings": 75,
    "Royal Challengers Bangalore": 67,
    "Sunrisers Hyderabad": 60,
    "Rajasthan Royals": 60,
    "Gujarat Titans": 60,
    "Chennai Super Kings": 44,
    "Delhi Capitals": 44,
    "Kolkata Knight Riders": 38,
    "Lucknow Super Giants": 25,
    "Mumbai Indians": 22
}

venues = [
    "Wankhede Stadium", "Eden Gardens", "M. Chinnaswamy Stadium",
    "MA Chidambaram Stadium", "Narendra Modi Stadium", "Arun Jaitley Stadium",
    "Sawai Mansingh Stadium", "Rajiv Gandhi International Stadium"
]

teams = list(team_strengths.keys())

data = []
# Generate a large number of matches so the Random Forest can pick up the signal clearly
for _ in range(5000):
    t1, t2 = random.sample(teams, 2)
    venue = random.choice(venues)
    toss_winner = random.choice([t1, t2])
    
    # Calculate win probability based on strengths
    s1 = team_strengths[t1]
    s2 = team_strengths[t2]
    
    # Toss winner gets a slight +5 point boost in strength
    if toss_winner == t1:
        s1 += 5
    else:
        s2 += 5
        
    total_strength = s1 + s2
    p1 = s1 / total_strength
    
    # Determine winner based on weighted probability
    if random.random() < p1:
        winner = t1
    else:
        winner = t2
        
    data.append([t1, t2, venue, toss_winner, winner])

os.makedirs("data", exist_ok=True)
df = pd.DataFrame(data, columns=["team1", "team2", "venue", "toss_winner", "winner"])
df.to_csv("data/matches.csv", index=False)
print("✅ Realistic data successfully generated in 'data/matches.csv' based on IPL 2026 standings")
