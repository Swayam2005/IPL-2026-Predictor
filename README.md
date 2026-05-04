#  IPL 2026 Match Predictor

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

```bash
pip install -r requirements.txt
python train.py
python run.py
## Dataset
Dataset is not included in the repository.

To generate dataset:
python generate_realistic_data.py

## Train Model
python train.py
