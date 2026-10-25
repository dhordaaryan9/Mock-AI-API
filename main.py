from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app  = FastAPI(title="Mock AI API")

class TextRequest(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "API is live on Render!"}

@app.post("/analyze")
def analyze_text(request: TextRequest):
    word_count = len(request.text.split())
    return {"status": "seccess", "word_count": word_count}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0" , port=8000)