import joblib

def load_model(path="models/isolation_forest.pkl"):
    model = joblib.load(path)
    return model