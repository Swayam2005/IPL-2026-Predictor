from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pickle
import random

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

model = pickle.load(open("model/model.pkl", "rb"))
encoder = pickle.load(open("model/encoder.pkl", "rb"))

teams = list(encoder['team1'].classes_)
venues = list(encoder['venue'].classes_)

def encode(col, value):
    return encoder[col].transform([value])[0]

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html", context={"teams": teams, "venues": venues}
    )

@app.post("/predict")
def predict(request: Request, team1: str = Form(...), team2: str = Form(...), venue: str = Form(...)):
    # Randomly decide toss winner
    toss_winner = random.choice([team1, team2])

    data = [[
        encode('team1', team1),
        encode('team2', team2),
        encode('venue', venue),
        encode('toss_winner', toss_winner)
    ]]

    pred = model.predict(data)
    winner = encoder['winner'].inverse_transform(pred)[0]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"teams": teams, "venues": venues, "result": winner, "team1_sel": team1, "team2_sel": team2, "venue_sel": venue, "toss_winner": toss_winner}
    )

@app.get("/simulate")
def simulate_tournament(request: Request):
    # Base points from actual IPL 2026 mid-season standings
    points = {
        'Punjab Kings': 13,
        'Royal Challengers Bangalore': 12,
        'Sunrisers Hyderabad': 12,
        'Rajasthan Royals': 12,
        'Gujarat Titans': 12,
        'Chennai Super Kings': 8,
        'Delhi Capitals': 8,
        'Kolkata Knight Riders': 7,
        'Mumbai Indians': 6,
        'Lucknow Super Giants': 6
    }
    for team in teams:
        if team not in points:
            points[team] = 0
    
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            t1, t2 = teams[i], teams[j]
            
            venue = random.choice(venues)
            toss = random.choice([t1, t2])
            
            data = [[
                encode('team1', t1),
                encode('team2', t2),
                encode('venue', venue),
                encode('toss_winner', toss)
            ]]
            
            pred = model.predict(data)
            winner = encoder['winner'].inverse_transform(pred)[0]
            points[winner] += 2
            
    table = sorted(points.items(), key=lambda x: x[1], reverse=True)
    champion = table[0][0]
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"teams": teams, "venues": venues, "simulation": True, "champion": champion, "points_table": table}
    )
from app.schema import MatchInput

@app.post("/predict_api")
def predict_api(data: MatchInput):
    venue = random.choice(encoder['venue'].classes_)
    toss = random.choice([data.team1, data.team2])

    input_data = [[
        encode('team1', data.team1),
        encode('team2', data.team2),
        encode('venue', venue),
        encode('toss_winner', toss)
    ]]

    pred = model.predict(input_data)
    winner = encoder['winner'].inverse_transform(pred)[0]

    return {"winner": winner}