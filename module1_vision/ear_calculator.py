import numpy as np

def calculate_ear(landmarks, frame_shape):
    h, w, _ = frame_shape

    left_eye = [33, 160, 158, 133, 153, 144]

    points = []

    for idx in left_eye:
        lm = landmarks.landmark[idx]
        x, y = int(lm.x * w), int(lm.y * h)
        points.append((x, y))

    vertical1 = np.linalg.norm(np.array(points[1]) - np.array(points[5]))
    vertical2 = np.linalg.norm(np.array(points[2]) - np.array(points[4]))
    horizontal = np.linalg.norm(np.array(points[0]) - np.array(points[3]))

    ear = (vertical1 + vertical2) / (2.0 * horizontal)

    return ear