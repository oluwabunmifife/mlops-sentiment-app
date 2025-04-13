import pickle
import os

def load_model():
    with open("app/model.pkl", "rb") as f:
        model_data = pickle.load(f)
    return model_data['model'], model_data['vectorizer']

def predict(model, vectorizer, text):
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return prediction