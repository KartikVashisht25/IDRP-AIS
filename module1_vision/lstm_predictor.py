def predict_lstm(features):

    ear = features["ear"]

    blink = features["blink_rate"]

    if ear < 0.20 and blink > 20:

        return 0.9

    elif ear < 0.25:

        return 0.5

    else:

        return 0.1