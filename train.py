import pandas as pd
import pickle
import os
import sys
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load dataset
try:
    df = pd.read_csv("data/matches.csv")
except pd.errors.EmptyDataError:
    print("❌ Error: The file 'data/matches.csv' is empty. Please add data to it.")
    sys.exit(1)
except FileNotFoundError:
    print("❌ Error: The file 'data/matches.csv' was not found.")
    sys.exit(1)

# Select useful columns
df = df[['team1', 'team2', 'venue', 'toss_winner', 'winner']].dropna()

# Get all unique teams to ensure consistent encoding across team columns
all_teams = pd.concat([df['team1'], df['team2'], df['toss_winner'], df['winner']]).unique()

# Encode categorical columns
encoder = {}
for col in df.columns:
    le = LabelEncoder()
    if col in ['team1', 'team2', 'toss_winner', 'winner']:
        le.fit(all_teams)
        df[col] = le.transform(df[col])
    else:
        df[col] = le.fit_transform(df[col])
    encoder[col] = le

# Split data
X = df.drop("winner", axis=1)
y = df["winner"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train.values, y_train)

# Save model + encoder
os.makedirs("model", exist_ok=True)
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("model/encoder.pkl", "wb") as f:
    pickle.dump(encoder, f)

print("✅ Model trained and saved")