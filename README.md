#  IPL 2026 Match Predictor
## Screenshots

![Screenshot1](Screenshots/Ss1.jpeg)
![Screenshot2](Screenshots/Ss2.jpeg)
![Screenshot3](Screenshots/Ss3.jpeg)
![Screenshot4](Screenshots/Ss4.jpeg)


A Machine Learning + FastAPI project that predicts IPL match winners and simulates tournament outcomes.

## Features
- Match winner prediction
- FastAPI backend
- Clean ML pipeline
- Realistic data generation

## Tech Stack
- Python
- FastAPI
- Scikit-learn
- Pandas

## API Endpoints

POST /predict_api

Example request:
{
  "team1": "MI",
  "team2": "CSK"
}

Response:
{
  "winner": "MI"
}

## Setup

pip install -r requirements.txt

# Generate dataset
python generate_realistic_data.py

# Train model
python train.py

# Run server
python run.py

## ⚠️ Limitations

This model predicts IPL match outcomes using historical and simulated data. 
While it captures general trends and team strengths, cricket matches are inherently unpredictable.

The model does not account for real-time factors such as:
- Player form and injuries
- Pitch and weather conditions
- In-game decisions

Therefore, predictions should be considered as probabilistic insights rather than exact outcomes.
