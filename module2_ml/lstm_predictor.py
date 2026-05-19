eye_closed_frames = 0


def predict_lstm(features):

    global eye_closed_frames

    ear = features["ear"]

    blink = features["blink_rate"]

    # Eyes closed continuously
    if ear < 0.18:

        eye_closed_frames += 1

    else:

        eye_closed_frames = 0

    # High risk only if eyes closed for long
    if eye_closed_frames > 15:

        return 0.95

    # Drowsy state
    elif ear < 0.23:

        return 0.6

    # Excessive blinking
    elif blink > 30:

        return 0.5

    else:

        return 0.1