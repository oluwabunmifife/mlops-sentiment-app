from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from model import load_model, predict

app = FastAPI()
model, vectorizer = load_model()

class TextInput(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(input: TextInput):
    if not input.text:
        raise HTTPException(status_code=400, detail="Text input is required.")
    prediction = predict(model, vectorizer, input.text)
    return {"prediction": prediction}