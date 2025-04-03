import pickle
from config import MODEL_PATH

def load_model():
    with open(MODEL_PATH, "rb") as archivo:
        return pickle.load(archivo)