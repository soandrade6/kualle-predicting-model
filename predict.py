import requests
from config import API_URL
from predict_model.model import load_model
from database import get_collection
from preprocessing import preprocess_data

def make_predictions():
    response = requests.get(API_URL)
    data = response.json()
    df, features = preprocess_data(data)
    
    model = load_model()
    predictions = model.predict(features)
    df['risk_level'] = predictions.clip(0, 100)
    
    collection = get_collection()
    for _, row in df.iterrows():
        collection.update_one(
            {"employee_id": row["employee_id"]},  
            {"$set": {"risk_level": round(row["risk_level"], 2)}}  
        )
    
    print("Actualización completada en MongoDB")