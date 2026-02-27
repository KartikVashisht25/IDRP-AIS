import random
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

def generate_data(samples_per_class=500):
    data=[]
    #SAFE CLASS(0)
    for _ in range(samples_per_class):
        data.append([
            random.uniform(0.25, 0.35), #ear
            random.randint(8, 15),      #blink rate
            random.uniform(0.1, 0.5),   #eye closure duration
            random.uniform(-5, 5),      #head pitch
            random.uniform(-5, 5),      #head yaw
            random.uniform(-3, 3),      # head roll
            0
        ])
    

    #MODERATE CLASS(1)
    for _ in range(samples_per_class):
        data.append([
            random.uniform(0.20, 0.25),
            random.randint(15, 22),
            random.uniform(0.5, 1.0),
            random.uniform(-10, 10),
            random.uniform(-10, 10),
            random.uniform(-6, 6),
            1
        ])

        
    #HIGH RISK CLASS(2)
    for _ in range(samples_per_class):
        data.append([
            random.uniform(0.15, 0.20),
            random.randint(22, 35),
            random.uniform(1.0, 2.0),
            random.uniform(-20, 20),
            random.uniform(-20, 20),
            random.uniform(-10, 10),
            2
        ])

    columns = [
        "ear",
        "blink_rate",
        "eye_closure_duration",
        "head_pitch",
        "head_yaw",
        "head_roll",
        "risk_level",
    ]
    return pd.DataFrame(data, columns=columns)



#TRAINING FUNCTION

def train_model():
    df = generate_data()
    X = df.drop("risk_level", axis=1)
    y = df["risk_level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(
        n_estimators = 100,
        random_state = 42,
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    print("\nModel Accuracy:", accuracy_score(y_test, predictions))
    print("\nClassification Report:\n")
    print(classification_report(y_test, predictions))

    #SAVE MODEL
    os.makedirs("module2_ml/model", exist_ok = True)
    joblib.dump(model, "module2_ml/model/risk_model.pkl")

    print("\nModel saved successfully!!")

if __name__ == "__main__":
    train_model()    

