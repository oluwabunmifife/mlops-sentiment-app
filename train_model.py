import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample training data
texts = [
    "I love this product!",
    "This is the best thing ever",
    "Absolutely fantastic experience",
    "I'm so happy with this",
    "I hate this",
    "This is awful",
    "Worst experience of my life",
    "Terrible and disappointing"
]

labels = [
    "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative"
]

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Save model and vectorizer to a .pkl file
model_data = {
    "model": model,
    "vectorizer": vectorizer
}

with open("app/model.pkl", "wb") as f:
    pickle.dump(model_data, f)

print("✅ Model trained and saved to app/model.pkl")