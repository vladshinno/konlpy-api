import os
from fastapi import FastAPI, Header, HTTPException
from konlpy.tag import Okt

app = FastAPI()
okt = Okt()

SECRET = os.getenv("KONLPY_API_SECRET")

@app.get("/analyze")
def analyze(text: str, x_api_key: str = Header(None)):
    if x_api_key != SECRET:
        raise HTTPException(status_code=403)

    return {
        "morphs": okt.morphs(text)
    }
