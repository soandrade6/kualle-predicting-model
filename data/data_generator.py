import pandas as pd
import uuid
import random
from faker import Faker

fake = Faker()

roles = ["Manager", "Analyst", "Operator", "Engineer", "Technician"]
economic_activities = [(1001, "Agriculture"), (3003, "Construction"), (4004, "Retail"), (5005, "Finance")]
education_levels = ["High School", "Bachelor's Degree", "Master's Degree", "PhD"]
genders = ["Male", "Female"]

num_records = 100

data = []
for i in range(1, num_records + 1):
    record = {
        "id": str(uuid.uuid4()),
        "employee_id": i,
        "name": fake.name(),
        "role": random.choice(roles),
        "gender": random.choice(genders),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d'),
        "economic_activity_code": (activity := random.choice(economic_activities))[0],
        "economic_activity_name": activity[1],
        "education_level": random.choice(education_levels),
        "risk_level": round(random.uniform(0, 100), 2)
    }
    data.append(record)

df = pd.DataFrame(data)
file_path = "data/data_train.csv"
df.to_csv(file_path, index=False)

print(f"Archivo CSV generado: {file_path}")
