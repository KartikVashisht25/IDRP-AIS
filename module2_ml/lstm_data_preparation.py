import numpy as np

def create_sequences(data, sequence_length=10):
    sequences = []
    labels = []

    for i in range(len(data) - sequence_length):
        seq = data[i:i + sequence_length]
        label = data[i + sequence_length][-1]  # last column as label

        sequences.append(seq[:, :-1])  # features
        labels.append(label)

    return np.array(sequences), np.array(labels)