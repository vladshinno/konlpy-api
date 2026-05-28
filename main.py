from fastapi import FastAPI
from konlpy.tag import Okt

app = FastAPI()
okt = Okt()

@app.get("/analyze")
def analyze(text: str):
    return {"result": okt.pos(text)}
