from pydantic import BaseModel

class MatchInput(BaseModel):
    team1: str
    team2: str