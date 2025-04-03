import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(data):
    df = pd.DataFrame(data)
    df['birth_date'] = pd.to_datetime(df['birth_date'])
    df['age'] = 2025 - df['birth_date'].dt.year
    
    label_encoders = {}
    for col in ['education_level', 'gender', 'role']:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le
    
    features = df[['age', 'economic_activity_code', 'education_level', 'gender', 'role']]
    return df, features