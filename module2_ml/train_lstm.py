import numpy as np
from lstm_model import build_lstm_model
from lstm_data_preparation import create_sequences

# Dummy data (replace later with real dataset)
#data = np.random.rand(200, 6)  # 5 features + 1 label
data = np.random.rand(200, 7)  # 6 features + 1 label

X, y = create_sequences(data)

model = build_lstm_model((X.shape[1], X.shape[2]))

model.fit(X, y, epochs=10, batch_size=16)

# model.save("model/lstm_model.h5")
model.save("module2_ml/model/lstm_model.h5")

print("✅ LSTM Model Trained")