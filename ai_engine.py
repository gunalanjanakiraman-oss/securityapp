from sklearn.ensemble import IsolationForest
import numpy as np

model = IsolationForest(contamination=0.15)

def train_model():
    data = np.array([
        [20, 30], [25, 35], [30, 40],
        [35, 45], [40, 50]
    ])
    model.fit(data)

def is_anomaly(cpu, ram):
    return model.predict([[cpu, ram]])[0] == -1
